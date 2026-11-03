# Toikatsu Protocol

**問い活プロトコル — 人間の問いを記録し、貢献を検証し、価値還流へつなぐための共通仕様**

Version: `v0.1.0`  
Specification Status: Draft  
Validation: GitHub Actions verified

---

## 1. Overview

Toikatsu Protocol（問い活プロトコル）は、人間が発した問いを起点として、そこから生まれた活動、成果、貢献候補、検証結果を記録するためのオープンなプロトコルです。

その目的は、専門知識や技術力の有無にかかわらず、誰もが「問い」を通じて知識創造や社会的な価値形成に参加できる仕組みを設計することです。

問いを登録しただけで、その問いに価値があると確定するわけではありません。

また、貢献が検証されたからといって、直ちに報酬を受け取る権利が発生するわけでもありません。

Toikatsu Protocolは、これらの段階を明確に分離します。

```text
Human Question
      |
      v
Question Registration
      |
      v
Activity Recording
      |
      v
Contribution Candidate
      |
      v
Independent Verification
      |
      +----> Rejected
      |
      v
Verified Contribution
      |
      v
Handoff
      |
      v
External Value Circulation System
      |
      v
Settlement / Redistribution
```

`Settlement` と `Redistribution` は、Toikatsu v0.1の対象外です。

---

## 2. Why Toikatsu?

AI時代には、人間が発した問いが、新しい研究、技術、創作、サービス改善などの出発点になることがあります。

しかし、問いの存在と、その問いが生み出した成果との関係を記録する共通の仕組みは、まだ十分に整備されているとはいえません。

Toikatsu Protocolは、この問題に対して、問いから貢献までの経緯を追跡できる記録構造を提案します。

基本的な考え方は次のとおりです。

- 誰もが問いを提出できる
- 問いから生まれた活動を記録できる
- 活動と成果の関係を追跡できる
- 貢献候補を根拠とともに提出できる
- 独立した検証者が貢献を評価できる
- 検証済みの貢献を後続システムへ引き渡せる

問いの数や人気だけで、貢献の価値を決定することはありません。

**問いの登録、貢献の検証、価値の還元は、それぞれ異なる処理です。**

---

## 3. Design Principles

### 3.1 Human-Centered Participation

問い活は、人間を中心とした参加構造です。

v0.1では、人間による問いの提出と、人間がAIの補助を利用して提出する問いを対象とします。

AIによる完全自動投稿は対象外です。

### 3.2 Registration Is Not Verification

問いの登録は、貢献の成立を意味しません。

### 3.3 Evidence Before Attribution

貢献候補には、問いと成果との関係を説明する根拠が必要です。

単なる時間的な前後関係だけでは、因果的な貢献は証明されません。

### 3.4 Independent Verification

貢献の申告と検証を分離します。

受益者による自己検証を禁止し、検証主体の独立性を重視します。

### 3.5 Consent-Bounded Use

活動記録、貢献評価、外部引き渡し、公開には、それぞれ適切な同意が必要です。

同意撤回後の新たな処理は禁止します。

### 3.6 Verification Is Not Payment

検証済みの貢献は、報酬の支払いを保証するものではありません。

支払いや価値還流は後続システムが扱います。

### 3.7 Non-Exclusive Participation

同じような問いが複数存在しても、それだけで不正と判断しません。

問いの登録日時は、世界で最初に着想したことの証明ではありません。

---

## 4. Scope of v0.1

### Included

Toikatsu Protocol v0.1は、以下を対象とします。

1. 人間の問いの登録
2. 参加者の識別
3. 同意範囲の記録
4. 問いから派生した活動の記録
5. 貢献候補の提出
6. 貢献の検証または却下
7. 検証済み貢献の外部引き渡し
8. JSON Schemaと意味検証
9. GitHub Actionsによる自動テスト

### Excluded

以下はv0.1の対象外です。

