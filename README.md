# 営業チームCRM - セミナー用サンプルリポジトリ

Claude CodeとGitHubを使ったチーム開発環境を体験するためのサンプルです。

---

## 当日の手順

### STEP 1｜このリポジトリをコピーする

1. このページ右上の「**Use this template**」ボタンをクリック
2. 「Create a new repository」を選択
3. Repository nameに `crm-practice` と入力
4. 「**Create repository**」をクリック

### STEP 2｜自分のPCにCloneする

1. VS Codeを開く
2. `Ctrl+Shift+P`（Mac: `Cmd+Shift+P`）→「Git: Clone」を選択
3. 自分のリポジトリのURLを貼り付け
4. 保存先フォルダを選択 → 「Open」をクリック

### STEP 3｜CLAUDE.mdを作成する

1. VS Code内でClaude Codeを開く
2. `prompts/01_create_claude_md.txt` の中身をコピー
3. Claude Codeに貼り付けて実行

### STEP 4｜Skillsを作成する

1. `prompts/02_create_skills.txt` の中身をコピー
2. Claude Codeに貼り付けて実行
3. `.claude/commands/` に2つのファイルが作成されることを確認

### STEP 5｜実際に使ってみる

**バグを発見・修正する**
```
/review
```

**PRの説明文を自動生成する**
```
/pr
```

### STEP 6｜GitHubに反映する

1. VS Code左側の「ソース管理」アイコン（🔀）をクリック
2. 変更ファイルの「+」ボタンでステージング
3. コミットメッセージを入力 → 「✓ コミット」をクリック
4. 「変更の同期」をクリック → GitHubに反映完了

---

## ファイル構成

```
crm-seminar/
├── CLAUDE.md                    ← Claudeへの指示書（セミナー中に作成）
├── .claude/
│   └── commands/
│       ├── review.md            ← /review コマンド（セミナー中に作成）
│       └── pr.md                ← /pr コマンド（セミナー中に作成）
├── main.py                      ← メインファイル（バグあり・体験用）
├── customers.py                 ← 顧客管理
├── sales.py                     ← 商談管理
└── prompts/
    ├── 01_create_claude_md.txt  ← STEP3で使うプロンプト
    └── 02_create_skills.txt     ← STEP4で使うプロンプト
```
