# Structural Transformation Vocabulary v0.1

**A Controlled Vocabulary for Structural DNA Transformation Operators**

構造DNAのための構造変換演算子・共通語彙仕様

- Specification ID: `SDNA-VOCAB-0.1`
- Version: `0.1.0`
- Status: Draft / Design Proposal
- Parent Specification: `specs/structural-dna/structural-dna-v0.1.md`
- Repository: `toikatsu-protocol`
- Implementation Status: Not implemented

---

## 0. Fundamental Principle

**A transformation operator describes a structural change, not a keyword.**

構造変換演算子は、単語ではなく、構造がどのように変化するかを表す。

同じ単語を使用した問いでも、異なる構造変換を表す場合がある。

また、異なる単語を使用した問いでも、同一または類似した構造変換を表す場合がある。

本仕様では、単語の出現だけを根拠として構造変換演算子を確定してはならない（MUST NOT）。

各演算子は、次の関係によって解釈する。

1. 変換前の構造
2. 変換を必要とする条件
3. 実行または提案される操作
4. 変換後の構造
5. 分析根拠

構造変換は、問いの文章から抽出された分析結果であり、実際のシステム変更や処理の実行を意味しない。

---

## 1. Purpose

本仕様の目的は、Structural DNA（S-DNA）が使用する構造変換演算子の意味を明確化することである。

これにより、以下の問題を軽減する。

- 単なるキーワード一致による誤分類
- 話題の類似性と構造の類似性の混同
- 変換方向の取り違え
- 演算子間の意味の重複
- 根拠のない構造解釈
- 分析モデルごとの語彙の不一致
- 構造の変化と改善の混同

本仕様は、あらゆる思考を有限個の演算子へ還元できると主張するものではない。

---

## 2. Normative Language

本仕様では、以下を使用する。

- MUST：必須
- MUST NOT：禁止
- SHOULD：推奨
- SHOULD NOT：非推奨
- MAY：任意

本仕様は設計段階の共通語彙を定義する。

各演算子の機械判定能力や分類精度が検証されたことを意味しない。

---

## 3. Structural Transformation Unit

### 3.1 Basic Definition

構造変換の基本単位を次のように定義する。

`T = (Source, Trigger, Operator, Target, Evidence)`

各要素の意味は以下のとおり。

| Element | Meaning |
|---|---|
| Source | 変換前の構造状態 |
| Trigger | 変換を必要とする条件・契機 |
| Operator | 変換操作 |
| Target | 変換後の構造状態 |
| Evidence | 変換解釈を裏付ける根拠 |

### 3.2 Structural State

Structural Stateは、ある時点または仮定された条件における構造の状態を表す。

例：

- `centralized-control`
- `distributed-autonomy`
- `linear-processing`
- `circular-processing`
- `fragmented-components`
- `coordinated-network`

状態名は、その状態が良いか悪いかを意味しない。

### 3.3 Trigger

Triggerは、構造変換を提案する理由や条件を表す。

例：

- `concentration-risk`
- `capacity-limit`
- `coordination-failure`
- `feedback-absence`
- `resource-imbalance`
- `environmental-change`

Triggerは、変換が成功したことを保証しない。

### 3.4 Operator

Operatorは、構造に対して提案または観測された操作を表す。

演算子は、構造状態そのものと区別しなければならない（MUST）。

### 3.5 Target State

Target Stateは、変換が意図する構造状態を表す。

提案された目標状態と、実際に観測された結果を同一視してはならない（MUST NOT）。

### 3.6 Evidence

Evidenceは、当該変換を認識した根拠である。

各分析結果は、元の問いまたは関連資料への参照を保持しなければならない（MUST）。

---

## 4. Vocabulary Design Principles

### 4.1 Meaning Before Labels

演算子の名称よりも、操作の意味を優先する。

### 4.2 Direction Matters

変換方向を区別する。

`centralize` と `distribute` は、通常は異なる方向の操作である。

