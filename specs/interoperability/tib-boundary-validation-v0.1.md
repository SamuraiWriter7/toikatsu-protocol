# TIB Boundary Validation Specification v0.1

**Toikatsu Interoperability Boundary — 境界整合性検証仕様**

- Specification Version: `0.1.0`
- Status: Draft / Design Proposal
- Specification ID: `TIB-VAL-0.1`
- Parent Specification: `specs/interoperability/toikatsu-boundary-v0.1.md`
- Parent Protocol: Toikatsu Protocol v0.1
- Scope: Boundary Conformance and Semantic Validation
- Implementation Status: Not implemented

---

## 0. Fundamental Principle

**A valid connection must preserve boundaries.**

正当な接続は、境界を破壊してはならない。

TIB Boundary Validationは、Toikatsu Protocolと外部システムの間で行われる参照、意味変換、情報引き渡しなどの処理が、定義された境界条件を満たしているか検証するための仕様である。

本仕様は、外部システムそのものの性能や品質を評価するものではない。

検証の対象は、システム間の接続によって、以下の問題が発生していないかという点にある。

1. 参照情報が不正な操作権限として使用されていないか。
2. 意味変換によって元の記録状態が改変されていないか。
3. 情報の受け渡しによって権限が不当に拡張されていないか。
4. 貢献の検証結果が報酬や決済の承認に変換されていないか。
5. 同意撤回後に禁止された新しい処理が行われていないか。
6. 接続失敗が成功として扱われていないか。

TIBでは、単に処理が完了することよりも、境界条件を守った状態で処理されることを重視する。

---

## 1. Purpose

本仕様の目的は、TIB v0.1の設計原則を、再現可能な検証条件へ変換することである。

具体的には以下を定義する。

- 境界検証の対象
- 正常な接続の成立条件
- 不正な接続の拒否条件
- PASS／FAILの判定基準
- 検証できない状態の扱い
- テストケースの識別方法
- 将来の自動検証に必要な基本条件

本仕様は、JSON Schemaや実行プログラムそのものではない。

将来の境界検証実装に対する設計基準として使用する。

---

## 2. Normative Language

本仕様では以下の規範用語を使用する。

- MUST：必須
- MUST NOT：禁止
- SHOULD：推奨
- SHOULD NOT：非推奨
- MAY：任意

本仕様はTIBへの適合を主張する実装に対する要件を定義する。

既存のToikatsu v0.1の記録形式や、公開済みv0.1.0の適合条件を遡及的に変更するものではない。

---

## 3. Validation Model

### 3.1 Boundary Validation Layers

TIBでは、次の検証層を区別する。

| Layer | Responsibility |
|---|---|
| Structural Validation | 入出力データの構造 |
| Reference Validation | 外部参照の整合性 |
| Semantic Validation | 意味と状態の保存 |
| Authority Validation | 操作権限の分離 |
| Consent Validation | 同意範囲と撤回状態 |
| Value Validation | 貢献検証と価値判断の分離 |
| Failure Validation | 失敗時の整合性維持 |

Structural Validationは、将来のJSON Schemaで検証可能な部分を扱う。

それ以外の層には、複数の記録や処理履歴を比較する意味検証が必要となる。

### 3.2 Validation Outcomes

境界検証の評価結果は以下の3種類とする。

| Outcome | Meaning |
|---|---|
| `PASS` | 必要な条件を確認できた |
| `FAIL` | 明示的な境界違反を確認した |
| `UNRESOLVED` | 証拠不足などにより判断できない |

`UNRESOLVED`は、`PASS`と同等に扱ってはならない（MUST NOT）。

安全性や権限の確認ができない処理については、`UNRESOLVED`のまま実行を許可してはならない（MUST NOT）。

自動テストでは、`UNRESOLVED`を期待する専用事例を除き、`UNRESOLVED`を適合成功として扱わない。

### 3.3 Test Expectations

各テストケースは、期待結果を明示する。

- 正常接続：Expected `PASS`
- 境界違反：Expected `FAIL`
- 判定不能：Expected `UNRESOLVED`

テストランナーは、実際の結果と期待結果を比較する。

期待結果との一致を、テストの成功とする。

