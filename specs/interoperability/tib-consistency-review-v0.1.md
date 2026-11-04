# TIB Consistency Review v0.1

**Toikatsu Interoperability Boundary — 規範整合性・接続安全性レビュー**

- Review Version: `0.1.0`
- Status: Draft / Design Review
- Review Date: 2026-11-04
- Parent Protocol: Toikatsu Protocol v0.1
- Boundary Specification: TIB v0.1
- Implementation Status: Review only
- Compatibility Policy: Non-breaking

---

## 0. Fundamental Principle

**Boundary consistency must precede interoperability.**

相互運用を拡張する前に、接続境界の整合性を確保しなければならない。

TIBは、複数の独立したプロトコルが情報を交換するための境界仕様である。

しかし、接続元の仕様、意味検証、接続先の解釈が異なれば、接続そのものが成立しても、意味や権限が変化する危険がある。

本レビューでは、次の原則を採用する。

1. 仕様と実装の差異を隠さない。
2. 検証不能な状態を成功とみなさない。
3. 元記録の状態と意味を維持する。
4. 情報交換と操作認可を分離する。
5. 同意撤回前の履歴と撤回後の操作を区別する。
6. 貢献検証と価値決定を分離する。
7. 既存の検証済み仕様を無断で変更しない。

---

## 1. Purpose

本書の目的は、Toikatsu Protocol v0.1とTIB v0.1の整合性を確認し、将来の検証実装に必要な判断基準を固定することである。

対象は以下のとおり。

- 規範仕様とValidatorの整合性
- 検証結果と外部操作の関係
- 意味変換における不明状態
- 同意撤回時の境界条件
- HandoffとReceiptの解釈
- 元記録の不変性
- 将来の修正と互換性の管理

本書はレビュー文書であり、既存仕様を直接変更するものではない。

---

## 2. Specification Hierarchy

各文書の責務を次のように区別する。

| Document | Responsibility |
|---|---|
| `toikatsu-v0.1.md` | 問い・活動・貢献・検証・handoff |
| `toikatsu-v0.1.schema.json` | 記録形式の検証 |
| `validate_examples.py` | 実装済みの意味検証 |
| `toikatsu-boundary-v0.1.md` | 外部接続の境界 |
| `tib-boundary-validation-v0.1.md` | 境界検証条件 |
| `tib-consistency-review-v0.1.md` | 差異・判断・未解決事項 |

### 2.1 Normative Authority

Toikatsu本体の規範は、Toikatsu本体仕様が定義する。

TIBの規範は、TIB境界仕様が定義する。

本レビューに記載した推奨事項は、正式に仕様へ反映されるまで、新たな適合要件として扱わない。

### 2.2 No Silent Override

ValidatorがPASSしたことを理由として、規範仕様の未実装要件を満たしたと主張してはならない。

逆に、Validator独自の厳しい規則を、文書化せずに共通仕様として扱ってはならない。

---

## 3. Identified Consistency Issues

### TIB-CR-001 — Verification Evidence Alignment

**Issue**

Toikatsu本体仕様は、貢献証拠と検証証拠に少なくとも一つの共通参照を要求する。

現行Validatorは、貢献申告に含まれるすべての証拠を検証記録が参照することを要求する。

両者は同一条件ではない。

**Decision**

TIBでは、単なる参照の重なりではなく、どの証拠が確認されたかを追跡可能にする。

既存Validatorの包含関係チェックは維持し、Toikatsu本体仕様との相違を未解決事項として管理する。

将来の仕様改訂では、すべての申告証拠の確認を必須とするか、重要証拠を明示する別の仕組みを採用するかを決定する。

**Status:** OPEN

### TIB-CR-002 — Verifier Independence

**Issue**

Toikatsu仕様は、検証者と受益者に加えて、検証者と貢献提案者の分離を要求する。

現行Validatorは受益者・参加者とのID一致を検出するが、提案者との一致を独立には検査していない。

**Decision**

以下の区別を維持する。

- IDの分離
- 操作権限の分離
- 実質的な利益相反の確認

TIB適合性を判断する場合、IDの相違だけで独立性を証明したとは扱わない。

提案者とのID一致チェックは、Toikatsu本体Validatorの今後の修正候補とする。

**Status:** OPEN

### TIB-CR-003 — Withdrawal Timestamp Boundary

**Issue**

Toikatsu仕様では、同意撤回時刻と同時刻の新規処理も禁止する。

現行Validatorの一部の撤回判定には、撤回時刻より後であることを示す `>` が使われている。