ただし、両者を常に完全な逆演算とみなしてはならない。

### 4.3 Context Matters

同じ演算子でも、対象領域によって具体的な意味が異なる。

例：

- AIネットワークの分散
- 組織権限の分散
- 経済資源の分散

これらは同一の実装を意味しない。

### 4.4 No Automatic Value Judgment

分散、循環、単純化などを無条件に望ましい変換と判断してはならない。

### 4.5 Multiple Operators

一つの問いに複数の演算子を割り当ててもよい（MAY）。

ただし、それぞれの演算子について根拠を区別する。

### 4.6 Unresolved Classification

適切な演算子を特定できない場合、分析結果を未解決として扱うことを推奨する（SHOULD）。

根拠不足を、確信度の高い分類結果へ変換してはならない（MUST NOT）。

---

## 5. Core Operator Registry

S-DNA v0.1では、以下の12種類を初期演算子として定義する。

| Operator ID | Operator | Primary Function |
|---|---|---|
| OP-001 | `detect_limit` | 限界・制約の検出 |
| OP-002 | `distribute` | 集中構造の分散 |
| OP-003 | `centralize` | 分散構造の集中 |
| OP-004 | `connect` | 独立要素の接続 |
| OP-005 | `separate` | 結合要素の分離 |
| OP-006 | `circulate` | 処理・資源・情報の循環化 |
| OP-007 | `regulate` | 状態・負荷の調整 |
| OP-008 | `reverse` | 方向・関係の反転 |
| OP-009 | `simplify` | 構造の単純化 |
| OP-010 | `combine` | 複数構造の統合・合成 |
| OP-011 | `stabilize` | 状態変動の抑制・安定化 |
| OP-012 | `preserve` | 既存構造の維持 |

演算子IDはv0.1内で一意とする。

定義済みIDを、将来別の意味へ再利用してはならない（MUST NOT）。

---

## 6. Operator Definitions

### 6.1 OP-001 — detect_limit

**Definition**

対象構造に存在する限界、制約、矛盾、過負荷などを識別する操作。

**Typical Preconditions**

- 分析対象となる既存構造がある。
- 構造の制約や問題についての根拠がある。

**Expected Transformation**

構造が、制約未特定の状態から、制約を明示的に認識した状態へ移行する。

**Example**

「中央集権的なAIネットワークは、単一障害点に弱いのではないか？」

**Non-example**

「中央集権的なAIネットワークとは何か？」

後者は概念の説明を求めているだけであり、限界検出を提案しているとは限らない。

**Caution**

問題が指摘されていても、その指摘が正しいことを保証しない。

---

### 6.2 OP-002 — distribute

**Definition**

集中した権限、機能、資源、処理などを複数の構成要素へ分配する操作。

**Typical Preconditions**

- 集中した対象が存在する。
- 分配先または分配方針が想定される。

**Expected Transformation**

`centralized-control → distributed-autonomy`

**Example**

「単一のAI管理者に集中した判断を、複数の専門AIへ分担できないか？」

**Non-example**

「AI管理者を10台のサーバーで動かすには？」

サーバー数の増加だけでは、権限や機能が構造的に分散したとは限らない。

**Caution**

物理的な複製と、論理的な権限分散を区別する。

---

### 6.3 OP-003 — centralize

**Definition**

分散した権限、機能、情報、処理などを、一つまたは少数の中心へ集約する操作。

**Typical Preconditions**

- 複数の構成要素が存在する。
- 集約対象と中心となる機能が識別される。

**Expected Transformation**

`distributed-functions → centralized-coordination`

**Example**

「緊急時だけ、分散したAI群の停止判断を中央の安全管理層へ集約できないか？」

**Non-example**

「AI同士で情報を共有できないか？」

情報共有だけでは、権限の集中を意味しない。

**Caution**

集中化を、常に自由の喪失や安全性の低下と判断しない。