ただし、Expected `FAIL`の事例がテストとして成功した場合でも、その接続自体は不正である。

---

## 4. Reference Boundary Validation

### 4.1 Objective

参照情報の利用が、元記録の改変や不正な権限取得につながらないことを確認する。

### 4.2 Rules

**TIB-REF-001: Reference Integrity**

外部へ渡す参照情報は、元の識別子と対応関係を保持しなければならない（MUST）。

**TIB-REF-002: Reference Is Not Authority**

参照情報の取得によって、元記録の編集権限や管理権限を取得してはならない（MUST NOT）。

**TIB-REF-003: Reference Resolution**

参照先が取得できない場合、取得済みとして扱ってはならない（MUST NOT）。

**TIB-REF-004: Reference Authenticity**

参照先の存在のみを根拠として、内容の真正性を認定してはならない（MUST NOT）。

**TIB-REF-005: External Data Isolation**

外部参照から取得したデータを、実行命令として無条件に処理してはならない（MUST NOT）。

### 4.3 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| REF-P01 | 正しい識別子を読み取り専用で参照 | PASS |
| REF-P02 | 参照先が取得不能であることを正しく報告 | PASS |
| REF-F01 | 参照情報から編集権限を取得 | FAIL |
| REF-F02 | 存在しない参照先を取得済みと報告 | FAIL |
| REF-F03 | 外部参照データを無条件に命令として実行 | FAIL |
| REF-U01 | 参照内容の真正性を確認できない | UNRESOLVED |

---

## 5. Semantic Boundary Validation

### 5.1 Objective

異なるプロトコル間で情報を変換しても、元の意味と状態が不当に変更されないことを確認する。

### 5.2 Semantic Preservation Rules

**TIB-SEM-001: Status Preservation**

元記録の状態を、意味変換だけで上位状態へ昇格させてはならない（MUST NOT）。

**TIB-SEM-002: Candidate Preservation**

`candidate`を`verified`として出力してはならない（MUST NOT）。

**TIB-SEM-003: Rejection Preservation**

`rejected`を`verified`として出力してはならない（MUST NOT）。

**TIB-SEM-004: Verification Separation**

`verified`を支払承認や価値決定済みとして変換してはならない（MUST NOT）。

**TIB-SEM-005: Unknown Meaning**

変換先に対応する概念が存在しない場合、意味を推測して補完してはならない（MUST NOT）。

**TIB-SEM-006: Transformation Trace**

意味変換では、元記録と変換結果を追跡可能にしなければならない（MUST）。

### 5.3 Semantic Mapping Outcomes

意味変換の結果には、以下の内部判定を使用できる。

| Mapping Outcome | Meaning |
|---|---|
| `mapped` | 意味を保持して変換できた |
| `unresolved` | 対応する意味を確定できない |
| `rejected` | 不正または禁止された変換 |

これらは意味変換の結果であり、境界検証全体の`PASS`／`FAIL`／`UNRESOLVED`とは区別する。

例えば、変換結果が`unresolved`でも、それを正しく報告し、危険な操作を実行しなかった場合、境界処理自体のテストはPASSとなり得る。

### 5.4 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| SEM-P01 | `candidate`を同じ意味で変換 | PASS |
| SEM-P02 | `verified`の意味を保持 | PASS |
| SEM-P03 | 対応不能な意味を`unresolved`として処理 | PASS |
| SEM-F01 | `candidate`を`verified`へ昇格 | FAIL |
| SEM-F02 | `rejected`を`verified`へ変更 | FAIL |
| SEM-F03 | `verified`を支払承認として変換 | FAIL |
| SEM-F04 | 元記録との対応関係を失う | FAIL |
| SEM-U01 | 必要な元記録が取得できず比較不能 | UNRESOLVED |

---

## 6. Authority Boundary Validation

### 6.1 Objective

情報の接続と操作権限の委譲を明確に分離する。

### 6.2 Rules

**TIB-AUTH-001: No Implicit Authority**

情報を受け取っただけで、元システムの操作権限を取得してはならない（MUST NOT）。

**TIB-AUTH-002: Explicit Authorization**

外部操作には、情報交換とは独立した操作認可が必要である（MUST）。

**TIB-AUTH-003: Scope Limitation**

