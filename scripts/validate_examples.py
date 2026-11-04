#!/usr/bin/env python3
"""Validate Toikatsu v0.1 JSON examples against schema and semantic rules.

Install: python -m pip install 'jsonschema>=4.18,<5'
Run:     python scripts/validate_examples.py
Override: python scripts/validate_examples.py --schema schemas/toikatsu-v0.1.schema.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from jsonschema import validators
except ImportError:
    sys.exit("ERROR: jsonschema is required. Run: python -m pip install jsonschema")

ROOT = Path(__file__).resolve().parents[1]

# An expected semantic reason prevents a negative fixture from passing merely
# because it fails for some unrelated reason.
REASONS = {
    "self-verified-contribution": "verifier_beneficiary_conflict",
    "verifier-beneficiary-conflict": "verifier_beneficiary_conflict",
    "verifier-proposer-conflict": "verifier_proposer_conflict",
    "candidate-contribution-handoff": "unverified_contribution_handoff",
    "rejected-contribution-handoff": "unverified_contribution_handoff",
    "activity-without-consent": "activity_consent_missing",
    "contribution-without-consent": "contribution_consent_missing",
    "handoff-without-consent": "handoff_consent_missing",
    "activity-after-withdrawal": "activity_after_withdrawal",
    "activity-at-withdrawal": "activity_after_withdrawal",
    "contribution-after-withdrawal": "contribution_after_withdrawal",
    "contribution-at-withdrawal": "contribution_after_withdrawal",
    "verification-after-withdrawal": "verification_after_withdrawal",
    "verification-at-withdrawal": "verification_after_withdrawal",
    "handoff-after-withdrawal": "handoff_after_withdrawal",
    "handoff-at-withdrawal": "handoff_after_withdrawal",
    "ready-after-withdrawal": "handoff_after_withdrawal",
    "handoff-without-receipt": "handoff_without_receipt",
    "duplicate-activity-id": "duplicate_activity_id",
    "duplicate-contribution-id": "duplicate_contribution_id",
    "duplicate-verification-id": "duplicate_verification_id",
    "verification-evidence-mismatch": "verification_evidence_mismatch",
    "verification-before-proposal": "verification_before_proposal",
    "timestamp-order-mismatch": "timestamp_order_mismatch",
    "contribution-target-mismatch": "contribution_target_mismatch",
}


def stamp(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt if dt.tzinfo is not None else None
    except ValueError:
        return None


def items(value: Any) -> list[dict[str, Any]]:
    return [x for x in value if isinstance(x, dict)] if isinstance(value, list) else []


def strings(value: Any) -> list[str]:
    return [x for x in value if isinstance(x, str)] if isinstance(value, list) else []


def semantic_errors(doc: dict[str, Any]) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []

    def err(code: str, where: str) -> None:
        errors.append((code, where))

    consent = doc.get("consent") or {}
    question = doc.get("question") or {}
    participant = doc.get("participant") or {}
    activities = items(doc.get("activities"))
    contributions = items(doc.get("contributions"))
    handoff = doc.get("handoff") or {}
    scopes = consent.get("scopes") or {}
    withdrawn = stamp(consent.get("withdrawn_at"))
    consent_time = stamp(consent.get("recorded_at"))
    is_withdrawn = consent.get("status") == "withdrawn"

    def check_consent(scope: str, at: Any, code: str, where: str) -> None:
        when = stamp(at)
        if not consent or scopes.get(scope) is not True:
            err(code, where)
        if consent_time and when and when < consent_time:
            err("timestamp_order_mismatch", where + ": before consent")
        # The instant of withdrawal is already outside the consent window.
        if is_withdrawn and withdrawn and when and when >= withdrawn:
            after_codes = {
                "activity_recording": "activity_after_withdrawal",
                "contribution_evaluation": "contribution_after_withdrawal",
                "external_handoff": "handoff_after_withdrawal",
            }
            err(after_codes[scope], where)

    if is_withdrawn and withdrawn is None:
        err("invalid_withdrawal", "consent.withdrawn_at")
    if consent.get("status") == "active" and consent.get("withdrawn_at") is not None:
        err("invalid_withdrawal", "consent.status")
    if withdrawn and consent_time and withdrawn < consent_time:
        err("timestamp_order_mismatch", "consent.withdrawn_at")

    def unique(records: list[dict[str, Any]], key: str, code: str) -> None:
        counts = Counter(x.get(key) for x in records if isinstance(x.get(key), str))
        for identifier, count in counts.items():
            if count > 1:
                err(code, f"{key}={identifier} ({count} occurrences)")

    unique(activities, "activity_id", "duplicate_activity_id")
    unique(contributions, "contribution_id", "duplicate_contribution_id")
    verifications = [c["verification"] for c in contributions if isinstance(c.get("verification"), dict)]
    unique(verifications, "verification_id", "duplicate_verification_id")

    activity_by_id = {a.get("activity_id"): a for a in activities}
    contribution_by_id = {c.get("contribution_id"): c for c in contributions}
    question_id = question.get("question_id")

    def chronological(first: Any, second: Any, where: str) -> None:
        t1, t2 = stamp(first), stamp(second)
        if t1 and t2 and t1 > t2:
            err("timestamp_order_mismatch", where)

    for a in activities:
        aid = str(a.get("activity_id"))
        when = a.get("occurred_at")
        if a.get("question_id") != question_id:
            err("question_reference_mismatch", f"activities[{aid}]")
        check_consent("activity_recording", when, "activity_consent_missing", f"activities[{aid}]")
        chronological(question.get("registered_at"), when, f"activities[{aid}]")
        chronological(when, doc.get("updated_at"), f"activities[{aid}] -> updated_at")

    for c in contributions:
        cid = str(c.get("contribution_id"))
        proposed = c.get("proposed_at")
        if c.get("question_id") != question_id:
            err("question_reference_mismatch", f"contributions[{cid}]")
        check_consent("contribution_evaluation", proposed, "contribution_consent_missing", f"contributions[{cid}]")
        chronological(question.get("registered_at"), proposed, f"contributions[{cid}]")
        chronological(proposed, doc.get("updated_at"), f"contributions[{cid}] -> updated_at")
        declared_targets: set[str] = set()
        for aid in strings(c.get("activity_ids")):
            activity = activity_by_id.get(aid)
            if activity is None:
                err("unknown_activity_reference", f"contributions[{cid}] -> {aid}")
            else:
                chronological(activity.get("occurred_at"), proposed, f"activities[{aid}] -> contributions[{cid}]")
                declared_targets.update(strings(activity.get("output_refs")))
        if c.get("target_ref") not in declared_targets:
            err("contribution_target_mismatch", f"contributions[{cid}]: target_ref={c.get('target_ref')}")

        verification = c.get("verification")
        if c.get("status") == "verified" and not isinstance(verification, dict):
            err("missing_verification", f"contributions[{cid}]")
        if not isinstance(verification, dict):
            continue
        if c.get("status") == "candidate":
            err("unexpected_verification", f"contributions[{cid}]")
        if verification.get("verifier_id") in {c.get("beneficiary_id"), participant.get("participant_id")}:
            err("verifier_beneficiary_conflict", f"contributions[{cid}]")
        if verification.get("verifier_id") == c.get("proposed_by"):
            err("verifier_proposer_conflict", f"contributions[{cid}]")
        claimed = set(strings(c.get("evidence_refs")))
        reviewed = set(strings(verification.get("evidence_refs")))
        if not claimed.issubset(reviewed):
            err("verification_evidence_mismatch", f"contributions[{cid}]: missing {sorted(claimed - reviewed)}")
        verified = verification.get("verified_at")
        t_proposed, t_verified = stamp(proposed), stamp(verified)
        if t_proposed and t_verified and t_verified < t_proposed:
            err("verification_before_proposal", f"contributions[{cid}]")
            err("timestamp_order_mismatch", f"contributions[{cid}]: verification before proposal")
        chronological(verified, doc.get("updated_at"), f"verification[{cid}] -> updated_at")
        if is_withdrawn and withdrawn and t_verified and t_verified >= withdrawn:
            err("verification_after_withdrawal", f"contributions[{cid}]")
        if consent_time and t_verified and t_verified < consent_time:
            err("timestamp_order_mismatch", f"verification[{cid}] before consent")

    status = handoff.get("status", "not_requested")
    if status != "not_requested":
        ids = strings(handoff.get("contribution_ids"))
        for cid in ids:
            c = contribution_by_id.get(cid)
            if c is None:
                err("unknown_contribution_reference", f"handoff -> {cid}")
            elif c.get("status") != "verified":
                err("unverified_contribution_handoff", f"handoff -> {cid}")
        for time_key in ("prepared_at", "handed_off_at"):
            when = handoff.get(time_key)
            if when is not None:
                check_consent("external_handoff", when, "handoff_consent_missing", f"handoff.{time_key}")
        if status in {"ready", "handed_off", "completed"}:
            if scopes.get("external_handoff") is not True or not consent:
                err("handoff_consent_missing", f"handoff.status={status}")
            if is_withdrawn and withdrawn:
                if status == "ready":
                    err("handoff_after_withdrawal", f"handoff.status={status}")
                elif status in {"handed_off", "completed"}:
                    dispatched = stamp(handoff.get("handed_off_at"))
                    if dispatched is None or dispatched >= withdrawn:
                        err("handoff_after_withdrawal", f"handoff.status={status}")
            if status in {"handed_off", "completed"} and not handoff.get("receipt_ref"):
                err("handoff_without_receipt", f"handoff.status={status}")
        chronological(handoff.get("prepared_at"), handoff.get("handed_off_at"), "handoff order")
        chronological(handoff.get("handed_off_at"), doc.get("updated_at"), "handoff -> updated_at")
    return errors


def find_schema(root: Path, explicit: str | None) -> Path:
    if explicit:
        path = (root / explicit).resolve()
        if not path.is_file():
            raise ValueError(f"Schema not found: {path}")
        return path
    candidates = sorted((root / "schemas").glob("*.json"))
    matches = []
    for path in candidates:
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        props = schema.get("properties", {})
        if all(k in props for k in ("record_id", "participant", "question", "contributions")):
            matches.append(path)
    preferred = [p for p in matches if "v0.1" in p.name or "0.1" in p.name]
    matches = preferred or matches
    if len(matches) != 1:
        raise ValueError(
            f"Cannot uniquely detect the v0.1 record schema ({len(matches)} candidates). "
            "Specify --schema schemas/YOUR_FILE.schema.json"
        )
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--schema", help="Path relative to repository root (or absolute path)")
    parser.add_argument("--no-schema", action="store_true", help="Semantic checks only (debugging)")
    args = parser.parse_args()
    root = args.root.resolve()
    paths = sorted((root / "examples" / "v0.1").glob("pass/*.json"))
    paths += sorted((root / "examples" / "v0.1").glob("fail/*.json"))
    if not paths:
        print("ERROR: No examples found in examples/v0.1/{pass,fail}/", file=sys.stderr)
        return 2
    validator = None
    if not args.no_schema:
        try:
            schema_path = find_schema(root, args.schema)
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            validator_cls = validators.validator_for(schema)
            validator_cls.check_schema(schema)
            validator = validator_cls(schema, format_checker=validator_cls.FORMAT_CHECKER)
            print(f"[schema] {schema_path.relative_to(root)}")
        except Exception as exc:
            print(f"ERROR: Schema initialization failed: {exc}", file=sys.stderr)
            return 2

    matched_count = 0
    for path in paths:
        expected = path.parent.name.upper()
        relative = path.relative_to(root)
        problems: list[tuple[str, str]] = []
        schema_issues: list[str] = []
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(doc, dict):
                raise ValueError("Top-level JSON must be an object")
            if validator is not None:
                schema_issues = [
                    f"{'.'.join(map(str, e.absolute_path))}: {e.message}"
                    for e in validator.iter_errors(doc)
                ]
            problems = semantic_errors(doc)
        except (ValueError, OSError) as exc:
            schema_issues = [str(exc)]
        codes = {code for code, _ in problems}
        actual = "FAIL" if schema_issues or problems else "PASS"
        target = REASONS.get(path.stem)
        target_ok = expected != "FAIL" or target is None or target in codes
        matched = actual == expected and target_ok
        matched_count += matched
        print(
            f"[{'MATCH' if matched else 'MISMATCH'}] {relative} expected={expected} actual={actual}"
            + (f" reason={target} {'OK' if target_ok else 'MISSING'}" if target else "")
        )
        if not matched:
            for issue in schema_issues[:5]:
                print(f"  [schema] {issue}")
            for code, where in problems[:10]:
                print(f"  [semantic:{code}] {where}")
            if not schema_issues and not problems:
                print("  [info] No violations detected")
    print(f"\n=== Toikatsu v0.1: {matched_count}/{len(paths)} matched ===")
    return 0 if matched_count == len(paths) else 1


if __name__ == "__main__":
    raise SystemExit(main())