---

### 6.4 OP-004 — connect

**Definition**

独立または分離された構成要素の間に、新しい関係や通信経路を形成する操作。

**Typical Preconditions**

- 接続対象が複数存在する。
- 接続に意味または目的がある。

**Expected Transformation**

`isolated-components → connected-components`

**Example**

「独立したAIエージェントの監査記録を、共通の来歴参照で接続できないか？」

**Non-example**

「二つのAIは似た回答を生成するのか？」

出力の類似だけでは、接続関係は成立しない。

**Caution**

接続は、権限の共有や信頼の成立を自動的に意味しない。

---

### 6.5 OP-005 — separate

**Definition**

結合している機能、権限、責任、情報などを独立した部分へ分ける操作。

**Typical Preconditions**

- 分離可能な結合構造がある。
- 分離する対象が明確である。

**Expected Transformation**

`coupled-functions → separated-functions`

**Example**

「AIの推論能力と、外部システムを操作する権限を分離できないか？」

**Non-example**

「異なるAIモデルを比較するには？」

比較だけでは、既存の結合構造を分離していない。

**Caution**

分離後の相互作用が不要になるとは限らない。

---

### 6.6 OP-006 — circulate

**Definition**

情報、資源、価値、制御信号などの流れを、再接続、反復、帰還を含む循環構造へ変換する操作。

**Typical Preconditions**

- 流れの対象がある。
- 帰還または再循環の経路が想定される。

**Expected Transformation**

`linear-flow → feedback-or-circulation-flow`

**Example**

「AIが得た価値の一部を、貢献した人間へ戻す循環構造を作れないか？」

**Non-example**

「AIから人間へ報酬を一度支払うには？」

単発の一方向送金だけでは、循環の成立を意味しない。

**Caution**

循環と無限ループは異なる。

循環構造には停止条件、流量制限、責任境界などが必要になる場合がある。

---

### 6.7 OP-007 — regulate

**Definition**

状態、負荷、流量、振る舞いなどを、条件や観測結果に応じて調整する操作。

**Typical Preconditions**

- 調整対象となる状態が存在する。
- 調整の条件または基準がある。

**Expected Transformation**

`unregulated-operation → condition-dependent-operation`

**Example**

「AIネットワークの負荷に応じて、集中と分散の度合いを自動調整できないか？」

**Non-example**

「AIネットワークの処理速度を上げられないか？」

単純な性能向上だけでは、状態依存の調整を意味しない。

**Caution**

調整機能の存在は、安全性や安定性を保証しない。

---

### 6.8 OP-008 — reverse

**Definition**

構造内の方向、順序、作用関係などを反転させる操作。

**Typical Preconditions**

- 反転対象となる方向性がある。
- 何が反転するかが明確である。

**Expected Transformation**

`direction-A → direction-B`

ただし、BはAと反対の方向を表す。

**Example**

「外部圧力を単に防御するのではなく、その圧力から学習情報を獲得できないか？」

この例では、防御対象だった外圧を情報源として利用する方向転換を表す。

**Non-example**

「AIの処理速度を落とすには？」

数値が減少するだけでは、構造上の反転とは限らない。

**Caution**

反転を元の状態への完全な復元と同一視しない。

---

### 6.9 OP-009 — simplify

**Definition**

不要な構成要素、関係、処理段階などを削除・統合・抽象化し、構造の複雑性を低減する操作。

**Typical Preconditions**

- 複数の構成要素や関係がある。
- 簡略化対象が識別できる。

**Expected Transformation**

`complex-structure → reduced-complexity-structure`

**Example**

「複数のAI認可処理を、共通の権限境界に整理できないか？」

**Non-example**

「説明文を短くできないか？」

文章の短縮だけでは、対象システムの構造が簡略化されたとは限らない。

**Caution**

単純化によって重要な機能や安全条件が失われる場合がある。

---

### 6.10 OP-010 — combine