認可された範囲を超える操作を実行してはならない（MUST NOT）。

**TIB-AUTH-004: No Implicit Delegation**

明示的な許可なしに、権限を第三者へ再委譲してはならない（MUST NOT）。

**TIB-AUTH-005: Verification Is Not Authority**

貢献検証の成立を、外部操作権限の根拠として使用してはならない（MUST NOT）。

### 6.3 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| AUTH-P01 | 読み取り権限のみで参照 | PASS |
| AUTH-P02 | 独立した操作認可を確認 | PASS |
| AUTH-F01 | 参照権限で元記録を変更 | FAIL |
| AUTH-F02 | Handoff情報を管理者権限として利用 | FAIL |
| AUTH-F03 | 許可範囲外の操作を実行 | FAIL |
| AUTH-F04 | 明示的な許可なく権限を再委譲 | FAIL |
| AUTH-F05 | `verified`を操作承認として使用 | FAIL |
| AUTH-U01 | 操作主体の権限を確認できない | UNRESOLVED |

---

## 7. Consent Boundary Validation

### 7.1 Objective

プロトコル間の接続によって、元の同意条件が失われたり、不当に拡張されたりしないことを確認する。

### 7.2 Rules

**TIB-CON-001: Scope Preservation**

情報交換では、元の同意範囲を維持しなければならない（MUST）。

**TIB-CON-002: External Handoff Consent**

外部引き渡しには、有効な`external_handoff`同意が必要である（MUST）。

**TIB-CON-003: Public Sharing Consent**

公開には、必要な`public_sharing`同意が存在しなければならない（MUST）。

**TIB-CON-004: Withdrawal Enforcement**

同意撤回後に、その同意に基づく新たな引き渡しを行ってはならない（MUST NOT）。

**TIB-CON-005: Historical Operation Preservation**

撤回前に完了した正当な処理を、撤回後に行われた不正な処理と同一視してはならない（MUST NOT）。

**TIB-CON-006: No Scope Expansion**

意味変換によって同意範囲を拡張してはならない（MUST NOT）。

### 7.3 Temporal Boundary

撤回前の処理と撤回後の処理を、日時に基づいて区別する。

```text
Consent Active
      |
      v
Authorized Handoff
      |
      v
Receipt Confirmed
      |
      v
Consent Withdrawn
      |
      v
No New Handoff
```

過去の履歴を保持できることは、今後の利用を無条件に許可するものではない。

同意撤回後の外部利用は、適用される同意方針と法令に従って判断する。

### 7.4 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| CON-P01 | 有効な同意範囲内の引き渡し | PASS |
| CON-P02 | 撤回前の正常な引き渡し履歴を保持 | PASS |
| CON-P03 | 撤回後の新規引き渡しを拒否 | PASS |
| CON-F01 | 同意なしで外部引き渡し | FAIL |
| CON-F02 | 撤回後に新しい引き渡しを実行 | FAIL |
| CON-F03 | 公開同意なしで記録を公開 | FAIL |
| CON-F04 | 意味変換で同意範囲を拡張 | FAIL |
| CON-U01 | 必要な同意状態が確認不能 | UNRESOLVED |

---

## 8. Value Boundary Validation

### 8.1 Objective

貢献の検証と価値評価、決済、還元を独立した処理として維持する。

### 8.2 Rules

**TIB-VAL-001: Verification Is Not Payment**

`verified`を支払完了として扱ってはならない（MUST NOT）。

**TIB-VAL-002: Handoff Is Not Settlement**

`handed_off`を決済完了として扱ってはならない（MUST NOT）。

**TIB-VAL-003: Independent Value Decision**

報酬や価値の決定には、後続システム側の独立した判断が必要である（MUST）。

**TIB-VAL-004: No Automatic Entitlement**

貢献の検証結果だけで報酬資格や報酬額を確定してはならない（MUST NOT）。

**TIB-VAL-005: Origin Preservation**

価値判断に利用した元記録を追跡可能にすべきである（SHOULD）。

