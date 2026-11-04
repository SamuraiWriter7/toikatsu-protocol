# Toikatsu Interoperability Boundary v0.1

**問い活・相互運用境界仕様 — 接続は許可しても、支配は許可しない**

- Specification Version: `0.1.0`
- Status: Draft / Design Proposal
- Parent Protocol: Toikatsu Protocol v0.1
- Specification ID: `TIB-0.1`
- Scope: Reference / Semantic / Authority / Value Boundaries
- Implementation Status: Not implemented

---

## 0. Fundamental Principle

**Connection does not imply authority.**

接続は、権限の移譲を意味しない。

Toikatsu Interoperability Boundary（以下TIB）は、問い活プロトコルと外部システムの間で、情報を安全かつ検証可能な形で交換するための境界条件を定義する。

本仕様は、外部システムを支配する仕組みではない。

また、Toikatsuの内部構造を外部システムへ強制する仕組みでもない。

それぞれのシステムが独立性を維持しながら、必要な情報だけを交換できる状態を目指す。

基本原則は次のとおりである。

1. 情報の参照は権限の取得を意味しない。
2. 意味変換は元記録の変更を意味しない。
3. 貢献検証は報酬資格の確定を意味しない。
4. Handoffは決済の承認を意味しない。
5. 外部接続はシステムの管理権限を変更しない。
6. 接続に失敗しても元の記録は維持される。

---

## 1. Purpose

TIBの目的は、Toikatsu Protocolと外部プロトコルとの間に、明示的な相互運用境界を設けることである。

対象となる外部プロトコルの例を以下に示す。

- Q Network：問いの来歴、派生、構造変化
- RMTP：異なるプロトコル間の意味変換
- Trace系プロトコル：処理の痕跡と検証証拠
- Royalty OS：価値帰属、Settlement、Redistribution

これらは接続候補であり、正式な相互運用性が確認されたことを意味しない。

TIBは次の問いに答える。

- 外部情報をどの条件で参照できるか。
- 意味変換によって何を保持する必要があるか。
- 外部システムへ何を渡すことができるか。
- どの権限を渡してはならないか。
- 接続失敗時に何を保護するか。

---

## 2. Normative Language

本仕様では以下の規範用語を使用する。

- MUST：必須
- MUST NOT：禁止
- SHOULD：推奨
- SHOULD NOT：非推奨
- MAY：任意

本書は設計提案であり、既存のToikatsu v0.1実装に新しい適合要件を遡及して課すものではない。

TIBへの適合性を主張する実装に対して、以下の規則を適用する。

---

## 3. Architecture

TIBは、Toikatsuと外部プロトコルの間に配置する論理的な境界層である。

```text
        Human Question
              |
              v
      Toikatsu Protocol
              |
              v
   +-----------------------+
   |                       |
   | TIB Boundary Layer    |
   |                       |
   | Reference Boundary    |
   | Semantic Boundary     |
   | Authority Boundary    |
   | Value Boundary        |
   |                       |
   +-----------------------+
              |
      +-------+-------+
      |       |       |
      v       v       v
      Q      RMTP   Royalty
    Network          OS
```

この図は概念構造であり、すべての情報がRMTPを経由する必要はない。

TIBは、中央集権的な管理サーバーとして実装される必要もない。

各システムが境界規則を独立して適用する構造も認める。

### 3.1 Boundary Responsibilities

TIBが担う役割は以下とする。

1. 参照可能な情報の範囲を定義する。
2. 意味変換における保存条件を定義する。
3. 権限を持たない情報交換を保証するための条件を定義する。
4. 貢献検証と価値決定の境界を定義する。
5. 接続に関する追跡可能性を確保する。

TIB自体は、外部システムの処理を実行しない。

---

## 4. Reference Boundary

### 4.1 Definition

Reference Boundaryは、外部プロトコルとの間で交換可能な参照情報の範囲を定義する。

参照は、情報の所在や関係を示すために用いる。

参照先へのアクセス権を自動的に与えるものではない。

### 4.2 Reference Examples

