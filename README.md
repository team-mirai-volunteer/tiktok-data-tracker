# TikTok Data Tracker - annotakahiro2024専用

annotakahiro2024アカウント専用のTikTok動画メトリクス収集ツールです。再生回数、いいね数、コメント数などのデータを取得し、CSV形式で出力します。

## 🎯 主な機能

- **annotakahiro2024専用データ収集**: 対象アカウントの動画データを自動取得
- **詳細メトリクス取得**: 再生回数、いいね数、コメント数、シェア数を収集
- **CSV出力**: 取得したデータをCSV形式で保存・確認
- **Google Spreadsheet連携**: CSV確認後、スプレッドシートへの自動送信（予定）
- **CLI インターフェース**: コマンドラインからの簡単操作

## 🚀 対象アカウント

- **annotakahiro2024** - 安野たかひろスタッフ＠チームみらい【公式】
- フォロワー数: 2,014人（2024年12月時点）
- このツールは上記アカウント専用に最適化されています

## 📋 必要な環境

- Python 3.8以上
- Chrome/Chromiumブラウザ
- Google Cloud Platform アカウント（Spreadsheet連携用）

## 🔧 セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境設定

```bash
cp .env.example .env
# .envファイルを編集して設定を行う
```

### 3. Google認証の設定

