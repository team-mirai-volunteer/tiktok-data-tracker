#!/usr/bin/env python3
"""
TikTok Data Tracker 使用例
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tiktok_tracker import TikTokTracker

def main():
    print("TikTok Data Tracker - 使用例")
    print("=" * 40)
    
    credentials_path = "credentials.json"
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit"
    
    tracker = TikTokTracker(
        credentials_path=credentials_path,
        spreadsheet_url=spreadsheet_url
    )
    
    print("\n1. 単一動画の追跡例:")
    video_url = "https://www.tiktok.com/@annotakahiro2024/video/1234567890"
    print(f"URL: {video_url}")
    print("実行コマンド:")
    print(f"python -m tiktok_tracker.cli track --url '{video_url}'")
    
    print("\n2. 複数動画の追跡例:")
    video_urls = [
        "https://www.tiktok.com/@annotakahiro2024/video/1234567890",
        "https://www.tiktok.com/@team_itabashi_mirai/video/9876543210"
    ]
    print("URLs:")
    for url in video_urls:
        print(f"  - {url}")
    print("実行コマンド:")
    print("python -m tiktok_tracker.cli track --urls \\")
    for url in video_urls:
        print(f"  '{url}' \\")
    
    print("\n3. ファイルからの一括処理例:")
    print("video_urls.txt ファイルを作成:")
    print("https://www.tiktok.com/@annotakahiro2024/video/1234567890")
    print("https://www.tiktok.com/@team_itabashi_mirai/video/9876543210")
    print("https://www.tiktok.com/@dy3kj587hd6b/video/1357924680")
    print("\n実行コマンド:")
    print("python -m tiktok_tracker.cli track --file video_urls.txt")
    
    print("\n4. プログラムからの使用例:")
    print("""
from tiktok_tracker import TikTokTracker

tracker = TikTokTracker(
    credentials_path="credentials.json",
    spreadsheet_url="https://docs.google.com/spreadsheets/d/YOUR_ID/edit"
)

video_data = tracker.track_single_video(
    "https://www.tiktok.com/@user/video/123456789"
)
print(f"再生回数: {video_data['view_count']:,}")

urls = [
    "https://www.tiktok.com/@user1/video/123",
    "https://www.tiktok.com/@user2/video/456"
]
results = tracker.track_multiple_videos(urls)
for result in results:
    print(tracker.get_video_summary(result))
""")
    
    print("\n" + "=" * 40)
    print("詳細な使用方法はREADME.mdを参照してください。")

if __name__ == '__main__':
    main()