Toikatsuに含まれる以下の情報を、接続候補として利用できる。

| Toikatsu Field | Purpose |
|---|---|
| `question.question_id` | 問いの識別 |
| `question.origin_ref` | 問いの来歴 |
| `activities[].activity_id` | 活動の識別 |
| `activities[].output_refs` | 活動成果への参照 |
| `contributions[].contribution_id` | 貢献の識別 |
| `contributions[].evidence_refs` | 貢献証拠への参照 |
| `verification.verification_id` | 検証記録の識別 |
| `handoff.destination_ref` | 引き渡し先の参照 |
| `handoff.receipt_ref` | 受領記録への参照 |

### 4.3 Reference Rules

- 外部参照は、元記録の識別子を保持しなければならない（MUST）。
- 参照情報は、Toikatsu側の状態を勝手に変更してはならない（MUST NOT）。
- 参照先の存在だけで真正性を認定してはならない（MUST NOT）。
- 外部参照を実行命令として解釈してはならない（MUST NOT）。
- 参照先を取得する場合、アクセス権限を別途確認しなければならない（MUST）。
- 参照先が取得できない場合、取得に成功したものとして扱ってはならない（MUST NOT）。
- 参照先に個人情報が含まれる場合、同意範囲と適用方針を確認しなければならない（MUST）。

### 4.4 Reference Resolution Failure

参照先が取得不能、消失、改ざん、または不一致の場合、TIB実装はその状態を明示しなければならない（MUST）。

失敗した参照を根拠として、新たな検証成立や権限取得を主張してはならない（MUST NOT）。

ただし、過去に正常に成立した処理を、参照取得失敗だけを理由に自動削除する必要はない。

---

## 5. Semantic Boundary

### 5.1 Definition

Semantic Boundaryは、Toikatsuの記録を外部プロトコルの形式へ変換する際、保持すべき意味を定義する。

構文の変換と意味の変更を区別する。

### 5.2 Semantic Invariants

以下の区別を保持しなければならない（MUST）。

| Source Meaning | Must Not Become |
|---|---|
| Question registered | Contribution verified |
| Activity recorded | Contribution established |
| Contribution candidate | Verified contribution |
| Contribution rejected | Verified contribution |
| Contribution verified | Payment authorized |
| Handoff ready | Handoff completed |
| Handoff completed | Settlement completed |
| Consent withdrawn | Consent active |

これらの状態を、変換処理だけで昇格させてはならない（MUST NOT）。

### 5.3 Meaning Preservation

意味変換時には、以下を保持することを基本とする。

- Source protocol identifier
- Source record identifier
- Original status
- Original timestamps
- Evidence references
- Verification references
- Consent restrictions
- Transformation provenance

変換先に対応する意味が存在しない場合、根拠のない値で補完してはならない（MUST NOT）。

変換不能な情報は、欠落情報または未対応の意味として明示すべきである（SHOULD）。

### 5.4 Relationship with RMTP

RMTPは、意味変換を行う外部プロトコルの接続候補である。

TIBはRMTPの内部仕様を再定義しない。

また、RMTPへの接続を必須としない。

TIB適合を主張する変換処理は、元記録から変換結果までの追跡可能性を確保しなければならない（MUST）。

---

## 6. Authority Boundary

### 6.1 Definition

Authority Boundaryは、情報交換と操作権限の委譲を分離するための境界である。

外部システムがToikatsuの記録を受け取っても、Toikatsuの管理権限を取得することはない。

### 6.2 Authority Rules

TIBの接続処理は、明示的かつ独立した許可なしに、以下を行ってはならない（MUST NOT）。

- Toikatsuの元記録の変更
- 同意状態の変更
- 検証結果の上書き
- 検証者のなりすまし
- 外部ツールの実行
- 決済や送金の実行
- 管理者権限の取得
- 他システムへの権限の再委譲

### 6.3 Authority Is Explicit

外部操作が必要な場合、その操作権限は情報の引き渡しとは別の仕組みで確認しなければならない（MUST）。

少なくとも以下の区別を必要とする。

- Information Access
- Operation Authorization
- Execution Authority