**Definition**

複数の構造、機能、規則などを組み合わせ、新しい複合構造を形成する操作。

**Typical Preconditions**

- 複数の構成要素が存在する。
- 統合先となる関係が提示される。

**Expected Transformation**

`structure-A + structure-B → composite-structure`

**Example**

「問い活の貢献記録とAIエージェントの決済記録を、共通の来歴構造へ接続して統合できないか？」

**Non-example**

「二つのプロトコルの特徴を比較したい」

比較だけでは、新しい複合構造の形成を意味しない。

**Caution**

統合によって、元の構造の意味、権限、同意範囲を失わせてはならない。

---

### 6.11 OP-011 — stabilize

**Definition**

構造状態の変動、振動、異常な偏りなどを抑え、指定された安定条件を維持しようとする操作。

**Typical Preconditions**

- 変動する状態がある。
- 安定条件または許容範囲がある。

**Expected Transformation**

`unstable-operation → bounded-operation`

**Example**

「AI群の負荷変動が大きい場合、出力能力を制限して動作状態を安定させられないか？」

**Non-example**

「AIの出力を常に一定値へ固定するには？」

固定化が必ずしも適切な安定化になるとは限らない。

**Caution**

安定化と固定化を区別する。

安定状態は動的に維持される場合もある。

---

### 6.12 OP-012 — preserve

**Definition**

外部条件や周辺構造が変化しても、指定された重要な構造要素または制約を維持する操作。

**Typical Preconditions**

- 保持すべき対象がある。
- 対象に影響する変更または外部条件がある。

**Expected Transformation**

`changing-environment + protected-invariant → preserved-invariant`

**Example**

「AIモデルが更新されても、人間の問いの来歴と同意記録を保持できないか？」

**Non-example**

「既存システムを何も変更したくない」

変更しないという希望だけでは、変動下で守るべき構造的不変条件が示されているとは限らない。

**Caution**

維持する対象と、変更を許容する対象を明確にする。

---

## 7. Operator Relationships

### 7.1 Opposing Operations

以下の演算子には、方向的な対比がある。

| Operator A | Operator B | Relationship |
|---|---|---|
| `distribute` | `centralize` | 分散と集中 |
| `connect` | `separate` | 接続と分離 |
| `combine` | `simplify` | 複合化と簡略化の一部 |
| `regulate` | `preserve` | 状態調整と不変条件の保持 |

これらは概念上の対比であり、必ずしも数学的な逆演算ではない。

### 7.2 Complementary Operations

一つの問いでは、複数の演算子が補完的に働く場合がある。

例：

`detect_limit → distribute → connect → regulate`

この系列は、集中構造の限界を認識し、機能を分散し、接続を確保し、全体を調整するという操作の流れを表す。

### 7.3 Conditional Operations

条件によって異なる演算子を選択する場合がある。

例：

- 平常時：`distribute`
- 異常時：`centralize`
- 回復後：`distribute`
- 全過程：`regulate`

この例は、中央集権と分散の切り替えを、状態依存の制御として表現する。

ただし、実際に安全に切り替えられるかどうかは、本語彙仕様の検証範囲外である。

---

## 8. Operator Composition

### 8.1 Composition Definition

複数の演算子を連続的に適用する構造を、Operator Compositionと呼ぶ。

概念表現：

`T1 → T2 → T3`

### 8.2 Sequential Composition

先行する変換の出力が、後続の変換の入力に対応する場合、連続変換として表現できる。

例：

`centralized → distributed → interconnected`

### 8.3 Parallel Composition

複数の変換が、共通の構造に対して並列に提案される場合がある。

例：

- 権限の分散
- 監査記録の接続
- 負荷の調整

これらを、必ずしも直列の実行順序へ変換してはならない。

### 8.4 Circular Composition

複数の操作が循環的な関係を形成する場合がある。

例：

`observe → regulate → act → observe`