**Decision**

将来の境界検証では、撤回時刻以降の新規処理を禁止する。

```text
operation_time < withdrawn_at
    -> 以前の処理として評価可能

operation_time >= withdrawn_at
    -> 新規処理は禁止
```

ただし、既存記録の移行や修正では、同時刻データの扱いと時刻精度を確認する必要がある。

**Status:** OPEN

### TIB-CR-004 — Handoff Historical Validity

**Issue**

同意撤回後の記録でも、撤回前に完了したhandoffが存在する。

現在の同意状態だけで過去の処理を判定すると、正当な履歴を誤って拒否する可能性がある。

**Decision**

次の二つを分離する。

1. Historical Validity — 過去の処理が当時の条件を満たしたか。
2. Current Authorization — 現在、新しい処理を行えるか。

過去の正当な処理履歴は、同意撤回だけで不正な処理へ変化しない。

ただし、記録の保持や継続利用は、適用される方針に従う。

**Status:** PRINCIPLE ACCEPTED

### TIB-CR-005 — Receipt Meaning

**Issue**

ToikatsuのReceiptと、決済システムのReceiptは異なる意味を持つ。

**Decision**

TIBでは以下を区別する。

- Handoff Receipt — 受領確認
- Payment Authorization — 支払い認可
- Settlement Receipt — 決済成立の記録
- Redistribution Record — 還元処理の記録

これらを同一の成功状態として扱ってはならない。

**Status:** PRINCIPLE ACCEPTED

---

## 4. UNRESOLVED Handling

### 4.1 Three-Valued Validation

TIBの境界検証結果は次の3種類とする。

| Result | Meaning |
|---|---|
| PASS | 適用される条件を確認できた |
| FAIL | 明示的な違反を確認した |
| UNRESOLVED | 判断に必要な証拠が不足している |

### 4.2 Validation Is Not Execution

検証結果と実行判断を分離する。

| Validation | Default Action |
|---|---|
| PASS | 独立した認可確認へ進める |
| FAIL | 対象操作を拒否 |
| UNRESOLVED | 対象操作を保留 |

PASSは実行許可ではない。

UNRESOLVEDは違反が存在する証明ではない。

ただし、同意・操作認可・価値移転などの重要条件が未確認である場合、処理を実行してはならない。

### 4.3 Fail-Closed Rule

認可条件を確認できない場合は、実行しない。

確認不能であることを理由に、元記録を改変したり削除したりしてはならない。

### 4.4 Missing Evidence

証拠不足によるUNRESOLVEDと、証拠によって確認された違反によるFAILを区別する。

必要な証拠が後から取得できた場合は、独立した再検証として扱う。

---

## 5. Consent Boundary

### 5.1 Historical and Current States

同意の判定では、少なくとも次を区別する。

- 同意取得日時
- 処理日時
- 同意撤回日時
- 現在の同意状態
- 操作の種類
- 許可された利用範囲

### 5.2 No Retroactive Authorization

後から取得した同意によって、過去の無許可操作を自動的に正当化してはならない。

### 5.3 No Retroactive Erasure

同意撤回によって過去の処理が実施されなかったことにはならない。

ただし、削除義務や保持制限が適用される場合、それに従う。

### 5.4 External Propagation

外部接続後に同意が撤回された場合、送付元と送付先の責任範囲を明確にする必要がある。

TIB v0.1では、撤回通知の配送保証や、外部送付先の処理完了確認方式は未定義とする。

---

## 6. Semantic Preservation

### 6.1 Preserved Meanings

以下の意味を維持する。

| Original State | Prohibited Interpretation |
|---|---|
| `candidate` | 検証済み貢献 |
| `rejected` | 検証済み貢献 |
| `verified` | 支払い承認 |
| `ready` | 受領完了 |
| `handed_off` | 決済完了 |
| `withdrawn` | 新規操作への有効な同意 |

### 6.2 Unknown Mapping

対応する意味が存在しない場合、変換結果は `unresolved` として扱う。

推測による状態昇格は禁止する。

### 6.3 Mapping Result vs Boundary Result

意味変換の内部結果と、TIB境界検証の結果を区別する。

例えば、不明な意味を安全に `unresolved` として報告する処理は、テストとしてPASSし得る。

しかし、その変換を利用した外部操作は、必要な意味が確認されるまで保留する。

---

## 7. Authority Separation

TIBでは、次の3段階を区別する。

```text
Information Access
        |
        v
Boundary Validation
        |
        v
Independent Authorization
        |
        v
Permitted Operation
```

