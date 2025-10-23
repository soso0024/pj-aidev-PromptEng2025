# All Model Comparison with Claude 4.5 Haiku

このディレクトリには、`claude-haiku-4-5`のデータを含む全モデル比較プログラムが含まれています。

## 含まれるモデル

- Claude 3 Haiku (`claude-3-haiku`)
- Claude 3.5 Haiku (`claude-3-5-haiku`)
- **Claude 4.5 Haiku (`claude-haiku-4-5`)** ← NEW
- Claude 4 Sonnet (`claude-4-sonnet`)
- Claude 4.5 Sonnet (`claude-4-5-sonnet`)
- Claude 4.1 Opus (`claude-opus-4-1`)

## プログラム一覧

### 1. `best_model_comparison.py`

各モデルの最適構成をコスト効率（coverage per $0.001）に基づいて比較するスキャッタープロットを作成します。

**実行方法:**

```bash
python best_model_comparison.py
```

**出力:**

- `best_model_comparison.png`: モデルごとの最適構成を示すプロット

### 2. `input_tokens_comparison.py`

全モデル・全構成の平均入力トークン数を比較するグループ化バーチャートを作成します。

**実行方法:**

```bash
python input_tokens_comparison.py
```

**出力:**

- `input_tokens_comparison.png`: 入力トークン比較チャート

### 3. `pareto_front_analysis.py`

コスト vs 実効カバレッジ（Effective Coverage = Coverage × Success Rate / 100）のパレートフロンティア分析を実行します。

**実行方法:**

```bash
python pareto_front_analysis.py
```

**出力:**

- `pareto_front_cost_vs_effective_coverage.png`: パレート最適点を示すプロット

**注:** このプログラムでは、より見やすい視覚化のため、以下のモデルのみを対象としています：

- Claude 3.5 Haiku
- Claude 4.5 Haiku (NEW)
- Claude 4 Sonnet
- Claude 4.5 Sonnet

### 4. `comprehensive_table_generator.py`

全モデル・全構成の詳細な統計表を生成します。

**実行方法:**

```bash
python comprehensive_table_generator.py
```

**出力:**

- `comprehensive_summary_table.csv`: CSV 形式の統計表
- `comprehensive_summary_table.txt`: テキスト形式の統計表

## 全プログラムを実行

全てのプログラムを一度に実行する場合：

```bash
python best_model_comparison.py
python input_tokens_comparison.py
python pareto_front_analysis.py
python comprehensive_table_generator.py
```

## 元のフォルダとの違い

`../all_comparison/`と比較して、以下の変更が加えられています：

1. **新しいモデルの追加**: `claude-haiku-4-5`（Claude 4.5 Haiku）のデータが含まれています
2. **モデルフォーマットの更新**: `_format_model_name()`メソッドに新しいモデルのフォーマットが追加されています
3. **カラーマップの更新**: 新しいモデル用の色（Deep Pink: `#FF1493`）が追加されています
4. **凡例の更新**: 新しいモデルを含むように凡例の順序が更新されています

## 依存関係

このプログラムは以下のモジュールに依存しています：

- pandas
- matplotlib
- numpy
- seaborn (input_tokens_comparison.py のみ)
- 親ディレクトリの`analysis`モジュール（`data_loader.py`, `problem_classifier.py`）

## データソース

プログラムは以下のディレクトリからデータを自動的に読み込みます：

- `../data/generated_tests_claude-3-haiku/`
- `../data/generated_tests_claude-3-5-haiku/`
- `../data/generated_tests_claude-haiku-4-5/` ← NEW
- `../data/generated_tests_claude-4-sonnet/`
- `../data/generated_tests_claude-4-5-sonnet/`
- `../data/generated_tests_claude-opus-4-1/`
- `../dataset/HumanEval.jsonl`