### 8.3 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| VAL-P01 | 検証済み貢献を評価候補として引き渡し | PASS |
| VAL-P02 | 後続システムで独立して価値判断 | PASS |
| VAL-F01 | `verified`を支払完了と解釈 | FAIL |
| VAL-F02 | Handoff Receiptを決済証明に変換 | FAIL |
| VAL-F03 | 独立した価値判断なしで報酬額を確定 | FAIL |
| VAL-F04 | 貢献検証を送金承認として利用 | FAIL |
| VAL-U01 | 後続システムの価値判断記録が不明 | UNRESOLVED |

---

## 9. Failure Isolation Validation

### 9.1 Objective

外部接続の失敗によって、元システムの記録、権限、処理状態が不当に変更されないことを確認する。

### 9.2 Rules

**TIB-FAIL-001: Source Preservation**

接続失敗によって元記録を不当に変更してはならない（MUST NOT）。

**TIB-FAIL-002: No False Success**

失敗した処理を成功として記録してはならない（MUST NOT）。

**TIB-FAIL-003: Authorization Failure**

権限が確認できない操作を実行してはならない（MUST NOT）。

**TIB-FAIL-004: Retry Safety**

再実行の安全性が確認できない処理を、自動で再実行してはならない（MUST NOT）。

**TIB-FAIL-005: Failure Containment**

外部接続の失敗が他の接続や元システム全体へ波及しないようにすべきである（SHOULD）。

### 9.3 Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| FAIL-P01 | 外部接続失敗後も元記録を保持 | PASS |
| FAIL-P02 | 受領確認不能を未完了として保持 | PASS |
| FAIL-P03 | 安全性不明の再試行を停止 | PASS |
| FAIL-F01 | 接続失敗後に元記録を破壊 | FAIL |
| FAIL-F02 | 失敗したHandoffを成功として記録 | FAIL |
| FAIL-F03 | 権限確認不能のまま実行 | FAIL |
| FAIL-F04 | 安全性未確認の処理を自動再実行 | FAIL |
| FAIL-U01 | 外部処理が完了したか確認不能 | UNRESOLVED |

---

## 10. Cross-Boundary Validation

個別の境界が正常でも、複数の境界をまたぐ処理で違反が発生する場合がある。

TIBでは、境界間の組み合わせを検証対象に含める。

### 10.1 Reference × Authority

参照できる情報を、操作権限として使用していないか確認する。

### 10.2 Semantic × Value

意味変換によって、貢献候補が報酬確定状態へ変化していないか確認する。

### 10.3 Consent × Handoff

同意撤回後に、過去の引き渡し履歴を利用して新しい引き渡しを行っていないか確認する。

### 10.4 Authority × Failure

接続失敗後の再試行で、元の認可範囲を超えていないか確認する。

### 10.5 Cross-Boundary Test Cases

| Test ID | Scenario | Expected |
|---|---|---|
| CROSS-P01 | 参照・意味・同意・権限を保持した接続 | PASS |
| CROSS-P02 | 接続失敗時に権限と元記録を維持 | PASS |
| CROSS-F01 | 意味変換を利用した権限昇格 | FAIL |
| CROSS-F02 | 検証結果を利用した無許可決済 | FAIL |
| CROSS-F03 | 同意撤回後の再送による新規引き渡し | FAIL |
| CROSS-F04 | 外部参照を利用した元記録の改変 | FAIL |
| CROSS-U01 | 複数境界の判断に必要な情報が不足 | UNRESOLVED |

---

## 11. Boundary Validation Record

### 11.1 Purpose

検証結果を再現可能にするため、将来の実装では境界検証記録を作成することを推奨する。

### 11.2 Conceptual Fields

| Field | Description |
|---|---|
| `boundary_validation_id` | 境界検証の識別子 |
| `test_case_id` | テストケースID |
| `source_protocol` | 元プロトコル |
| `source_record_id` | 元記録ID |
| `destination_protocol` | 接続先 |
| `boundary_types` | 検証対象の境界 |
| `expected_result` | 期待結果 |
| `actual_result` | 実際の結果 |
| `violation_codes` | 検出された違反 |
| `evidence_refs` | 判定に使用した証拠 |
| `validated_at` | 検証日時 |
| `validator_ref` | 検証主体または検証実装 |

これらは概念フィールドであり、v0.1ではJSON Schemaを定義しない。

### 11.3 Traceability

