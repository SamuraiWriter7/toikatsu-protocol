# Structural DNA Specification v0.1

**S-DNA — 問いに含まれる構造変換を表現・比較・追跡するための共通仕様**

- Specification Version: `0.1.0`
- Specification ID: `SDNA-0.1`
- Status: Draft / Design Proposal
- Parent Repository: `toikatsu-protocol`
- Related Protocols: Toikatsu / Q Network / TIB
- Implementation Status: Not implemented

---

## 0. Fundamental Principle

**Structural DNA describes transformations, not identities.**

構造DNAは、人間の身元ではなく、問いに含まれる構造変換を表現する。

Structural DNA（以下S-DNA）は、人間またはAIが生成した問いに含まれる、対象分野に依存しない構造要素、関係性、変換規則を抽出し、比較・追跡可能な形式で表現するための仕様である。

本仕様の目的は、人間を固定的な思考類型に分類することではない。

問いがどのような構造から生まれ、どのような変換を提案し、どのように変化したかを観測することである。

S-DNAは次の原則に従う。

1. 構造の類似性は、同一人物の証明ではない。
2. 構造の類似性は、創造的起源の証明ではない。
3. 構造の変化は、必ずしも進歩を意味しない。
4. 問いの分析結果は、元の問いを置き換えない。
5. 推定された関係と、記録で裏付けられた関係を区別する。
6. 分析結果だけで、権利や報酬資格を確定しない。
7. 人間の同意と主体性を維持する。

---

## 1. Purpose

S-DNAは、異なる分野の問いに共通して現れる構造変換を記録することを目的とする。

例えば、以下の問いは対象領域が異なる。

- AIの中央集権的な構造を分散できるか。
- 国家制度の権限集中を緩和できるか。
- 地域経済の一極集中を循環型に転換できるか。

しかし、これらには共通する構造変換が含まれる可能性がある。

```text
Centralization
      |
      v
Limit Detection
      |
      v
Distribution
      |
      v
Circulation
      |
      v
Self-Regulation
```

S-DNAは、このような構造上の共通性と差異を記録する。

ただし、共通性が存在すると判断するには、元の問いに含まれる根拠を示さなければならない。

---

## 2. Normative Language

本仕様では次の用語を使用する。

- MUST：必須
- MUST NOT：禁止
- SHOULD：推奨
- SHOULD NOT：非推奨
- MAY：任意

本書は設計仕様であり、S-DNAの完全な自動分析能力が実装・検証されたことを意味しない。

---

## 3. Scope

### 3.1 Included

v0.1は以下を対象とする。

1. 問いの構造要素の抽出
2. 構造変換規則の表現
3. 構造系列の記録
4. 構造グラフの概念表現
5. 構造類似性の分析条件
6. 構造変異の分類
7. 構造融合・構造収束の区別
8. 分析根拠の参照
9. Toikatsuとの接続境界
10. 同意とプライバシーの保護

### 3.2 Excluded

以下はv0.1の対象外とする。

- 個人の身元認証
- 生体認証
- 匿名ユーザーの再識別
- 人物の性格や能力の自動判定
- 思想的傾向による人物格付け
- 著作権や所有権の自動確定
- 問いの最初の発案者の証明
- 貢献度や報酬額の自動決定
- 思考の優劣の普遍的な数値評価
- AI内部の推論過程の完全な再現

---

## 4. Structural Transformation Model

### 4.1 Definition

S-DNAの基本単位は、構造変換である。

一つの構造変換は、原則として以下の要素から構成する。

| Field | Meaning |
|---|---|
| `source_state` | 変換前の構造状態 |
| `trigger` | 変換の契機となる条件 |
| `operator` | 構造変換の操作 |
| `target_state` | 変換後の構造状態 |
| `evidence_refs` | 分析根拠への参照 |

### 4.2 Transformation Expression

概念的には次の形式とする。

```text
T = (Source, Trigger, Operator, Target, Evidence)
```

変換を次のように表現できる。

```text
Source State
      |
      v
Trigger Detection
      |
      v
Transformation Operator
      |
      v
Target State
```

この表現は、問いに含まれる提案や問題設定を記録するものである。

実際に変換が実行されたことを意味しない。

### 4.3 Evidence Requirement