- 問いの金銭的価値の自動算定
- ポイントや報酬額の決定
- ロイヤルティ分配率の計算
- 決済や送金
- 法的な権利の確定
- 問いの独創性の完全な証明
- 実名認証の実装
- 不正参加の完全な防止
- 外部プロトコルとの正式な相互運用保証

---

## 5. Record Structure

一つのToikatsu Recordは、一つの問いを中心に構成されます。

主要フィールドは以下のとおりです。

| Field | Description |
|---|---|
| `schema_version` | 仕様バージョン |
| `record_id` | 記録の識別子 |
| `updated_at` | 最終更新日時 |
| `participant` | 参加者情報 |
| `question` | 登録された問い |
| `consent` | 同意状態と利用範囲 |
| `activities` | 問いから派生した活動 |
| `contributions` | 貢献候補と検証結果 |
| `handoff` | 外部引き渡し状態 |

### Question

問いには、本文、識別子、登録日時、提出方式などを記録します。

提出方式は次の2種類です。

- `human`
- `human_with_ai_assistance`

### Activities

問いから派生した活動を記録します。

活動種別は以下の4種類です。

- `exploration`
- `derived_question`
- `improvement`
- `evaluation`

### Contributions

貢献候補には、関連する活動、成果物、根拠、受益候補者などを記録します。

貢献状態は以下の3種類です。

- `candidate`
- `verified`
- `rejected`

`verified` は、記録された検証方法に基づいて貢献が認められたことを表します。

唯一の貢献者であることや、報酬の資格を確定するものではありません。

---

## 6. Consent and Withdrawal

Toikatsu Protocolは、参加者の同意を基本条件とします。

同意には、次の4つの利用範囲があります。

| Scope | Purpose |
|---|---|
| `activity_recording` | 活動記録 |
| `contribution_evaluation` | 貢献の評価 |
| `external_handoff` | 外部システムへの引き渡し |
| `public_sharing` | 記録の公開 |

同意状態は次の2種類です。

- `active`
- `withdrawn`

同意撤回後は、その同意を根拠とする新たな活動記録、貢献評価、引き渡しを行ってはなりません。

ただし、撤回前に正常に完了した処理は、撤回によって過去に存在しなかったことにはなりません。

記録の保持、削除、匿名化、撤回通知は、適用される方針に従って処理します。

---

## 7. Verification

貢献の検証では、以下を確認します。

- 貢献対象と活動成果の関係
- 根拠への参照
- 活動と貢献の識別子
- 検証者の独立性
- 貢献申告と検証の時系列
- 同意状態
- 検証記録の一意性

検証記録には以下の情報を含めます。

| Field | Description |
|---|---|
| `verification_id` | 検証ID |
| `verifier_id` | 検証主体 |
| `verified_at` | 検証日時 |
| `method_ref` | 検証方法への参照 |
| `evidence_refs` | 確認した根拠 |
| `decision_reason` | 判定理由 |

貢献が却下された場合も、検証記録と判定理由を残します。

形式的な検証を通過しても、根拠資料の真正性や実際の因果関係が証明されたとは限りません。

---

## 8. Handoff

Handoffは、検証済みの貢献を後続システムへ引き渡すための状態管理です。

状態は以下の4種類です。

| Status | Meaning |
|---|---|
| `not_requested` | 引き渡し未申請 |
| `ready` | 引き渡し準備完了 |
| `handed_off` | 受領確認済み |
| `cancelled` | 引き渡し中止 |

基本的な状態遷移は以下のとおりです。

```text
not_requested
      |
      v
    ready
      |
      +------> cancelled
      |
      v
  handed_off
```

`ready` の段階では、受領Receiptは不要です。

`handed_off` には、送付先の受領を示す `receipt_ref` が必要です。

同意撤回前に正常に完了した引き渡しは、履歴として記録できます。

Handoffは支払いの実行ではありません。

---

## 9. Repository Structure