検証結果は、元記録、接続操作、適用した規則と関連付けられるべきである（SHOULD）。

検証者や検証方法が不明な結果を、独立した検証済み結果として表示してはならない（MUST NOT）。

---

## 12. Violation Codes

将来の自動検証で使用する違反コード候補を定義する。

| Violation Code | Meaning |
|---|---|
| `reference_authority_violation` | 参照情報による権限取得 |
| `reference_resolution_mismatch` | 参照取得状態の不一致 |
| `semantic_state_escalation` | 不正な状態昇格 |
| `semantic_mapping_mismatch` | 意味変換の不整合 |
| `transformation_trace_missing` | 変換来歴の欠落 |
| `unauthorized_operation` | 許可されていない操作 |
| `authority_scope_exceeded` | 権限範囲の超過 |
| `unauthorized_delegation` | 無許可の権限再委譲 |
| `consent_scope_violation` | 同意範囲違反 |
| `handoff_after_withdrawal` | 撤回後の新規引き渡し |
| `verification_as_payment` | 検証と支払完了の混同 |
| `handoff_as_settlement` | 引き渡しと決済完了の混同 |
| `value_decision_missing` | 独立した価値判断の欠落 |
| `source_record_modified` | 元記録の不正変更 |
| `false_success_reported` | 失敗処理の成功報告 |
| `unsafe_retry` | 安全性未確認の再試行 |

本一覧は初期案であり、コードの最終的な命名や網羅性は将来のSchema・Validator開発時に確定する。

---

## 13. Test Design Requirements

### 13.1 Positive Tests

正常例は、許可された情報交換が成立することを確認する。

ただし、正常な情報交換が成立したことを理由に、別の境界検証を省略してはならない。

### 13.2 Negative Tests

不正例では、少なくとも一つの明示的な境界違反を検出できなければならない（MUST）。

対象の違反理由が定義されている場合は、その理由でFAILとなることを確認する。

意図しない別のエラーによる失敗を、当該境界検証の成功とみなしてはならない（MUST NOT）。

### 13.3 Unresolved Tests

判定不能事例では、証拠不足を明示できることを確認する。

`UNRESOLVED`を`PASS`や`FAIL`へ自動変換してはならない（MUST NOT）。

### 13.4 Test Isolation

個別のテストケースでは、原則として対象の違反条件を一つに限定することを推奨する（SHOULD）。

複数境界の相互作用は、Cross-Boundary Testで別途検証する。

### 13.5 Evidence Requirements

検証で利用する証拠は、対象とする境界条件の成立または違反を判断できる内容でなければならない（MUST）。

証拠の存在だけをもって、その内容の真正性を保証してはならない（MUST NOT）。

---

## 14. Expected Validator Behavior

将来のValidatorは、以下の動作を満たすことを目標とする。

1. 入力の構造を確認する。
2. 適用可能な境界規則を特定する。
3. 必要な参照・状態・同意・権限情報を確認する。
4. 明示的な境界違反を検出する。
5. 判定不能な条件を区別する。
6. PASS／FAIL／UNRESOLVEDを出力する。
7. 期待結果との一致を確認する。
8. 検証結果と違反理由を記録する。

判定不能な操作を、自動的に許可してはならない（MUST NOT）。

### 14.1 Fail-Closed Behavior

操作の認可、同意、価値移転に関係する重要な条件を確認できない場合、実行を停止または保留することを基本とする。

この原則をFail-Closedと呼ぶ。

ただし、判定不能な情報を削除したり、元記録を不正な状態へ変更したりすることは認めない。

---

## 15. Relationship to Toikatsu v0.1 Validation

Toikatsu v0.1の既存Validatorは、主に単一のToikatsu Recordについて検証する。

対象には以下が含まれる。

- JSON Schema
- 識別子の一意性
- 参照の整合性
- 同意状態
- 時系列
- 貢献と証拠の関係
- Handoffの成立条件

TIB Boundary Validationは、これらを置き換えない。

既存のToikatsu Recordが妥当であることと、その記録を外部システムへ安全に接続できることは別の問題である。

### 15.1 Validation Separation