各構造変換には、元の問い、関連資料、または分析対象の記録への参照を持たせなければならない（MUST）。

分析者は、根拠を示せない変換を確定した分析結果として扱ってはならない（MUST NOT）。

---

## 5. Structural Vocabulary

v0.1では、説明用の基本語彙として以下を定義する。

| Code | Name | Description |
|---|---|---|
| H | Hierarchy | 階層・集中・固定された構造 |
| L | Limit Detection | 限界・矛盾・制約の検出 |
| D | Distribution | 分散・役割分担・自律性 |
| C | Circulation | 循環・再接続・還流 |
| S | Self-Regulation | 自己調整・負荷制御・安定化 |

### 5.1 Example Sequence

```text
H → L → D → C → S
```

この系列は、構造変換の一例である。

すべての問いがこの順序で変化する必要はない。

### 5.2 Non-Canonical Vocabulary

H・L・D・C・Sは初期語彙であり、自然界や人間の思考に普遍的な基本単位として証明されたものではない。

分析実装は、語彙定義のバージョンを明示すべきである（SHOULD）。

異なる語彙体系を利用する場合、その対応関係を別途記録する。

---

## 6. Transformation Operators

S-DNAでは、構造状態よりも変換操作を重視する。

v0.1の候補演算子を以下に定義する。

| Operator | Purpose |
|---|---|
| `detect_limit` | 制約・矛盾・限界を発見する |
| `distribute` | 集中した機能を分散する |
| `centralize` | 分散した機能を集中する |
| `connect` | 独立した構造を接続する |
| `separate` | 結合した構造を分離する |
| `circulate` | 一方向の処理を循環へ変える |
| `regulate` | 状態や負荷を調整する |
| `reverse` | 変換方向を反転する |
| `simplify` | 構造を単純化する |
| `combine` | 複数の構造を組み合わせる |
| `stabilize` | 状態を安定化する |
| `preserve` | 既存の構造を維持する |

これらの演算子は、分析用の記述語彙であり、実行可能なプログラム命令ではない。

### 6.1 Operator Rules

- 演算子は分析上の意味を持たなければならない（MUST）。
- 演算子だけから変換前後の状態を推定してはならない（MUST NOT）。
- 根拠なしに変換を補完してはならない（MUST NOT）。
- 分析対象に適切な演算子がない場合は、未解決として扱ってよい（MAY）。
- 新しい演算子を追加する際は、その意味とバージョンを記録すべきである（SHOULD）。

---

## 7. Structural Representations

S-DNAは、次の三種類の表現を区別する。

### 7.1 Structural Sequence

問いに含まれる変換の順序や系列を表す。

```text
H → L → D → C → S
```

系列は人間にとって理解しやすい。

ただし、複雑な分岐や並列関係を完全に表現できるとは限らない。

### 7.2 Structural Graph

構造の分岐、合流、循環、逆方向の関係を表す。

```text
             Distribution
            /            \
Hierarchy --              --> Circulation
            \            /
             Centralization
                    |
                    v
              Self-Regulation
```

グラフでは、ノードと関係を識別可能にすることを推奨する（SHOULD）。

循環構造を表現する場合も、無制限な再帰実行を意味しない。

### 7.3 Structural Embedding

問いや構造変換を、数値ベクトルとして表現する方法である。

主な用途は以下とする。

- 類似する問いの候補検索
- 大量の問いの探索
- 構造上の近傍候補の抽出
- 分析対象の絞り込み

埋め込みベクトルの近さだけで、構造的同一性や影響関係を確定してはならない（MUST NOT）。

### 7.4 Representation Separation

Sequence、Graph、Embeddingは互いに異なる表現である。

一方の表現から他方への変換で失われる情報がある場合、その損失を明示すべきである（SHOULD）。

---

## 8. Conceptual Record Model

v0.1では、構造分析記録の概念モデルを定義する。

```json
{
  "sdna_version": "0.1.0",
  "analysis_id": "sdna-analysis-001",
  "question_ref": "question-example-001",
  "analyzer": {
    "method_ref": "structural-classifier-v0.1",
    "model_ref": null
  },
  "transformations": [
    {
      "transformation_id": "transformation-001",
      "source_state": "centralized-control",
      "trigger": "concentration-risk",
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
      "operator": "circulate",
      "target_state": "coordinated-circulation",
      "evidence_refs": [
        "question-span:002"
      ]
    }
  ],
  "structural_sequence": [
    "H",
    "L",
    "D",
    "C"
  ],
  "confidence": null,
  "analysis_status": "proposed"
}
```