概念上の循環は、無制限な実行を許可するものではない。

### 8.5 Composition Validity

演算子同士を接続する場合、変換元・変換先の状態が意味的に整合する必要がある。

整合性を確認できない接続は、未解決として扱うことを推奨する。

---

## 9. Classification Rules

### 9.1 Evidence-Based Classification

演算子の分類には、問いの内容に関する根拠が必要である。

分類記録は、根拠を参照できなければならない（MUST）。

### 9.2 No Keyword-Only Classification

特定の単語が現れたことだけを理由に演算子を確定してはならない（MUST NOT）。

例えば「循環」という単語が登場しても、構造的な帰還経路が示されていなければ、`circulate` を確定できない場合がある。

### 9.3 Transformation Direction

変換元と変換先を入れ替えると意味が変わる場合、方向を明示しなければならない（MUST）。

### 9.4 Multiple Interpretations

同一の問いに対して、複数の演算子解釈を認める。

競合する解釈が存在する場合、それぞれの根拠を記録することを推奨する。

### 9.5 No Unsupported Completion

問いに明示されていない変換を、分析者の期待だけで追加してはならない（MUST NOT）。

例えば、分散化を提案する問いに対し、循環化や自己調律を必ず追加してはならない。

---

## 10. Ambiguity and Unresolved Cases

演算子分類が困難な場合、以下を区別する。

| Condition | Treatment |
|---|---|
| 根拠が十分 | 分類候補を提示 |
| 複数の解釈が成立 | 複数候補を保持 |
| 根拠が不足 | UNRESOLVED |
| 変換方向が不明 | UNRESOLVED |
| 演算子が未定義 | 語彙拡張候補 |
| 根拠と分類が矛盾 | FAIL候補 |

UNRESOLVEDは、問いの価値がないことを意味しない。

分類できない問いを、不適切な問いとして扱ってはならない。

---

## 11. Conceptual Operator Record

演算子分析記録の概念例を以下に示す。

```json
{
  "vocabulary_version": "0.1.0",
  "analysis_id": "sdna-vocab-analysis-001",
  "question_ref": "question-example-001",
  "transformations": [
    {
      "transformation_id": "transformation-001",
      "source_state": "centralized-control",
      "trigger": "concentration-risk",
      "operator_id": "OP-002",
      "operator": "distribute",
      "target_state": "distributed-autonomy",
      "evidence_refs": [
        "question-span:001"
      ]
    },
    {
      "transformation_id": "transformation-002",
      "source_state": "distributed-autonomy",
      "trigger": "coordination-need",
      "operator_id": "OP-004",
      "operator": "connect",
      "target_state": "coordinated-network",
      "evidence_refs": [
        "question-span:002"
      ]
    }
  ],
  "classification_status": "proposed"
}
```

このJSONは概念例であり、正式なJSON Schemaへの適合性を保証するものではない。

`question-span`参照方式、IDの形式、分析主体、時刻、重複処理などは将来のSchemaで定義する。

---

## 12. Structural Similarity

S-DNAでは、演算子の類似性を構造比較の一要素として使用できる。

ただし、同じ演算子が含まれていても、問い全体が同一の構造であるとは限らない。

### 12.1 Comparison Dimensions

- 演算子の一致
- 変換元状態の対応
- 変換先状態の対応
- 変換方向
- 演算子の順序
- 演算子間の関係
- 根拠の妥当性

### 12.2 Similarity Limitations

演算子の一致だけで、以下を判断してはならない（MUST NOT）。

- 同一人物による創作
- 直接的な模倣
- 歴史的な影響関係
- 知的所有権
- 貢献度
- 報酬資格

構造の類似性は、独立した来歴証拠の代替にはならない。

---

## 13. Operator Change and Structural Evolution

構造分析の時系列変化を、以下のように分類する。

### 13.1 Addition

新しい演算子が追加される。

例：

`distribute → connect`

から、

`distribute → connect → regulate`

