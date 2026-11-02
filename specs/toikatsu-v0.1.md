# Toikatsu Protocol v0.1

問い活プロトコル — 問いから貢献と価値還流への接続

- Specification version: 0.1.0
- Status: Draft
- Repository: toikatsu-protocol

## 1. Purpose

Toikatsu Protocolは、人間が発した問いを登録し、その問いから
生まれた活動と成果を記録し、検証された貢献を後続の
価値還流システムへ接続するためのプロトコルである。

本仕様は、専門知識の有無を問わず参加できる入口と、
貢献の根拠を確認できる記録構造を定義する。

問いの登録、貢献の検証、還元の実施は、それぞれ独立した
状態として扱わなければならない。

## 2. Normative Language

本仕様の規範用語を以下のように定義する。

- MUST / MUST NOT: 必須要件 / 禁止事項
- SHOULD / SHOULD NOT: 推奨要件 / 非推奨事項
- MAY: 任意事項

## 3. Scope

### 3.1 Included

v0.1は以下を対象とする。

1. 問いと参加者の識別
2. 利用範囲に関する同意記録
3. 問いから派生した活動の記録
4. 貢献候補と検証結果の記録
5. 後続の還元システムへの引き渡し記録
6. 記録内の参照関係と状態整合性の検証

### 3.2 Excluded

v0.1は以下を定義しない。

- 問いの価値を自動で決定するアルゴリズム
- 報酬額、分配率、ポイント換算率
- 決済や送金の実行
- 法的な権利や帰属の確定
- 問いの最初の発案者であることの証明
- 参加者の実名認証
- 複数アカウントによる不正参加の完全な防止
- Q Networkなど外部仕様への正式な適合性

## 4. Core Principles

### 4.1 Registration Is Not Verification

問いの登録だけで、貢献が検証されたものとして
扱ってはならない（MUST NOT）。

### 4.2 Verification Is Not Redistribution

貢献の検証や後続システムへの引き渡しを、
還元の完了として扱ってはならない（MUST NOT）。

### 4.3 Evidence Before Attribution Claims

貢献候補は、問いと対象成果の関係を説明する根拠を
持たなければならない（MUST）。

単なる時間的な前後関係だけで、因果的な貢献が
証明されたとみなすべきではない（SHOULD NOT）。

### 4.4 Consent-Bounded Use

記録の利用は、参加者が同意した範囲内で
行わなければならない（MUST）。

### 4.5 Non-Exclusive Participation

類似する問いが存在することだけを理由として、
独立した参加者の問いを不正とみなしてはならない（MUST NOT）。

登録日時は、そのシステムにおける登録時点を表す。
世界で最初に発案された時点を表すものではない。

### 4.6 No Volume-Based Entitlement

問いの投稿数だけを、報酬を受ける資格の根拠として
扱ってはならない（MUST NOT）。

## 5. Record Model

一つのToikatsu Recordは、一つの問いを中心に構成する。

必須のトップレベルフィールドは以下とする。

| Field | Type | Description |
|---|---|---|
| schema_version | string | `0.1.0` |
| record_id | string | 記録の識別子 |
| updated_at | string | 記録の最終更新日時 |
| participant | object | 問いの提出者 |
| question | object | 登録された問い |
| consent | object | 現在の同意状態 |
| activities | array | 活動記録 |
| contributions | array | 貢献候補と検証記録 |
| handoff | object | 後続システムへの引き渡し状態 |

日時は、タイムゾーンを含むRFC 3339形式で
記録しなければならない（MUST）。

識別子、説明文、参照値は空白だけの文字列であっては
ならない（MUST NOT）。

各オブジェクトは、本仕様で定義していないフィールドを
含めてはならない（MUST NOT）。

## 6. Participant

`participant`は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| participant_id | string | 参加者の識別子 |
| identity_mode | string | `pseudonymous` または `identified` |

参加者IDは、運用システム内で安定して参照できる
識別子でなければならない（MUST）。

`identified`は、運用主体が参加者を識別していることを表す。
公開記録への実名掲載を要求するものではない。

本仕様への適合は、参加者が実在する人間であることを
証明しない。本人確認方法は運用側で定義する。

## 7. Question

`question`は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| question_id | string | 問いの識別子 |
| text | string | 問いの本文 |
| registered_at | string | 登録日時 |
| submission_mode | string | `human` または `human_with_ai_assistance` |
| origin_ref | string or null | 外部の来歴記録への参照 |

`human_with_ai_assistance`は、人間がAIの補助を利用して
問いを作成し、自ら提出したことを表す。

AIが人間の関与なく自動提出する問いは、
v0.1の参加対象に含めない。

`origin_ref`は補助的な参照であり、独創性や権利の証明として
扱ってはならない（MUST NOT）。