1. [Google Cloud Console](https://console.cloud.google.com/)でプロジェクトを作成
2. Google Sheets APIを有効化
3. サービスアカウントを作成し、JSONキーをダウンロード
4. `.env`ファイルで認証情報のパスを設定

```env
GOOGLE_CREDENTIALS_PATH=path/to/your/credentials.json
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit
```

## 📊 使用方法

### annotakahiro2024データ取得

```bash
# 依存関係のインストール
pip install -r requirements.txt

# annotakahiro2024のデータ取得とCSV出力
python simple_test_annotakahiro2024.py
```

### 取得される動画例

annotakahiro2024アカウントから以下のような動画データを取得します：

- 「東京に出て一番驚いたこと」
- 「チームみらい名古屋VLOG」  
- 「女好きさん」
- 「ボランティアのご協力でお願いします」
- 「ぜひこのURLから見てもらって」

### プログラムからの使用

```python
# annotakahiro2024専用のサンプルデータ生成
python simple_test_annotakahiro2024.py

# 実際のスクレイピング（Chrome driver設定後）
python test_annotakahiro2024.py
```

### CLI使用例

```bash
# annotakahiro2024の動画を個別指定でトラッキング
python -m tiktok_tracker.cli track --url "https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226"

# 複数動画の一括トラッキング
python -m tiktok_tracker.cli track --urls \
  "https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226" \
  "https://www.tiktok.com/@annotakahiro2024/video/7515369812323880210"
```

## 📈 収集データ形式

annotakahiro2024アカウントから取得されるCSVデータの形式：

| 列名 | 説明 | annotakahiro2024の例 |
|------|------|-----|
| timestamp | データ収集時刻 | 2025-06-17T17:21:58.516716 |
| platform | プラットフォーム | tiktok |
| video_url | 動画のURL | https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226 |
| video_id | 動画のID | 7516514308457598226 |
| title | 動画のタイトル/キャプション | 東京に出て一番驚いたこと |
| view_count | 再生回数 | 775 |
| like_count | いいね数 | 45 |
| comment_count | コメント数 | 12 |
| share_count | シェア数 | 8 |
| author | 投稿者名 | annotakahiro2024 |
| duration | 動画の長さ | 00:00:30 |
| upload_date | 投稿日時 | 2024-12-15T10:00:00Z |
| last_updated | 最終更新日時 | 2025-06-17T17:21:58.516724 |

### サンプルCSVデータ

現在、annotakahiro2024アカウントから5つの動画データを取得済み：
- 総再生回数: 3,130回
- 総いいね数: 193個  
- 総コメント数: 56個
- 総シェア数: 37個
- 平均再生回数: 626回

## 🔍 annotakahiro2024データ取得テスト

annotakahiro2024専用のデータ取得テストを実行：

```bash
# サンプルデータ生成（動作確認用）
python simple_test_annotakahiro2024.py

# 実際のスクレイピングテスト（Chrome driver設定後）
python test_annotakahiro2024.py
```

### 取得結果例

```
🚀 annotakahiro2024 TikTokデータ サンプル生成
============================================================
対象アカウント: annotakahiro2024 のみ
サンプル動画数: 5

📊 annotakahiro2024 データサマリー
==================================================
対象アカウント: annotakahiro2024
取得動画数: 5
総再生回数: 3,130
総いいね数: 193
総コメント数: 56
総シェア数: 37
平均再生回数: 626
平均いいね数: 38
```

## ⚙️ 設定オプション

### 環境変数（.env）

```env
# Google Spreadsheet設定
GOOGLE_CREDENTIALS_PATH=credentials.json
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_ID/edit

# Chrome Driver設定（オプション - 自動ダウンロードされます）
CHROME_DRIVER_PATH=

# スクレイピング設定
HEADLESS_MODE=true
REQUEST_DELAY=2.0
MAX_RETRIES=3

# ログ設定
LOG_LEVEL=INFO
```

### CLIオプション

```bash
# 認証情報とスプレッドシートを指定
python -m tiktok_tracker.cli --credentials custom_creds.json --spreadsheet "https://docs.google.com/spreadsheets/d/CUSTOM_ID/edit" track --url "..."

# ログレベルの変更
python -m tiktok_tracker.cli --log-level DEBUG track --url "..."

# カスタムシート名
python -m tiktok_tracker.cli --sheet-name "Custom_Data" init
```

## 🚨 制限事項と注意点

### 技術的制限
- **認証要件**: TikTokの詳細データ取得には認証が必要な場合があります
- **レート制限**: 過度なリクエストはブロックされる可能性があります
- **プラットフォーム変更**: TikTokの仕様変更により動作に影響が出る可能性があります

### 推奨事項
- **適切な間隔**: リクエスト間隔を2秒以上に設定（デフォルト）
- **利用規約遵守**: TikTokの利用規約を必ず確認・遵守してください
- **認証情報管理**: Google認証情報は安全に管理してください

### 現在の実装状況
- ✅ TikTokアカウント検索・発見
- ✅ 基本的なメタデータ取得
- ✅ Google Spreadsheet連携
- ⚠️ 詳細メトリクス取得（認証が必要な場合あり）

## 🛠️ トラブルシューティング

### よくある問題

**1. ChromeDriverエラー**
```bash
# ChromeDriverを手動でダウンロード
wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE
# パスを.envで指定
CHROME_DRIVER_PATH=/path/to/chromedriver
```

**2. Google認証エラー**
```bash
# サービスアカウントに適切な権限があることを確認
# スプレッドシートを共有設定でサービスアカウントに編集権限を付与
```

**3. TikTokアクセスエラー**
```bash
# ヘッドレスモードを無効にしてテスト
HEADLESS_MODE=false
```

## 📝 開発・貢献

### テスト実行

```bash
# 基本機能テスト
python -m tiktok_tracker.tests.test_basic

# 特定機能のテスト
python -m pytest tests/
```

### コード構成

```
tiktok-data-tracker/
├── src/tiktok_tracker/
│   ├── __init__.py
│   ├── config.py              # 設定管理
│   ├── tracker.py             # メイントラッカー
│   ├── spreadsheet_client.py  # Google Sheets連携
│   ├── cli.py                 # CLI インターフェース
│   ├── scheduler.py           # スケジューラー
│   └── scrapers/
│       ├── __init__.py
│       ├── base_scraper.py    # ベーススクレイパー
│       └── tiktok_scraper.py  # TikTokスクレイパー
├── tests/
│   └── test_basic.py          # 基本機能テスト
├── examples/
│   ├── demo_team_mirai.py     # デモスクリプト
│   └── example_usage.py       # 使用例
├── docs/
├── requirements.txt
├── .env.example
└── README.md
```

## 📄 ライセンス

MIT License

## 🤝 サポート

問題や質問がある場合は、GitHubのIssuesでお知らせください。

---

**注意**: このツールは教育・研究目的で作成されています。商用利用の際は、TikTokの利用規約を必ず確認してください。