情報を読む権限は、操作を実行する権限ではない。

操作が承認されていても、無制限の再委譲を認めるものではない。

### 6.4 Human Authority

人間が関与する承認の仕組みを設ける場合、その決定権をAIによる意味変換だけで代替してはならない（MUST NOT）。

TIBは、承認された権限の範囲を超えない接続を基本とする。

---

## 7. Value Boundary

### 7.1 Definition

Value Boundaryは、貢献の検証と、経済的・社会的価値の決定を分離する。

Toikatsuが扱うのは、問いと活動から生まれた貢献の記録および検証である。

Royalty OSなどの後続システムが扱うのは、適用する制度に基づく価値評価、帰属、決済、還流である。

### 7.2 Value Separation

以下を区別しなければならない（MUST）。

```text
Contribution Evidence
         |
         v
Contribution Verification
         |
         v
Verified Contribution
         |
         v
Handoff
         |
         v
Independent Value Decision
         |
         v
Settlement
         |
         v
Redistribution
```

`Verified Contribution`は、報酬の支払い義務を意味しない。

`Handoff`は、決済完了を意味しない。

### 7.3 Value Rules

- 貢献検証の結果だけで報酬額を確定してはならない（MUST NOT）。
- Handoff Receiptを支払完了証明として扱ってはならない（MUST NOT）。
- 後続システムは独立した価値判定規則を適用しなければならない（MUST）。
- Toikatsuの元記録を報酬決定に合わせて改変してはならない（MUST NOT）。
- 価値評価に使用した根拠と判断は、後続システム側で追跡可能にすべきである（SHOULD）。

### 7.4 Non-Monetary Value

TIBは、金銭的な価値還流に限定されない。

後続システムは、ポイント、クーポン、サービス利用枠などの非金銭的な還元を扱ってもよい（MAY）。

ただし、それらの発行条件や運用責任はTIBの対象外である。

---

## 8. Consent Propagation Boundary

### 8.1 Principle

情報を外部へ接続しても、元の同意条件が消失してはならない。

TIBを通じた情報交換では、目的に応じた同意範囲の確認が必要となる。

### 8.2 Consent Requirements

- 外部引き渡しには、適切な `external_handoff` の同意が必要である（MUST）。
- 公開には、適切な `public_sharing` の同意が必要である（MUST）。
- 意味変換によって利用目的や同意範囲を拡張してはならない（MUST NOT）。
- 同意撤回後の新たな引き渡しを認めてはならない（MUST NOT）。
- 同意撤回前に完了した引き渡しの履歴と、新規処理を区別しなければならない（MUST）。

### 8.3 Withdrawal Propagation

外部へ引き渡した記録に同意撤回が発生した場合、運用主体は適用される同意方針に従って対応しなければならない（MUST）。

必要に応じて、送付先への通知、利用停止、削除、匿名化などを行う。

TIB v0.1は、撤回通知の共通メッセージ形式や配送保証を定義しない。

この機能は将来の拡張候補とする。

---

## 9. Handoff Boundary

### 9.1 Handoff Is Not Settlement

Toikatsuの `handoff.status = handed_off` は、外部送付先による受領確認を表す。

この状態は、以下を意味しない。

- 貢献の再検証完了
- 金銭的価値の確定
- 支払い承認
- 決済完了
- ロイヤルティ分配完了

### 9.2 Handoff Conditions

TIB適合の接続処理では、外部へ貢献記録を引き渡す前に、以下を確認しなければならない（MUST）。

1. 対象貢献が `verified` であること。
2. 外部引き渡しに必要な同意が有効であること。
3. 引き渡し先が明示されていること。
4. 参照する貢献IDが存在すること。
5. 操作主体が必要な権限を持つこと。

引き渡し結果は、受領確認と区別して記録しなければならない（MUST）。

### 9.3 Duplicate Handoff

TIB v0.1では、ネットワーク全体の重複引き渡し防止機構を定義しない。

後続システムは、送付元の名前空間と貢献IDを組み合わせるなどして、重複処理を防ぐべきである（SHOULD）。