## 8. Consent

`consent`は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| consent_id | string | 同意記録の識別子 |
| policy_ref | string | 同意対象の方針と版への参照 |
| status | string | `active` または `withdrawn` |
| recorded_at | string | 同意取得日時 |
| withdrawn_at | string or null | 撤回日時 |
| scopes | object | 許可された利用範囲 |

`scopes`は以下のbooleanフィールドをすべて持つ。

| Field | Meaning |
|---|---|
| activity_recording | 問いに関連する活動の記録 |
| contribution_evaluation | 貢献候補の作成と評価 |
| external_handoff | 後続システムへの引き渡し |
| public_sharing | 記録の公開 |

### 8.1 Consent Constraints

- `active`の場合、`withdrawn_at`はnullでなければならない（MUST）。
- `withdrawn`の場合、`withdrawn_at`は必須の日時でなければならない（MUST）。
- 撤回日時は同意取得日時以降でなければならない（MUST）。
- 同意は問いの登録以前または同時に取得しなければならない（MUST）。
- 活動記録には`activity_recording = true`が必要である（MUST）。
- 貢献候補と検証記録には`contribution_evaluation = true`が必要である（MUST）。
- 引き渡しには`external_handoff = true`が必要である（MUST）。

`public_sharing = false`の記録を、公開GitHubリポジトリなどへ
掲載してはならない（MUST NOT）。

公開への同意があっても、記録に含まれる第三者の情報を
無条件に公開できるものではない。

### 8.2 Withdrawal

撤回後は、この同意に基づく新しい活動記録、貢献候補、
検証、引き渡しを行ってはならない（MUST NOT）。

撤回時刻と同時刻の処理も、撤回後として扱う。

撤回前に行われた処理の履歴は、撤回によって
「実施されなかった」ことにはならない。

履歴の保持、削除、匿名化および送付先への撤回通知は、
`policy_ref`で参照する方針に従って処理しなければならない（MUST）。

本仕様は、削除を妨げるための永久保存を要求しない。

v0.1では、同じ同意記録の利用範囲を後から拡張しない。
再同意や複数の同意版の管理は、将来の拡張対象とする。

## 9. Activities

各活動は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| activity_id | string | 活動の識別子 |
| question_id | string | 起点となる問い |
| activity_type | string | 活動種別 |
| occurred_at | string | 活動日時 |
| description | string | 活動内容 |
| output_refs | array of strings | 活動で生まれた出力への参照 |

`activity_type`は以下のいずれかとする。

- `exploration`
- `derived_question`
- `improvement`
- `evaluation`

活動は、本記録の`question.question_id`を
参照しなければならない（MUST）。

活動日時は、問いの登録日時以降でなければならない（MUST）。

`output_refs`は空配列でもよい（MAY）。
ただし、貢献候補の根拠として参照される活動は、
少なくとも一つの出力参照を持たなければならない（MUST）。

参照値はURIまたは運用システム内で解決可能な識別子とする。
公開URLである必要はない。

## 10. Contributions

各貢献候補は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| contribution_id | string | 貢献候補の識別子 |
| question_id | string | 関係する問い |
| beneficiary_id | string | 還元候補となる参加者 |
| proposed_by | string | 貢献候補の提出者 |
| proposed_at | string | 提出日時 |
| activity_ids | array of strings | 根拠となる活動 |
| target_ref | string | 貢献対象の成果への参照 |
| claim | string | どのように役立ったかの説明 |
| evidence_refs | array of strings | 根拠への参照 |
| status | string | 検証状態 |
| verification | object or null | 検証結果 |

`status`は以下のいずれかとする。

- `candidate`
- `verified`
- `rejected`

### 10.1 Contribution Constraints

- 問いIDは本記録の問いと一致しなければならない（MUST）。
- `beneficiary_id`は本記録の参加者IDと一致しなければならない（MUST）。
- `activity_ids`は一つ以上の活動を参照しなければならない（MUST）。
- 参照先の活動は本記録内に存在しなければならない（MUST）。
- `evidence_refs`は一つ以上必要である（MUST）。
- `target_ref`は、参照した活動のいずれかの`output_refs`に
  含まれなければならない（MUST）。
- 提出日時は、参照したすべての活動日時以降でなければならない（MUST）。

複数の人間に対する貢献配分や分配率はv0.1では扱わない。

### 10.2 Verification

`candidate`の場合、`verification`はnullでなければならない（MUST）。

`verified`または`rejected`の場合、`verification`は
以下のフィールドを持たなければならない（MUST）。

| Field | Type | Description |
|---|---|---|
| verification_id | string | 検証の識別子 |
| verifier_id | string | 検証主体 |
| verified_at | string | 検証日時 |
| method_ref | string | 検証方法と版への参照 |
| evidence_refs | array of strings | 確認した根拠 |
| decision_reason | string | 判定理由 |