への変化。

### 13.2 Removal

既存の演算子が削除される。

削除を、思考能力の低下と判断してはならない。

### 13.3 Replacement

演算子が別の演算子へ置き換えられる。

例：

`centralize` から `distribute` への変更。

### 13.4 Reordering

演算子の順序が変更される。

例：

`connect → regulate`

から、

`regulate → connect`

への変更。

### 13.5 Recombination

異なる問いから得られた構造変換系列が組み合わされる。

### 13.6 Convergence

異なる経路で形成された問いが、類似する演算子構成へ到達する。

ただし、類似した分析結果だけでは、実際の歴史的収束や独立性を証明できない。

### 13.7 No Automatic Progress Judgment

演算子の数、種類、系列の長さ、複雑性によって、思考の進歩を自動判定してはならない。

---

## 14. Interoperability

### 14.1 Structural DNA

本仕様は、Structural DNA Specification v0.1で定義した変換モデルを補足する。

基本仕様と本仕様の間に規範上の矛盾がある場合、矛盾を明示して解決する。

### 14.2 Toikatsu Protocol

Toikatsuは問いの登録、活動、同意、貢献、検証、handoffを扱う。

本語彙仕様は、問いに含まれる構造変換を記述する。

演算子分類は、Toikatsuの貢献評価を自動的に変更しない。

### 14.3 Person-Provenance

演算子の組み合わせを、本人認証や個人識別に利用してはならない。

### 14.4 Structural Lineage

演算子の追加、削除、置換、融合などは、構造変化の候補情報として利用できる。

実際の派生関係を主張するには、別途来歴証拠を必要とする。

### 14.5 TIB

外部システムへ構造分析を引き渡す場合、Reference・Semantic・Authority・Valueの境界を尊重する。

演算子分類の結果を、実行権限や所有権へ自動変換してはならない。

### 14.6 Royalty OS

本語彙仕様は、価値の起源や構造変化を調べる補助情報となり得る。

ただし、演算子の類似性や新規性だけで分配対象や分配率を決めてはならない。

---

## 15. Privacy and Human Agency

本仕様に基づく分析結果は、問いを記述するものであり、人物を固定的に分類するものではない。

### 15.1 Non-Identity Rule

構造変換の類似性を本人認証として使用してはならない（MUST NOT）。

### 15.2 Consent

個人に紐づく継続分析、外部共有、公開利用には、適切な同意と目的の明確化が必要である。

### 15.3 Withdrawal

同意撤回後は、適用される同意条件に従って、新たな分析や外部共有を停止する。

### 15.4 No Covert Profiling

本人の認識や適切な同意なく、長期的な思考パターンの追跡による人物プロファイルを構築してはならない（MUST NOT）。

### 15.5 Interpretive Freedom

一つの問いに複数の解釈を認める。

分析結果を、本人の思考の唯一の正しい表現として押し付けてはならない。

---

## 16. Validation Requirements

将来のValidatorは、以下の観点を検査する。

### 16.1 Formal Validation

- 語彙バージョンの存在
- 演算子IDの妥当性
- 演算子名との対応
- 必須フィールド
- データ型
- 根拠参照の形式
- 重複識別子

### 16.2 Semantic Validation

- 変換前後の意味的整合
- 演算子と変換方向の対応
- 分類根拠の存在
- 演算子の不正な追加
- 話題の一致と構造の一致の混同
- 類似性と派生関係の混同
- 既存記録の無断変更
- 同意条件との整合性

### 16.3 Validation Outcomes

将来の検証結果は、原則として以下を区別する。

- `PASS`
- `FAIL`
- `UNRESOLVED`

形式的なPASSは、分類の意味的な正しさを保証しない。

意味的なPASSは、歴史的な起源や貢献価値を証明しない。

---

## 17. Minimum Test Cases

### 17.1 Positive Cases