本記録は概念例であり、v0.1ではJSON Schemaによる形式検証を保証しない。

`question-span`の識別方式、分析主体の認証、分析時刻、グラフ形式、埋め込み形式などは今後定義する。

### 8.1 Source Preservation

S-DNA分析は、元のToikatsu Recordを変更してはならない（MUST NOT）。

分析結果は、元の問いを参照する独立した記録として保持する。

### 8.2 Analysis Status

分析記録の候補状態は以下とする。

- `proposed` — 分析結果の候補
- `reviewed` — 指定された方法による確認済み
- `rejected` — 当該分析結果を不採用
- `unresolved` — 根拠不足などで判断不能

`reviewed`は、問いの創造的起源や社会的価値を証明するものではない。

---

## 9. Structural Similarity

### 9.1 Definition

構造類似性とは、二つ以上の問いに含まれる構造状態、変換規則、関係性などの対応を分析した結果である。

### 9.2 Similarity Dimensions

少なくとも以下の観点を区別する。

| Dimension | Description |
|---|---|
| State Similarity | 構造状態の類似 |
| Operator Similarity | 変換操作の類似 |
| Direction Similarity | 変換方向の類似 |
| Graph Similarity | 構造関係の類似 |
| Context Similarity | 話題・文脈の類似 |

構造類似性と話題の類似性は、同一の尺度として扱わない。

### 9.3 Similarity Is Not Lineage

構造類似性だけから、以下を断定してはならない（MUST NOT）。

- 同じ人物が生成した
- 一方が他方を模倣した
- 一方が他方から派生した
- 同じ知的起源を持つ
- 同じ権利者に帰属する

類似性は、追加調査のための候補情報として扱う。

---

## 10. Structural Change

S-DNAでは、異なる時点または異なる問いの間で、構造がどのように変化したかを記録できる。

### 10.1 Structural Mutation

Structural Mutationは、構造要素または変換規則の追加、削除、置換、方向変更などを指す。

例：

```text
Generation 1

H → L → D

Generation 2

H → L → D → C

Generation 3

H → L → D → C → S
```

この例は説明上の系列であり、同一人物による時間的発展が確認されたことを意味しない。

### 10.2 Structural Recombination

Structural Recombinationは、複数の問いの構造要素や変換規則が組み合わされ、新しい構造を形成することを指す。

実際の派生関係を主張する場合は、引用、編集履歴、共同作業記録などの根拠が必要である。

### 10.3 Structural Convergence

Structural Convergenceは、異なる問いが類似した構造へ到達する現象を指す。

収束は、直接的な影響関係が存在することを意味しない。

### 10.4 Structural Simplification

変換規則の削除、統合、抽象化によって構造が単純化する場合がある。

複雑性の増加を、構造的進歩と同一視してはならない（MUST NOT）。

### 10.5 Change Is Not Improvement

構造の変化と、問題解決能力の改善を区別する。

改善を主張する場合は、別途定義された評価基準と証拠が必要となる。

---

## 11. Structural Lineage

### 11.1 Definition

Structural Lineageは、問いの構造分析結果同士の関係を記録する概念である。

主な関係候補は以下とする。

- `derived_from`
- `revised_from`
- `combined_from`
- `similar_to`
- `convergent_with`

### 11.2 Relationship Classes

次の二種類を明確に分離する。

**Recorded Lineage**

文書、編集履歴、引用、共同作業記録などによって裏付けられた派生関係。

**Inferred Similarity**

構造分析によって推定された類似関係。

推定された類似性を、根拠なしに歴史的な派生関係へ昇格させてはならない（MUST NOT）。

### 11.3 Multiple Origins

一つの問いや構造は、複数の問い・活動・主体から影響を受ける場合がある。

S-DNAは、単一起源を必須としない。

複数の来歴や関係を記録できる構造が望ましい。

### 11.4 Cycles

構造グラフ上の循環は許容する。