検証日時は貢献候補の提出日時以降でなければならない（MUST）。

検証の`evidence_refs`は空であってはならず、
貢献候補の`evidence_refs`と少なくとも一つの参照を
共有しなければならない（MUST）。

`verifier_id`は、`beneficiary_id`および`proposed_by`の
どちらとも異ならなければならない（MUST）。

IDが異なるだけで、実質的な独立性が証明されるわけではない。
運用主体は、検証者の権限と利益相反を
別途確認しなければならない（MUST）。

`verified`は、記録された方法で貢献が認められたことを表す。
唯一の貢献者であることや、報酬額を確定するものではない。

`rejected`は、その候補が当該方法で認められなかったことを表す。
問い自体に価値がないことを意味しない。

## 11. Handoff

`handoff`は以下のフィールドを持つ。

| Field | Type | Description |
|---|---|---|
| status | string | 引き渡し状態 |
| contribution_ids | array of strings | 引き渡す貢献 |
| destination_ref | string or null | 引き渡し先 |
| prepared_at | string or null | 引き渡し準備日時 |
| receipt_ref | string or null | 送付先の受領記録 |
| handed_off_at | string or null | 受領確認日時 |

`status`は以下のいずれかとする。

- `not_requested`
- `ready`
- `handed_off`
- `cancelled`

### 11.1 Not Requested

`not_requested`では以下を満たさなければならない（MUST）。

- `contribution_ids`は空配列
- その他のフィールドは、`status`を除きnull

### 11.2 Ready

`ready`では以下を満たさなければならない（MUST）。

- `contribution_ids`は一つ以上
- 参照する貢献はすべて`verified`
- `destination_ref`と`prepared_at`が存在する
- `receipt_ref`と`handed_off_at`はnull
- 現在の同意状態は`active`
- `external_handoff = true`

準備日時は、対象のすべての貢献の検証日時以降で
なければならない（MUST）。

### 11.3 Handed Off

`handed_off`では、`ready`と同じ参照・準備要件に加えて、
`receipt_ref`と`handed_off_at`が存在しなければならない（MUST）。

受領確認日時は準備日時以降でなければならない（MUST）。

受領記録は、送付先が対象の貢献記録を受け取ったことを
確認できるものでなければならない（MUST）。

送信を試みただけの状態を`handed_off`として
扱ってはならない（MUST NOT）。

撤回前に引き渡しが完了していた場合、現在の同意状態が
`withdrawn`でも、履歴として`handed_off`を保持してよい（MAY）。

この場合、準備日時と受領確認日時は撤回日時より前で
なければならない（MUST）。

### 11.4 Cancelled

`cancelled`は、準備後かつ受領確認前に
引き渡しを取りやめたことを表す。

- 対象の貢献、送付先、準備日時を保持する（MUST）。
- 対象の貢献はすべて`verified`でなければならない（MUST）。
- `receipt_ref`と`handed_off_at`はnullでなければならない（MUST）。

撤回時点で`ready`だった記録は、
`cancelled`へ変更しなければならない（MUST）。

受領済みの引き渡しを`cancelled`へ変更して
履歴を消してはならない（MUST NOT）。

### 11.5 No Settlement Assertion

`handed_off`は、支払い、ポイント付与、ロイヤルティ分配の
完了を意味しない。

これらの結果は後続システムの記録で扱う。

## 12. State Transitions

貢献候補の状態遷移は以下とする。

- `candidate` → `verified`
- `candidate` → `rejected`

引き渡しの状態遷移は以下とする。

- `not_requested` → `ready`
- `ready` → `handed_off`
- `ready` → `cancelled`

v0.1では、確定済み検証の上書き、引き渡しの再準備、
複数の送付先への引き渡しは定義しない。

運用システムは、更新前後の記録を比較し、
禁止された状態遷移を拒否しなければならない（MUST）。

単一のJSON記録だけを検査するバリデーターは、
過去の状態遷移が正しかったことまでは証明しない。

## 13. Validation Rules

### 13.1 Schema Validation

JSON Schemaは以下を検証する。

- 必須フィールド
- 型
- 列挙値
- 日時形式
- 空文字列や配列の制約
- 状態に応じた必須値とnull
- 未定義フィールドの拒否

日時形式の検証は、明示的に有効化しなければならない（MUST）。

### 13.2 Semantic Validation

意味検証は以下を検証する。