```text
toikatsu-protocol/
|
|-- README.md
|
|-- specs/
|   `-- toikatsu-v0.1.md
|
|-- schemas/
|   `-- toikatsu-v0.1.schema.json
|
|-- examples/
|   `-- v0.1/
|       |-- pass/
|       |   `-- *.json
|       |
|       `-- fail/
|           `-- *.json
|
|-- scripts/
|   `-- validate_examples.py
|
`-- .github/
    `-- workflows/
        `-- validate.yml
```

- `specs/` — プロトコルの規範仕様
- `schemas/` — JSON Schema
- `examples/v0.1/pass/` — 正常な記録例
- `examples/v0.1/fail/` — 異常な記録例
- `scripts/` — 検証スクリプト
- `.github/workflows/` — CI設定

---

## 10. Validation

Toikatsu v0.1では、JSON Schema検証と意味検証を組み合わせます。

### JSON Schema Validation

以下を確認します。

- 必須フィールド
- データ型
- 列挙値
- 日時形式
- 状態ごとの必須値
- null制約
- 未定義フィールド

### Semantic Validation

以下を確認します。

- IDの一意性
- 問いと活動の参照関係
- 貢献対象と活動成果の整合性
- 貢献と検証の証拠関係
- 検証者と受益者の分離
- 時刻の前後関係
- 同意範囲
- 同意撤回後の操作
- 未検証貢献の引き渡し
- HandoffとReceiptの整合性

### Expected Results

正常例はPASS、異常例はFAILとなることを確認します。

```text
examples/v0.1/pass/  -> PASS
examples/v0.1/fail/  -> FAIL
```

異常例では、単に検証が失敗するだけでなく、意図した違反理由を検出できることも重要です。

### Current Validation Result

GitHub Actionsによるv0.1の検証が通過しました。

修正前の実行では31件中27件が一致し、残り4件について意味検証規則を修正しました。

修正後のGitHub Actions通過が確認されています。

この結果は、収録されたテスト事例に対する検証成功を意味します。

すべての実運用条件、真正性、外部システムの安全性を証明するものではありません。

---

## 11. Running Validation Locally

### Requirements

- Python 3.12
- `jsonschema` 4.x

### Install Dependencies

```bash
python -m pip install "jsonschema>=4.18,<5"
```

### Run All Validations

リポジトリのルートから実行します。

```bash
python scripts/validate_examples.py
```

### Specify Schema Explicitly

```bash
python scripts/validate_examples.py \
  --schema schemas/toikatsu-v0.1.schema.json
```

### Semantic Validation Only

```bash
python scripts/validate_examples.py --no-schema
```

正常終了時、Validatorは終了コード `0` を返します。

期待結果に不一致がある場合は、終了コード `1` を返します。

検証結果の例：

```text
[MATCH] examples/v0.1/pass/... expected=PASS actual=PASS
[MATCH] examples/v0.1/fail/... expected=FAIL actual=FAIL

=== Toikatsu v0.1: 31/31 matched ===
```

---

## 12. GitHub Actions

GitHub Actionsにより、以下の検証を自動実行します。

1. Python環境の準備
2. 検証ライブラリのインストール
3. Python構文チェック
4. JSON構文チェック
5. JSON Schema検証
6. 意味検証
7. PASS／FAIL期待結果の照合

ワークフロー：

```text
.github/workflows/validate.yml
```

主な実行条件：

- `main` ブランチへの対象ファイルのPush
- Pull Requestでの対象ファイル変更
- 手動実行（workflow_dispatch）

検証が失敗した場合、GitHub Actionsは失敗状態を返します。

---

## 13. Relationship to Other Protocols

Toikatsu Protocolは、既存のAI関連仕様を置き換えるものではありません。

問いから価値還流へ至る過程の入口を担当する設計です。

### Q Network

Q Networkは、問いの派生、来歴、構造変化などを扱います。

Toikatsuは、問いの登録と活動記録を中心とします。

将来的には、`origin_ref`などを通じた接続を検討できます。

### Trace and Verification

Traceは活動や処理の痕跡を扱い、Verificationは貢献候補に対する確認結果を扱います。

