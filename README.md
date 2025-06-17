# TikTok Data Tracker

TikTok動画のメトリクス（再生回数、いいね数、コメント数など）を収集し、Google Spreadsheetに出力するツールです。

## 🎯 主な機能

- **TikTok動画データ収集**: 再生回数、いいね数、コメント数、シェア数を取得
- **アカウント検索**: キーワードでTikTokアカウントを検索・発見
- **Google Spreadsheet連携**: 収集データを自動でスプレッドシートに出力
- **バッチ処理**: 複数動画の一括処理
- **スケジューラー**: 定期的な自動データ更新
- **CLI インターフェース**: コマンドラインからの簡単操作

## 🚀 実証済み機能

「チームみらい」での検索テストで以下のアカウントを発見・処理済み：
- `annotakahiro2024` - 安野たかひろスタッフ＠チームみらい【公式】(2014フォロワー)
- `team_itabashi_mirai` - チーム板橋みらい (28フォロワー)
- `dy3kj587hd6b` - ナタールブラザーズチームみらいを応援する党代表 (112フォロワー)

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

### 基本的な使用例

```bash
# スプレッドシートの初期化
python -m tiktok_tracker.cli init

# 単一動画のトラッキング
python -m tiktok_tracker.cli track --url "https://www.tiktok.com/@username/video/1234567890"

# 複数動画のトラッキング（ファイルから）
python -m tiktok_tracker.cli track --file video_urls.txt

# 複数動画のトラッキング（直接指定）
python -m tiktok_tracker.cli track --urls \
  "https://www.tiktok.com/@user1/video/123" \
  "https://www.tiktok.com/@user2/video/456"

# 既存データの更新
python -m tiktok_tracker.cli update --file video_urls.txt
```

### プログラムからの使用

```python
from tiktok_tracker import TikTokTracker

# トラッカーの初期化
tracker = TikTokTracker(
    credentials_path="credentials.json",
    spreadsheet_url="https://docs.google.com/spreadsheets/d/YOUR_ID/edit"
)

# 単一動画の追跡
video_data = tracker.track_single_video("https://www.tiktok.com/@user/video/123")
print(f"Views: {video_data['view_count']:,}")

# 複数動画の追跡
urls = ["https://www.tiktok.com/@user1/video/123", "https://www.tiktok.com/@user2/video/456"]
results = tracker.track_multiple_videos(urls)
```

### スケジューラーの使用

```python
from tiktok_tracker.scheduler import TikTokScheduler

scheduler = TikTokScheduler()

# 毎日午前9時に更新
scheduler.schedule_daily_update(
    urls_file="video_urls.txt",
    time="09:00"
)

# スケジューラー開始
scheduler.start()
```

## 📈 収集データ形式

Google Spreadsheetには以下の形式でデータが保存されます：

| 列名 | 説明 | 例 |
|------|------|-----|
| Timestamp | データ収集時刻 | 2024-12-17T10:30:00 |
| Platform | プラットフォーム | tiktok |
| Video_URL | 動画のURL | https://www.tiktok.com/@user/video/123 |
| Video_ID | 動画のID | 1234567890123456789 |
| Title | 動画のタイトル/キャプション | テクノロジーで誰も取り残さない日本へ！ |
| View_Count | 再生回数 | 15420 |
| Like_Count | いいね数 | 892 |
| Comment_Count | コメント数 | 156 |
| Share_Count | シェア数 | 78 |
| Author | 投稿者名 | annotakahiro2024 |
| Duration | 動画の長さ | 00:01:23 |
| Upload_Date | 投稿日時 | 2024-12-10T14:30:00Z |
| Last_Updated | 最終更新日時 | 2024-12-17T10:30:00 |

## 🔍 デモ実行

システムの動作確認用デモを実行：

```bash
python examples/demo_team_mirai.py
```

このデモでは「チームみらい」関連の実際のTikTokアカウントを基にしたデータ処理例を確認できます。

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