同じ貢献情報を再送しただけで、追加報酬の資格が生じるものではない。

---

## 10. Boundary Trace

### 10.1 Purpose

相互運用処理では、どの記録が、どの接続先に、どのような条件で渡されたかを追跡できることが重要である。

そのためTIBでは、接続処理に関する痕跡を記録する考え方を定義する。

### 10.2 Conceptual Trace Fields

将来の実装では、以下の情報を記録することを推奨する。

| Field | Description |
|---|---|
| `boundary_trace_id` | 接続処理の識別子 |
| `source_protocol` | 送付元プロトコル |
| `source_record_id` | 元記録の識別子 |
| `destination_protocol` | 接続先プロトコル |
| `operation_type` | 参照・変換・引き渡し等 |
| `consent_ref` | 同意記録への参照 |
| `transformation_ref` | 意味変換履歴への参照 |
| `authority_ref` | 操作権限の確認記録 |
| `executed_at` | 処理日時 |
| `result` | 処理結果 |

これらは概念フィールドであり、v0.1ではJSON Schemaを定義しない。

### 10.3 Trace Rules

- 接続結果を元のToikatsu記録と関連付けられるようにすべきである（SHOULD）。
- 失敗した処理を成功として記録してはならない（MUST NOT）。
- 検証不能な外部応答を、検証済みの受領記録として扱ってはならない（MUST NOT）。
- 痕跡の保存は、適用されるプライバシー方針および保持規則に従わなければならない（MUST）。

---

## 11. Failure Isolation

### 11.1 Principle

**Boundary failure must not become system-wide authority failure.**

接続境界の失敗によって、元システムの権限や記録の整合性を破壊してはならない。

### 11.2 Failure Cases

想定する失敗例を以下に示す。

- 外部参照先が取得不能
- 意味変換が失敗
- 同意条件が不一致
- 受領記録が欠落
- 送付先が不正な状態を返す
- 検証済み状態への不正な昇格要求
- 権限範囲外の操作要求
- 接続先から不正な命令が送られる

### 11.3 Failure Rules

- 接続失敗によって元記録を変更してはならない（MUST NOT）。
- 確認できない成功状態を推定してはならない（MUST NOT）。
- 権限不明の操作は実行してはならない（MUST NOT）。
- 失敗の影響を可能な限り接続境界内に限定すべきである（SHOULD）。
- 安全に再試行できることが確認できない処理を、自動再実行してはならない（MUST NOT）。

外部接続を停止しても、Toikatsu本体の記録機能を維持できる設計が望ましい。

---

## 12. Protocol Independence

TIBは、個別の外部プロトコルに対して従属しない。

Q Network、RMTP、Royalty OSなどとの接続では、それぞれの責務と仕様を尊重する。

### 12.1 Non-Invasive Integration

TIB適合実装は、外部プロトコルの内部構造を変更することなく接続できる方式を優先すべきである（SHOULD）。

### 12.2 No Mandatory Central Authority

すべての接続を単一の管理主体に集中させることを要求しない。

中央管理型、分散型、混合型の構成を認める。

ただし、いずれの場合も権限境界と検証条件を維持しなければならない（MUST）。

### 12.3 No Implicit Trust

共通の形式やプロトコルを使用しているという理由だけで、相手システムを信頼してはならない（MUST NOT）。

形式への適合、主体の認証、証拠の真正性、操作の認可は別個に確認する。

---

## 13. Security and Privacy

TIBの接続処理では、以下の脅威を考慮する。

- 偽造された参照情報
- 不正な意味変換
- 検証結果の改ざん
- 権限の混同
- プロンプトインジェクション
- 個人情報の漏えい
- 同意撤回後の再利用
- 重複した価値請求
- 偽造された受領記録

### 13.1 Security Requirements

- 外部から取得したデータを命令として実行してはならない（MUST NOT）。
- 操作権限は情報交換とは別に確認しなければならない（MUST）。
- 必要最小限の情報のみ交換すべきである（SHOULD）。
- 接続先の応答を無条件に信用してはならない（MUST NOT）。
- 個人情報の公開と外部提供を同一視してはならない（MUST NOT）。