```text
Toikatsu Record
      |
      v
Toikatsu Validation
      |
      v
Record-Level Validity
      |
      v
TIB Boundary Validation
      |
      v
Boundary-Level Validity
      |
      v
Independent Authorization
      |
      v
Permitted External Operation
```

この構造は、各検証の責任範囲を示す概念図である。

境界検証にPASSしたことだけで、実行権限が自動的に与えられるものではない。

### 15.2 Existing Validator Compatibility

TIBの導入によって、既存のToikatsu v0.1のJSON Schemaや状態定義を変更しない。

Toikatsu側の規範仕様とValidatorの間に不整合が見つかった場合、その修正は別途管理する。

TIBの適合性を主張する前に、接続元の検証条件が明確であることを確認すべきである（SHOULD）。

---

## 16. Non-Goals

本仕様は以下を対象としない。

- 外部システムの動作保証
- 暗号認証方式の新規定義
- 決済プロトコルの実装
- ロイヤルティ計算
- 報酬資格の法的確定
- あらゆる意味変換の正しさの完全証明
- AIモデル内部の推論過程の監査
- ネットワーク全体の不正行為の完全防止
- 外部プロトコルへの仕様変更の強制

境界を定義することは、外部システムの内部を支配することではない。

---

## 17. Implementation Roadmap

本仕様は段階的な検証基盤の整備を想定する。

### Phase 1 — Specification

- 境界規則の定義
- テストケースの定義
- PASS／FAIL／UNRESOLVEDの整理
- 違反コード候補の定義

**Current Stage: Draft specification**

### Phase 2 — Test Fixtures

- Reference Boundaryの正常・異常例
- Semantic Boundaryの正常・異常例
- Authority Boundaryの正常・異常例
- Consent Boundaryの正常・異常例
- Value Boundaryの正常・異常例
- Failure Isolationの正常・異常例
- Cross-Boundaryの複合事例

### Phase 3 — Automated Validator

- 境界検証用Schema
- 意味検証ルール
- テスト期待値の照合
- 違反理由の出力

### Phase 4 — Continuous Validation

- GitHub Actionsとの接続
- 自動テストの再現性確認
- 仕様とテスト事例の整合性確認
- 将来の外部接続実験への利用

これらは構想上の段階であり、現時点で実装が完了したことを意味しない。

---

## 18. Completion Criteria

TIB Boundary Validation v0.1の設計段階の完了条件は以下とする。

1. 主要な境界規則が文書化されている。
2. 各境界の正常例と違反例が定義されている。
3. PASS／FAIL／UNRESOLVEDが区別されている。
4. 重要な違反に識別可能なコードが割り当てられている。
5. 同意、意味、権限、価値の境界が混同されていない。
6. 既存Toikatsu v0.1の仕様を変更していない。
7. 検証可能な条件と、実運用上の確認が必要な条件を区別している。

これらの成立は、設計文書としての整理が完了したことを意味する。

自動検証の実装完了や、実運用上の安全性の証明を意味するものではない。

---

## 19. Design Summary

TIB Boundary Validationは、異なるシステム間で情報が交換されるとき、何を守るべきかを検証可能な条件として定義する。

**Reference Boundary**

参照情報を操作権限へ変換しない。

**Semantic Boundary**

意味変換によって元の状態を改変しない。

**Authority Boundary**

情報の取得を権限の取得と混同しない。

**Consent Boundary**

外部接続によって人間の同意条件を失わない。

**Value Boundary**

貢献検証を報酬や決済の確定と混同しない。

**Failure Isolation**

接続の失敗を元システム全体へ波及させない。

---

## 20. Closing Declaration

AI時代のシステムは、接続が増えるほど複雑になる。

一つのシステムでは正しい情報でも、別のシステムへ渡されたとき、その意味が変わることがある。

参照情報が権限として扱われることがある。

検証結果が、支払いの承認として誤解されることもある。

だからこそ、単に接続できることだけでは不十分である。

必要なのは、接続する際に守るべき境界を明確にし、その境界が維持されているか確認できる構造である。

**Connect without controlling.**

**Transform without distorting.**

**Verify without granting authority.**

**Preserve consent across boundaries.**

**Never confuse contribution with entitlement.**

TIB Boundary Validation v0.1

*接続の自由と、境界の信頼性を両立させる。*