Information Accessは操作認可を意味しない。

Boundary ValidationのPASSも操作認可を意味しない。

外部操作には、その操作に対して独立した認可が必要である。

実行主体、対象、目的、操作範囲は、認可条件と一致していなければならない。

---

## 8. Boundary Validation Record

将来の境界検証記録には、最低限、次の情報を含める設計を推奨する。

| Category | Minimum Information |
|---|---|
| Identity | 検証ID、元記録ID |
| Context | 接続元、接続先、操作種別 |
| Policy | 適用した規則と仕様版 |
| Evidence | 判定に利用した証拠 |
| Outcome | PASS / FAIL / UNRESOLVED |
| Reasons | 違反理由または判断不能理由 |
| Time | 検証日時 |
| Validator | 検証主体・実装の識別子 |

### 8.1 Evidence of Verification

単なる `PASS` という文字列だけでは、検証の再現性は確保できない。

どの規則を、どの証拠に対して適用したかを追跡できる構造が必要である。

### 8.2 No Self-Authorization

境界検証記録は、それ自体を実行権限の証明書として使用してはならない。

### 8.3 Privacy

検証記録への参照を保持することと、すべての証拠内容を公開することは異なる。

必要最小限の情報公開を原則とする。

---

## 9. Source Preservation and Failure Isolation

### 9.1 Immutable Source Principle

TIBの意味変換・参照・検証は、元のToikatsu記録を直接変更しないことを原則とする。

元記録の正当な更新が必要な場合は、Toikatsu本体の独立した更新手続きを使用する。

### 9.2 Failure States

外部接続において、以下を区別する。

- 明確な成功
- 明確な失敗
- 処理結果不明
- 検証結果不明

処理結果が不明な場合、成功を推定してはならない。

### 9.3 Retry Boundary

再試行を行う場合、重複処理を防止できる条件と、認可の有効性を確認する。

安全性を確認できない場合、再試行を保留する。

---

## 10. Consistency Decision Register

| ID | Subject | Decision | Status |
|---|---|---|---|
| CR-001 | Evidence alignment | 規範の統一が必要 | OPEN |
| CR-002 | Verifier independence | 提案者との分離を追加検証 | OPEN |
| CR-003 | Withdrawal timestamps | 同時刻の扱いを統一 | OPEN |
| CR-004 | Historical handoff | 履歴と現在の認可を分離 | ACCEPTED |
| CR-005 | Receipt meaning | 受領・決済・還元を分離 | ACCEPTED |
| CR-006 | UNRESOLVED | 判定不能と処理保留を分離 | ACCEPTED |
| CR-007 | Authorization | 境界PASSと実行認可を分離 | ACCEPTED |
| CR-008 | Failure isolation | 元記録を保護 | ACCEPTED |

ACCEPTEDは設計方針への合意を示し、実装済みや検証済みを意味しない。

---

## 11. Compatibility Policy

TIBの導入によって、既存のToikatsu v0.1.0の記録形式を変更しない。

互換性に影響する変更を行う場合は、少なくとも以下を記録する。

1. 変更対象
2. 変更理由
3. 影響する規範条件
4. 影響する既存事例
5. 必要な追加テスト
6. バージョン管理上の扱い

既存のGitHub Actionsが通過していることを理由に、新たな規範上の不一致を放置してはならない。

---

## 12. Completion Criteria

本レビューの設計上の完了条件を次のように定義する。

- 主要な規範差異が明示されている
- 採用する境界原則が明確である
- 未解決事項がOPENとして残されている
- UNRESOLVEDとFAILを区別している
- 検証と実行認可を分離している
- 同意撤回と過去の履歴を区別している
- TIBの接続によって元記録を無断変更しない
- 既存のToikatsu v0.1.0の形式を変更していない

本レビューだけで、TIB実装の適合性や実運用上の安全性が成立するわけではない。

---

## 13. Closing Principle

Toikatsuは、人間の問いから生まれた貢献を記録する。

TIBは、その記録を他のシステムへ接続するときの境界を定義する。

しかし、接続された情報は、元の意味を失ってはならない。

検証結果は、権限へ変化してはならない。

受領記録は、決済完了へ変化してはならない。

同意撤回は、過去の履歴と未来の許可を混同させてはならない。

**Validate the boundary before crossing it.**

**Preserve meaning before transforming it.**

**Separate evidence from authority.**

**Keep the origin intact.**

TIB Consistency Review v0.1

*境界を保つことが、分散したシステム同士の信頼を支える。*