一方、実際の時間的派生を表す関係は、確認された時間順序と矛盾してはならない。

構造上の循環と、歴史的来歴の循環を区別する。

---

## 12. Analysis Provenance

### 12.1 Purpose

S-DNAの分析結果自体にも来歴が必要である。

同じ問いに対して、異なる分析モデルや人間の分析者が、異なる構造解釈を提示する可能性があるためである。

### 12.2 Recommended Information

分析記録は、以下の情報を保持すべきである（SHOULD）。

- 分析対象の識別子
- 元記録の版またはハッシュ
- 分析方法とバージョン
- 分析モデルの識別子
- 分析日時
- 抽出した変換規則
- 根拠参照
- 分析結果の状態
- 検証またはレビュー履歴

### 12.3 No Absolute Interpretation

一つの問いに対して、複数の分析結果を認める。

異なる分析結果が存在することだけを理由に、一方を不正と判断してはならない。

分析間の不一致は、比較可能な形で保持することを推奨する。

---

## 13. Human Agency and Privacy

### 13.1 Non-Identity Principle

S-DNAを本人認証や生体認証の代替として使用してはならない（MUST NOT）。

構造の類似性を根拠として、匿名参加者の身元を特定してはならない（MUST NOT）。

### 13.2 No Fixed Personality Classification

S-DNA分析を、人間の人格、知能、能力、思想的価値の固定的な判定として扱ってはならない（MUST NOT）。

### 13.3 Consent

問いの分析、分析結果の公開、外部共有、継続的な追跡は、それぞれ適切な同意と利用目的の確認が必要である。

既存のToikatsu v0.1の同意範囲だけで、あらゆるS-DNA分析や人物横断的な追跡が自動的に許可されるわけではない。

### 13.4 Withdrawal

同意撤回後は、適用される方針に従って新しい分析や共有を停止する。

保持、削除、匿名化などの処理は、適用される同意条件と法令に従う。

### 13.5 No Covert Profiling

本人の認識や適切な同意なしに、S-DNAを用いて長期的な人物プロファイルを構築してはならない（MUST NOT）。

---

## 14. Interoperability Boundaries

### 14.1 Toikatsu Protocol

Toikatsuは、問いの登録、活動記録、同意、貢献候補、検証、handoffを扱う。

S-DNAは、問いの構造分析を扱う。

S-DNA分析は、Toikatsuの貢献検証結果を自動的に変更しない。

### 14.2 Q Network

Q Networkは問いの派生・来歴・構造変化などを扱う。

S-DNAは、問いに含まれる変換規則を追加的な分析情報として提供できる。

正式なフィールド対応や相互運用性は別途定義する。

### 14.3 TIB

TIBは、S-DNAの分析結果を外部システムへ接続する際の境界条件を扱う。

次の原則を維持する。

- Reference is not Authority.
- Similarity is not Identity.
- Lineage is not Ownership.
- Verification is not Entitlement.

### 14.4 Person-Provenance

Person-Provenanceは、提出主体や提出行為の来歴を扱う。

S-DNAは、その人物の身元を証明しない。

両者を接続する場合、主体識別と構造分析を独立した情報として保持する。

### 14.5 Machine Provenance

AIによる推論の検証証拠は、外部参照として関連付けてもよい。

ただし、モデル推論の証明を、S-DNAの構造解釈の正しさの証明として扱ってはならない。

### 14.6 Royalty OS

S-DNAの類似性、変異、系譜に関する情報だけで、貢献度、権利帰属、報酬資格、分配率を決定してはならない（MUST NOT）。

価値帰属や還流の判断は、独立した根拠、制度、契約、検証を必要とする。

---

## 15. Validation Principles

### 15.1 Structural Validation

将来のJSON Schemaでは、主に以下を確認する。

- 必須フィールド
- データ型
- バージョン
- 状態の列挙値
- 参照の形式
- 変換レコードの構造

### 15.2 Semantic Validation

意味検証では、以下を対象とする。

1. 変換元と変換先の関係
2. 演算子の定義と整合性
3. 根拠参照の存在
4. 系列とグラフの対応
5. 分析方法の識別
6. 根拠のない状態昇格
7. 類似性と派生関係の混同
8. 身元認証への不正な転用
9. 貢献認定への不正な転用
10. 同意範囲との整合性