- `detect-limit-from-concentration`
- `distribute-control`
- `centralize-emergency-authority`
- `connect-independent-agents`
- `separate-inference-and-authority`
- `circulate-value-flow`
- `regulate-load`
- `reverse-external-pressure`
- `simplify-authorization`
- `combine-provenance-records`
- `stabilize-agent-operation`
- `preserve-question-origin`
- `compose-distribute-connect-regulate`
- `conditional-centralize-distribute`
- `multiple-valid-interpretations`

### 17.2 Negative Cases

- `keyword-only-classification`
- `operator-direction-mismatch`
- `missing-transformation-evidence`
- `unknown-operator-id`
- `operator-name-id-mismatch`
- `unsupported-operator-addition`
- `invalid-composition`
- `similarity-as-identity`
- `similarity-as-lineage`
- `classification-as-ownership`
- `classification-as-payment-entitlement`
- `unauthorized-longitudinal-profiling`

### 17.3 Unresolved Cases

- `ambiguous-transformation-direction`
- `insufficient-evidence`
- `competing-valid-operators`
- `undefined-transformation-pattern`
- `unclear-source-state`
- `unclear-target-state`

これらは将来の検証対象候補であり、現時点で実装済みのテストファイルを示すものではない。

---

## 18. Versioning Policy

### 18.1 Vocabulary Version

本仕様の初期バージョンを `0.1.0` とする。

### 18.2 Operator Stability

公開済みの演算子IDを、異なる意味へ再利用してはならない（MUST NOT）。

### 18.3 Operator Addition

新しい演算子を追加する場合は、以下を記録する。

1. 演算子ID
2. 名称
3. 定義
4. 適用前提
5. 変換後の意味
6. 適用例
7. 誤分類例
8. 既存演算子との関係

### 18.4 Compatibility

語彙の変更が既存の分析結果に影響する場合、対応関係と互換性への影響を記録する。

### 18.5 No Silent Reinterpretation

過去の分析結果を、新しい語彙定義で無断に再解釈してはならない（MUST NOT）。

再分析する場合は、元の結果と新しい結果を区別できるようにする。

---

## 19. Implementation Status

本仕様は設計段階である。

以下は未実装とする。

- JSON Schema
- Operator Registryの機械可読形式
- 自動分類器
- 意味検証Validator
- PASS／FAIL／UNRESOLVEDサンプル
- 構造類似性評価器
- GitHub Actions

既存Toikatsu ProtocolのCI成功は、本語彙仕様の適合性を保証しない。

---

## 20. Completion Criteria

本仕様の設計段階の完了条件を以下とする。

1. 初期演算子の名称と意味を定義している。
2. 演算子ごとの適用前提を記録している。
3. 適用例と誤分類例を区別している。
4. 変換方向を明示している。
5. 演算子の合成条件を定義している。
6. 曖昧性と未解決状態を扱っている。
7. 構造類似性と人物同一性を分離している。
8. 構造変化と進歩の判断を分離している。
9. Toikatsu・TIBとの責任境界を明示している。
10. 未実装事項を明示している。

---

## 21. Closing Principle

構造を理解することは、単語を分類することではない。

それは、何が変わり、なぜ変わり、どのような関係が生まれたのかを理解することである。

中央集権から分散へ。

固定から流動へ。

一方向から循環へ。

制御から調律へ。

しかし、これらの変換に、あらかじめ優劣があるわけではない。

ある環境では分散が有効であり、別の環境では集中が必要になる。

ある場面では変化が必要であり、別の場面では維持が重要になる。

S-DNAの演算子は、その選択と変換を記述するために存在する。

人間の思考を固定するためではない。

人間が新しい構造を発見し、必要に応じて組み替えるためである。

**Meaning before labels.**

**Transformation before classification.**

**Evidence before attribution.**

**Human agency before automation.**

Structural Transformation Vocabulary v0.1

*構造を分類するのではなく、構造が変化する仕組みを記述する。*