TIB適合を主張することは、セキュリティ監査の完了を意味しない。

---

## 14. Conformance

### 14.1 Conformance Scope

TIB v0.1の適合性は、境界条件の遵守を対象とする。

Toikatsu本体や接続先プロトコルのすべての要件に対する適合を意味しない。

### 14.2 Minimum Conformance Conditions

TIB適合を主張する実装は、少なくとも以下を満たさなければならない（MUST）。

1. 元記録を無断で変更しない。
2. 元記録と変換結果を関連付けられる。
3. 意味変換によって状態を不正に昇格させない。
4. 情報の参照と操作権限を区別する。
5. 有効な同意の範囲を超えて情報を引き渡さない。
6. 貢献検証を報酬の確定として扱わない。
7. Handoffを決済完了として扱わない。
8. 接続失敗を成功として記録しない。
9. 外部データを無条件に信頼しない。
10. 適用する同意・保持・削除方針を遵守する。

### 14.3 Validation Status

v0.1では、適合性要件の文書化のみを行う。

専用のJSON Schema、PASS／FAIL事例、検証スクリプト、GitHub Actionsは未実装である。

既存のToikatsu v0.1のGitHub Actions通過は、TIBの適合性を証明しない。

将来の実装では、各規則に対応する再現可能な検証事例を整備することが望ましい。

---

## 15. Relationship to Existing Specifications

### 15.1 Toikatsu Protocol

Toikatsuは問い、活動、貢献、検証、handoffの記録を担当する。

TIBはその外部接続条件を担当する。

TIBはToikatsu本体の状態モデルを変更しない。

### 15.2 Q Network

Q Networkは問いの派生・来歴・構造変化を扱う。

TIBは問いの識別子や来歴参照を接続候補として扱う。

### 15.3 RMTP

RMTPは異なる記録構造間の意味変換を扱う。

TIBは、意味変換で失ってはならない境界条件を定義する。

### 15.4 Royalty OS

Royalty OSは価値の帰属、Settlement、Redistributionなどを扱う構想である。

TIBは、検証済み貢献の情報を外部へ接続する条件を定義する。

価値評価や分配を実行しない。

---

## 16. Future Extensions

将来の検討候補として、以下を挙げる。

### v0.2 Candidate

- Boundary Trace JSON Schema
- Reference validation examples
- Semantic preservation tests
- Authority violation tests
- Consent propagation tests
- Handoff boundary tests
- Automated boundary validator

### Later Candidates

- Cross-protocol verification receipts
- Signed boundary records
- Withdrawal notification protocol
- Privacy-preserving reference exchange
- Multi-destination handoff control
- Duplicate value claim detection
- Federated interoperability validation

これらは計画候補であり、実装時期や採用を約束するものではない。

---

## 17. Design Summary

TIBの中心となる設計原則は、以下の4つである。

**Reference Boundary**

参照できることは、操作できることを意味しない。

**Semantic Boundary**

形式を変換できることは、意味を変更できることを意味しない。

**Authority Boundary**

情報を渡すことは、権限を渡すことを意味しない。

**Value Boundary**

貢献を検証することは、報酬を確定することを意味しない。

これらの境界を維持することで、Toikatsuと外部システムは、それぞれの役割を保ちながら接続できる。

---

## 18. Closing Declaration

AI時代のシステムは、すべてを一つの巨大な構造に統合する必要はない。

異なる目的を持つシステムが、互いの独立性を尊重しながら接続できればよい。

問いを扱うシステム。

意味を変換するシステム。

貢献を検証するシステム。

価値を還流するシステム。

それぞれが異なる役割を持ち、必要な情報だけを交換する。

そのために必要なのは、すべてを支配する中央の権限ではなく、明確な境界と検証可能な接続条件である。

**Connect without controlling.**

**Transform without distorting.**

**Verify without granting authority.**

**Circulate value without erasing origin.**

Toikatsu Interoperability Boundary v0.1

*接続は許可しても、支配は許可しない。*