### 15.3 Validation Outcomes

将来の分析・境界検証では、以下を区別することを推奨する。

- `PASS`
- `FAIL`
- `UNRESOLVED`

根拠不足によるUNRESOLVEDを、根拠のあるPASSへ自動変換してはならない。

### 15.4 Operational Limits

形式検証に成功しても、次の事項は保証されない。

- 分析された変換が唯一の正しい解釈であること
- 元の問いが独創的であること
- 記録された系譜が歴史的に完全であること
- 思考の変化が人間の能力向上を意味すること
- 類似する構造が同じ人物によって生成されたこと

---

## 16. Minimum Test Coverage

将来の実装では、少なくとも次のテストを推奨する。

### Positive Cases

- 単一の構造変換
- 複数の連続変換
- 構造変換の分岐
- 構造変換の合流
- 逆方向の変換
- 構造の単純化
- 異分野間の構造類似
- 不明な構造のUNRESOLVED処理
- 複数分析結果の併存
- 根拠付きの構造派生

### Negative Cases

- 根拠のない構造変換
- 未定義の演算子
- 構造系列と参照の不整合
- 類似性を派生関係と断定
- 構造類似性を身元証明として利用
- 構造分析を所有権証明として利用
- 構造分析を支払承認として利用
- 同意範囲外の継続分析
- 分析結果による元記録の改変
- 実際の時間的来歴と矛盾する派生関係

---

## 17. Implementation Policy

v0.1では、構造設計を先行する。

以下は未実装とする。

- S-DNA JSON Schema
- 自動構造分類器
- Structural Graph Schema
- Structural Embedding Model
- Structural Lineage Validator
- PASS／FAILテストデータ
- S-DNA専用GitHub Actions

既存のToikatsu v0.1のGitHub Actions通過は、S-DNAの適合性を証明しない。

実装段階へ進む場合は、構造表現の曖昧さと検証可能性を先に確認する。

---

## 18. Future Extensions

将来の拡張候補には以下がある。

### Structural Analysis

- 演算子語彙の体系化
- 分析結果の版管理
- 複数分析者による比較
- 構造解釈の不一致管理

### Structural Lineage

- 来歴グラフのスキーマ化
- 変異と融合の記録
- 独立収束の分析
- 複数主体の派生関係

### Privacy

- プライバシー保護型構造検索
- 分析記録の撤回・削除
- 仮名化された来歴参照
- 人物プロファイリングの防止

### Interoperability

- Q Networkとのマッピング
- TIBによる接続境界検証
- Shared Traceとの証拠接続
- Knowledge Lineage Networkとの連携

これらは研究・設計候補であり、実装を約束するものではない。

---

## 19. Completion Criteria

S-DNA v0.1の設計段階の完了条件を以下とする。

1. 構造変換の基本単位を定義している。
2. 初期語彙と変換演算子を区別している。
3. Sequence・Graph・Embeddingの役割を区別している。
4. 類似性と実際の派生関係を区別している。
5. 構造変異・融合・収束を定義している。
6. 分析結果に根拠を要求している。
7. 元の問いの記録を保護している。
8. 本人認証や人物格付けへの転用を禁止している。
9. ToikatsuやTIBとの責任境界を明示している。
10. 実装済み事項と未実装事項を区別している。

これらは設計文書の完了条件であり、分析手法の科学的妥当性や実装の正確性を保証しない。

---

## 20. Closing Declaration

問いは、単なる文章ではない。

その背後には、問題の認識、限界の発見、構造の変換、新しい関係の形成など、さまざまな思考操作が存在する。

異なる分野の問いでも、共通する構造変換が現れることがある。

そして、その構造は固定的ではない。

新しい経験によって変化する。

他者の問いによって修正される。

異なる構造と結びつく。

ときには、より単純な形へ収束する。

Structural DNAは、それらの変化を記録するための設計である。

人間を固定的な型に分類するためではない。

人間が自らの問いを振り返り、新しい思考の可能性を発見するためである。

**Structure is not identity.**

**Similarity is not ownership.**

**Change is not automatically progress.**

**Lineage requires evidence.**

**Human agency remains primary.**

Structural DNA Specification v0.1

*問いの構造を記録し、思考の自由を守る。*
