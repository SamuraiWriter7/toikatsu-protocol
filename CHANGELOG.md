# Changelog

All notable changes to the Toikatsu Protocol are documented in this file.

This project follows the principles of
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and uses version identifiers inspired by
[Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### Planned

- Multi-participant contribution records
- Multiple independent verifiers
- Verification appeals and reassessment
- More detailed state transition histories
- Cross-record identity and reference validation
- Integration with external provenance systems
- Duplicate handoff prevention
- Privacy-preserving contribution evidence
- Interoperability with Q Network and Trace protocols
- Connections to downstream value circulation systems

These items are proposals for future development.
They are not implemented in v0.1.0.

---

## [0.1.0] - 2026-11-03

### Initial Specification Release

The first validation-backed draft of Toikatsu Protocol.

Toikatsu Protocol defines a human-centered record structure
for connecting questions, activities, contribution claims,
verification results, and downstream handoffs.

The protocol separates question registration,
contribution verification, and value redistribution.

### Added

#### Core Specification

- Added `specs/toikatsu-v0.1.md`.
- Defined the purpose, scope, and normative requirements
  of Toikatsu Protocol v0.1.
- Defined human-centered question submission.
- Supported human submissions with AI assistance.
- Defined consent-bounded recording and evaluation.
- Defined contribution evidence and independent verification.
- Defined handoff to external value circulation systems.
- Established explicit boundaries between verification,
  handoff, settlement, and redistribution.

#### JSON Schema

- Added `schemas/toikatsu-v0.1.schema.json`.
- Defined the Toikatsu Record structure.
- Added validation constraints for required fields,
  data types, enumerations, and record states.
- Defined participant and question records.
- Defined consent status and permission scopes.
- Defined activities and contribution candidates.
- Defined verification records.
- Defined handoff states and receipt requirements.

#### Question and Activity Records

- Added unique question and activity identifiers.
- Added question registration timestamps.
- Added submission modes:
  - `human`
  - `human_with_ai_assistance`
- Added activity types:
  - `exploration`
  - `derived_question`
  - `improvement`
  - `evaluation`
- Added output references for activity traces.

#### Consent and Withdrawal

- Added four consent scopes:
  - `activity_recording`
  - `contribution_evaluation`
  - `external_handoff`
  - `public_sharing`
- Added `active` and `withdrawn` consent states.
- Added consent timestamps and withdrawal timestamps.
- Added semantic checks for operations outside consent scope.
- Added checks for activities, contributions,
  verification, and handoff after withdrawal.
- Preserved the distinction between historical operations
  and new operations after withdrawal.

#### Contribution Verification

- Added contribution states:
  - `candidate`
  - `verified`
  - `rejected`
- Added contribution claims, target references,
  evidence references, and activity references.
- Added verification identifiers and verifier identities.
- Added verification timestamps, methods, and reasons.
- Added independent-verification checks.
- Added evidence consistency checks.
- Added contribution target consistency checks.
- Added duplicate identifier detection.
- Supported verification records for rejected claims.

#### Handoff

- Added handoff states:
  - `not_requested`
  - `ready`
  - `handed_off`
  - `cancelled`
- Added contribution references and destination references.
- Added preparation and receipt timestamps.
- Added receipt requirements for completed handoffs.
- Allowed `ready` records without a receipt.
- Added restrictions against handing off unverified
  or rejected contributions.
- Added consent-based handoff validation.
- Allowed historical handoffs completed before
  consent withdrawal to remain recorded.

#### Example Records

- Added positive examples covering:
  - Question registration
  - Question activity recording
  - Contribution candidates
  - Verified contributions
  - Rejected contributions
  - Handoff preparation
  - Completed handoff
  - Cancellation after withdrawal
  - Historical handoff followed by withdrawal

- Added negative examples covering:
  - Missing activity references
  - Contribution target mismatch
  - Missing consent
  - Operations after withdrawal
  - Unverified contribution handoff
  - Rejected contribution handoff
  - Self-verification
  - Verifier-beneficiary conflicts
  - Duplicate activity identifiers
  - Duplicate contribution identifiers
  - Duplicate verification identifiers
  - Verification evidence mismatch
  - Verification before contribution proposal
  - Timestamp ordering violations
  - Missing handoff receipts
  - Missing verification records

#### Validation Script

- Added `scripts/validate_examples.py`.
- Added JSON Schema validation.
- Added semantic validation.
- Added PASS/FAIL expectation matching.
- Added targeted semantic failure checks.
- Added identifier uniqueness validation.
- Added reference integrity validation.
- Added timestamp ordering checks.
- Added consent and withdrawal checks.
- Added verification evidence validation.
- Added handoff state validation.
- Added nonzero exit status for validation failures.

#### GitHub Actions

- Added `.github/workflows/validate.yml`.
- Configured automated validation for relevant pushes.
- Configured Pull Request validation.
- Added manual workflow execution.
- Added Python syntax validation.
- Added JSON syntax validation.
- Added JSON Schema and semantic validation.
- Added PASS/FAIL expectation checks.
- Added GitHub Actions validation summaries.

#### Documentation

- Expanded `README.md`.
- Documented the protocol's purpose and design principles.
- Documented the record structure and supported states.
- Documented consent and withdrawal rules.
- Documented verification and handoff boundaries.
- Documented local validation commands.
- Documented relationships with Q Network,
  Trace, and Royalty OS.
- Documented limitations and future development areas.

### Fixed

- Corrected semantic validation of rejected contributions
  that contain valid verification records.
- Corrected receipt requirements for handoff records
  in the `ready` state.
- Corrected handling of historical handoffs completed
  before consent withdrawal.
- Added detection of contribution targets not referenced
  by their declared activities.
- Removed deprecated `jsonschema.RefResolver` usage.
- Enabled JSON Schema format checking.

### Validation

GitHub Actions validation passed after correcting
four expectation mismatches identified during testing.

The previous failing run reported:

```text
=== Toikatsu v0.1: 27/31 matched ===
```

After updating the semantic validator, the GitHub Actions
workflow completed successfully.

The validation suite checks positive and negative examples,
including intended semantic violations.

A successful validation run confirms consistency with
the implemented checks and included examples.

It does not prove:

- Real-world authenticity of evidence
- Actual consent collection
- Causal contribution to external outcomes
- Legal ownership or entitlement
- Financial settlement
- Royalty redistribution
- Production readiness

### Known Limitations

- The protocol remains a draft specification.
- A single record cannot prove historical state transitions.
- Cross-record identity verification is not implemented.
- Real-world evidence authenticity requires external checks.
- Actual verifier independence requires operational controls.
- External handoff receipts are represented by references,
  not independently authenticated.
- Settlement and redistribution are outside the protocol.
- Full compliance with every normative specification
  requirement is not established solely by the current tests.

### Design Note

Toikatsu Protocol v0.1 establishes a structured entry point
for recording and evaluating human contributions
originating from questions.

The protocol follows three fundamental distinctions:

1. Question registration is not contribution verification.
2. Contribution verification is not payment authorization.
3. Handoff completion is not value redistribution.

These distinctions preserve the separation between
participation, evidence, verification, and economic outcomes.

---

## Versioning Policy

- **v0.1.x** — Corrections and stabilization of the initial draft
- **v0.2.x** — Future backward-incompatible or expanded draft features, as specified at release time
- **v1.0.0** — A future stable specification release, subject to explicit review

Version numbers describe the evolution of the specification
and do not independently certify production readiness.

---

## Closing Principle

**Questions create possibilities.  
Evidence supports contributions.  
Verification builds trust.  
Value circulation requires accountability.**

Toikatsu Protocol is designed to connect human questions
to verifiable contributions without automatically equating
participation with economic entitlement.
