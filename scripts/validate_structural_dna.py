#!/usr/bin/env python3
"""Validate Structural DNA v0.1 operator registry and optional fixtures.

Install:
    python -m pip install "jsonschema>=4.18,<5"

Run:
    python scripts/validate_structural_dna.py
    python scripts/validate_structural_dna.py --no-schema  # diagnostics only

Optional fixtures (complete registry documents):
    examples/structural-dna/v0.1/pass/*.json
    examples/structural-dna/v0.1/fail/*.json

The registry validator does not determine whether an AI's interpretation of a
question is semantically correct. UNRESOLVED applies to future classification
records, not to the syntax of this fixed operator dictionary.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('ERROR: install jsonschema: python -m pip install "jsonschema>=4.18,<5"')

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = Path("schemas/structural-dna/structural-operator-registry-v0.1.schema.json")
DEFAULT_REGISTRY = Path("registries/structural-dna/structural-operators-v0.1.json")
DEFAULT_EXAMPLES = Path("examples/structural-dna/v0.1")

EXPECTED_OPERATORS = {
    "OP-001": "detect_limit",
    "OP-002": "distribute",
    "OP-003": "centralize",
    "OP-004": "connect",
    "OP-005": "separate",
    "OP-006": "circulate",
    "OP-007": "regulate",
    "OP-008": "reverse",
    "OP-009": "simplify",
    "OP-010": "combine",
    "OP-011": "stabilize",
    "OP-012": "preserve",
}

RELATIONS = {
    "contrasts_with",
    "complements",
    "may_precede",
    "may_follow",
    "overlaps_with",
}


def load_json(path: Path) -> Any:
    """Load UTF-8 JSON, rejecting duplicate object keys."""
    def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON object key: {key}")
            result[key] = value
        return result

    with path.open(encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=reject_duplicate_keys)


def semantic_errors(doc: Any) -> list[tuple[str, str]]:
    """Validate registry relationships and identifiers beyond JSON Schema."""
    problems: list[tuple[str, str]] = []

    def fail(code: str, location: str) -> None:
        problems.append((code, location))

    if not isinstance(doc, dict):
        return [("invalid_registry", "root")]

    operators = doc.get("operators")
    if not isinstance(operators, dict):
        return [("invalid_operators", "operators")]

    keys = set(operators)
    expected = set(EXPECTED_OPERATORS)
    for identifier in sorted(expected - keys):
        fail("missing_operator", f"operators.{identifier}")
    for identifier in sorted(keys - expected):
        fail("unknown_operator", f"operators.{identifier}")

    names: dict[str, str] = {}
    for identifier, definition in sorted(operators.items()):
        location = f"operators.{identifier}"
        if not isinstance(definition, dict):
            fail("invalid_operator_definition", location)
            continue

        if definition.get("operator_id") != identifier:
            fail("operator_id_mismatch", f"{location}.operator_id")

        name = definition.get("name")
        if identifier in EXPECTED_OPERATORS and name != EXPECTED_OPERATORS[identifier]:
            fail("operator_name_mismatch", f"{location}.name")
        if isinstance(name, str):
            if name in names:
                fail("duplicate_operator_name", f"{location}.name (also {names[name]})")
            names[name] = identifier

        relationships = definition.get("relationships", [])
        if not isinstance(relationships, list):
            fail("invalid_relationships", f"{location}.relationships")
            continue

        seen: set[tuple[str, str]] = set()
        for index, rel in enumerate(relationships):
            ref_location = f"{location}.relationships[{index}]"
            if not isinstance(rel, dict):
                fail("invalid_relationship", ref_location)
                continue
            target = rel.get("target_operator_id")
            kind = rel.get("relation")
            if not isinstance(target, str) or target not in keys:
                fail("unknown_relationship_target", f"{ref_location}.target_operator_id")
            if target == identifier:
                fail("self_relationship", ref_location)
            if kind not in RELATIONS:
                fail("unknown_relationship_type", f"{ref_location}.relation")
            if isinstance(target, str) and isinstance(kind, str):
                pair = (target, kind)
                if pair in seen:
                    fail("duplicate_relationship", ref_location)
                seen.add(pair)

    return problems


def check_document(
    doc: Any, validator: Draft202012Validator | None
) -> tuple[list[str], list[tuple[str, str]]]:
    schema_problems: list[str] = []
    if validator is not None:
        issues = sorted(
            validator.iter_errors(doc),
            key=lambda e: (tuple(str(p) for p in e.absolute_path), e.message),
        )
        for issue in issues:
            location = "/".join(map(str, issue.absolute_path)) or "<root>"
            schema_problems.append(f"{location}: {issue.message}")
    return schema_problems, semantic_errors(doc)


def report(
    name: str, doc: Any, validator: Draft202012Validator | None, expected: str
) -> bool:
    schema_problems, semantic_problems = check_document(doc, validator)
    actual = "FAIL" if schema_problems or semantic_problems else "PASS"
    matched = actual == expected
    print(f"[{'MATCH' if matched else 'MISMATCH'}] {name} expected={expected} actual={actual}")
    if not matched:
        for problem in schema_problems[:8]:
            print(f"  [schema] {problem}")
        for code, location in semantic_problems[:12]:
            print(f"  [semantic:{code}] {location}")
        if actual == "PASS":
            print("  [info] No violations detected")
    return matched


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--examples-dir", type=Path, default=DEFAULT_EXAMPLES)
    parser.add_argument("--no-schema", action="store_true", help="Debug mode; incomplete validation")
    args = parser.parse_args()
    root = args.root.resolve()

    def within_root(path: Path) -> Path:
        return path if path.is_absolute() else root / path

    validator: Draft202012Validator | None = None
    if not args.no_schema:
        schema_path = within_root(args.schema)
        try:
            schema = load_json(schema_path)
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema)
        except (OSError, ValueError, TypeError) as exc:
            print(f"ERROR: Cannot initialize schema {schema_path}: {exc}", file=sys.stderr)
            return 2
        print(f"[schema] {schema_path}")
    else:
        print("[warning] --no-schema: JSON Schema validation disabled")

    registry_path = within_root(args.registry)
    try:
        doc = load_json(registry_path)
    except (OSError, ValueError) as exc:
        print(f"ERROR: Cannot load registry {registry_path}: {exc}", file=sys.stderr)
        return 2

    print("=== Structural DNA v0.1 Registry Validation ===")
    matched = int(report(str(registry_path), doc, validator, "PASS"))
    total = 1

    example_dir = within_root(args.examples_dir)
    fixtures: list[tuple[Path, str]] = []
    for expectation in ("PASS", "FAIL"):
        fixtures.extend(
            (path, expectation)
            for path in sorted((example_dir / expectation.lower()).glob("*.json"))
        )

    if not fixtures:
        print("[info] No optional PASS/FAIL registry fixtures found")

    for path, expectation in fixtures:
        total += 1
        try:
            candidate = load_json(path)
        except (OSError, ValueError) as exc:
            print(f"[MISMATCH] {path} expected={expectation} actual=ERROR")
            print(f"  [parse] {exc}")
            continue
        matched += int(report(str(path), candidate, validator, expectation))

    print(f"\n=== Structural DNA v0.1: {matched}/{total} matched ===")
    return 0 if matched == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