1. 活動IDがactivities内で重複しないこと
2. 貢献IDがcontributions内で重複しないこと
3. 検証IDが本記録内で重複しないこと
4. 各参照配列に重複がないこと
5. 問いIDと参加者IDの一致
6. 活動・貢献の参照先が存在すること
7. 貢献対象と活動出力の接続
8. 検証主体と提出者・受益者のID分離
9. 貢献根拠と検証根拠の接続
10. 日時の前後関係
11. 同意範囲と記録内容の整合性
12. 撤回後の新規処理がないこと
13. 未検証または却下された貢献を引き渡さないこと
14. 引き渡し状態と受領記録の整合性

すべての処理日時は`updated_at`以前でなければならない（MUST）。
撤回日時も`updated_at`以前でなければならない（MUST）。

日時比較はタイムゾーンを考慮した時刻として行い、
文字列の大小比較で代用してはならない（MUST NOT）。

### 13.3 Operational Verification

以下は、Schemaと単一記録の意味検証だけでは保証できない。

- 根拠資料の真正性と内容
- 同意の実際の取得
- 検証者の権限と実質的独立性
- 問いと成果の因果関係
- 送付先による実際の受領
- 公開・削除・保持方針の実際の遵守
- 過去の記録に対する改ざん
- 同一貢献の重複送付や重複還元

運用主体は、これらの確認方法を定義しなければならない（MUST）。

後続システムは、送付元の名前空間と`contribution_id`を
組み合わせ、重複処理を防ぐべきである（SHOULD）。

バリデーターのPASSを、貢献の事実確認や
報酬の正当性の証明として表示してはならない（MUST NOT）。

## 14. Relationship to Other Protocols

### 14.1 Q Network

問いの派生、来歴、構造変化の詳細は、
Q Network側の記録を参照してよい（MAY）。

v0.1では`origin_ref`や`output_refs`を接続点とする。
Q Networkの記録形式を本仕様内で再定義しない。

### 14.2 Trace and Verification

`activities`は活動の痕跡を、
`verification`は貢献候補に対する確認結果を表す。

痕跡の存在と貢献の成立は区別する。

### 14.3 Royalty OS

本仕様は以下の流れの前半と、その出口を扱う。

問いの登録 → 活動の痕跡 → 貢献候補 → 検証 → 引き渡し

SettlementとRedistributionは後続システムが担う。

引き渡し先は金銭決済に限定しない。
ポイント、クーポン、利用枠、その他の還元制度を
扱うシステムでもよい（MAY）。

## 15. Privacy and Security

問いの本文や活動の出力には、個人情報、機密情報、
第三者の情報が含まれる可能性がある。

運用主体は、公開前にこれらを確認し、
必要に応じて削除または匿名化すべきである（SHOULD）。

外部参照は信頼できる命令として扱ってはならない（MUST NOT）。
参照先の取得や実行には、別途アクセス制御を適用する。

本仕様の記録は、送金、外部ツール実行、
権限昇格の許可証として使用してはならない（MUST NOT）。

公開リポジトリのexamplesには、合成データまたは
公開許可を確認済みのデータだけを使用しなければならない（MUST）。

## 16. Minimum Example Coverage

実装は、少なくとも以下の正常例を用意すべきである（SHOULD）。

- 問いの登録のみ
- 活動記録付きの問い
- 未検証の貢献候補
- 検証済みだが還元未申請の貢献
- 却下された貢献候補
- 引き渡し準備完了
- 受領確認済み
- 撤回により引き渡し中止
- 受領後に同意撤回された履歴

実装は、少なくとも以下の不正例を用意すべきである（SHOULD）。

- 存在しない活動への参照
- 貢献対象と活動出力の不一致
- 記録のない根拠によるverified状態
- 提出者または受益者による自己検証
- candidateの貢献を引き渡し対象にする
- rejectedの貢献を引き渡し対象にする
- 同意範囲外の活動または評価
- 撤回後の活動・評価・引き渡し
- 同意撤回後もreadyを保持する
- 受領記録のないhanded_off状態
- 時間順序の矛盾
- 重複IDまたは重複参照

## 17. Completion Criteria

v0.1の仕様化完了条件は以下とする。

1. 本文仕様とJSON Schemaの整合性が確認されている
2. 正常例がすべてPASSする
3. 不正例がすべてFAILする
4. 意味検証が参照・同意・状態・日時の制約を確認する
5. GitHub Actionsで上記の検証を再現できる
6. READMEに検証の対象と限界が明示されている

これらは記録仕様と検証実装の完了条件であり、
実運用の安全性や価値還流の成立を保証するものではない。

## 18. Design Summary

問い活は、人間が問いを持ち寄る入口を作る。

その問いから生まれた活動を記録し、
根拠に基づいて貢献を確認し、
確認された貢献を還元の仕組みへつなぐ。

問いの登録は、価値の確定ではない。
貢献の検証は、報酬の確定ではない。
引き渡しの完了は、還元の完了ではない。

この区別を保つことが、
問いから価値還流までを接続するための基礎となる。