痕跡の存在は、貢献の成立を自動的に意味しません。

### Royalty OS

Royalty OSは、価値の帰属、決済、還流などを扱う上位の構想です。

Toikatsuは、その前段階である問いの登録、活動記録、貢献検証、引き渡しを担当します。

```text
Toikatsu Protocol
       |
       v
Question
       |
       v
Activity / Trace
       |
       v
Contribution
       |
       v
Verification
       |
       v
Handoff
       |
       v
External Value System
       |
       v
Settlement
       |
       v
Redistribution
```

将来の還元方式は、金銭に限定されません。

ポイント、クーポン、サービス利用枠なども、後続システムの設計対象になり得ます。

ただし、それらの発行や分配はv0.1では実装しません。

---

## 14. Privacy and Security

Toikatsu Protocolでは、以下の原則を重視します。

- 参加者の同意範囲を尊重する
- 同意撤回後の新規処理を禁止する
- 個人情報や機密情報を無条件に公開しない
- 外部参照を信頼済み命令として扱わない
- 検証記録を送金や権限昇格の許可証として利用しない
- 検証者の利益相反を確認する
- 過去の処理履歴と現在の権限を区別する

公開するサンプルには、原則として合成データを使用します。

ValidatorがPASSを返した場合でも、運用上の安全性や法的適合性を保証するものではありません。

---

## 15. Current Status

**Version:** v0.1.0  
**Specification:** Draft  
**JSON Schema:** Available  
**PASS/FAIL Examples:** Available  
**Semantic Validator:** Available  
**GitHub Actions:** Passed

v0.1は、問いの登録から検証済み貢献の引き渡しまでを扱う、最初の仕様化段階です。

この段階では、実際の価値還流システムとの接続や本番運用を保証しません。

今後の拡張では、以下の課題が考えられます。

- 複数参加者による共同貢献
- 複数の検証者による評価
- 検証の異議申し立て
- より詳細な状態遷移履歴
- 外部Traceとの相互運用
- 検証済み貢献の重複引き渡し防止
- プライバシー保護型の来歴証明
- 後続の価値還流システムとの接続

これらは将来の検討項目であり、v0.1での実装を意味しません。

---

## 16. Documentation

詳細仕様：

[Toikatsu Protocol v0.1 Specification](specs/toikatsu-v0.1.md)

JSON Schema：

[Toikatsu v0.1 JSON Schema](schemas/toikatsu-v0.1.schema.json)

Validation Script：

[validate_examples.py](scripts/validate_examples.py)

GitHub Actions：

[validate.yml](.github/workflows/validate.yml)

---

## 17. Design Philosophy

Toikatsuは、問いそのものに自動的な価格を付ける仕組みではありません。

人間が発した問いを出発点として、そこから生まれる活動と貢献の関係を記録し、適切な根拠に基づいて評価できる構造を目指します。

問いを発することは、知識創造への参加の入口です。

しかし、問いが登録されたことと、貢献が成立したことは同じではありません。

貢献が検証されたことと、報酬が確定したことも同じではありません。

この境界を維持することで、問いの自由な参加と、価値還流の信頼性を両立させることを目指します。

**Questions create possibilities.  
Evidence supports contributions.  
Verification builds trust.  
Value circulation requires accountability.**

---

## 18. Closing Statement

問いは、専門家だけのものではありません。

子どもも、大人も、研究者も、技術者も、日常生活の中で疑問を持つ人も、問いを通じて新しい可能性を生み出すことができます。

Toikatsu Protocolは、その可能性を記録し、検証可能な貢献へとつなぐための小さな共通基盤です。

問いを独占するのではなく、問いから生まれた価値を追跡できるようにする。

価値を自動的に決めるのではなく、根拠と検証を通じて判断できるようにする。

そして、貢献が認められたとき、その記録を将来の価値還流の仕組みへ接続できるようにする。

**問いから、貢献へ。  
貢献から、検証へ。  
検証から、価値還流へ。**

Toikatsu Protocol v0.1 is the first step.
