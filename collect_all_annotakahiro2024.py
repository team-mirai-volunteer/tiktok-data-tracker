#!/usr/bin/env python3
"""
annotakahiro2024の全動画を取得するスクリプト
"""
import sys
import os
import csv
import json
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from tiktok_tracker.scrapers.profile_scraper import TikTokProfileScraper

def collect_all_videos():
    """annotakahiro2024の全動画を収集"""
    print("🚀 annotakahiro2024 全動画収集開始")
    print("=" * 60)
    
    try:
        with TikTokProfileScraper() as scraper:
            print("📊 プロフィールページから動画データを取得中...")
            print("⏳ ページの読み込みとスクロールを実行中...")
            
            videos_data = scraper.get_complete_video_data_from_profile("annotakahiro2024")
            
            if not videos_data:
                print("❌ 動画データが取得できませんでした")
                print("🔍 デバッグ: プロフィールページの構造を確認中...")
                
                try:
                    urls_only = scraper.extract_video_urls_from_profile("annotakahiro2024")
                    if urls_only:
                        print(f"📋 URLのみ取得成功: {len(urls_only)}本")
                        videos_data = []
                        for i, url in enumerate(urls_only):
                            video_id = scraper._extract_video_id_from_url(url)
                            videos_data.append({
                                "timestamp": datetime.now().isoformat(),
                                "platform": "tiktok",
                                "video_url": url,
                                "video_id": video_id,
                                "title": f"動画 #{i+1}",
                                "view_count": 0,
                                "like_count": 0,
                                "comment_count": 0,
                                "share_count": 0,
                                "author": "annotakahiro2024",
                                "duration": "",
                                "upload_date": "",
                                "last_updated": datetime.now().isoformat()
                            })
                    else:
                        print("❌ URLの取得も失敗しました")
                        return None, []
                except Exception as url_error:
                    print(f"❌ URL取得エラー: {url_error}")
                    return None, []
            
            print(f"✅ {len(videos_data)}本の動画を発見しました")
            
            csv_filename = f"annotakahiro2024_all_videos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            headers = [
                'timestamp', 'platform', 'video_url', 'video_id', 'title',
                'view_count', 'like_count', 'comment_count', 'share_count',
                'author', 'duration', 'upload_date', 'last_updated'
            ]
            
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(videos_data)
            
            return csv_filename, videos_data
            
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        print(f"詳細エラー: {traceback.format_exc()}")
        return None, []

def display_summary(videos_data):
    """収集結果のサマリーを表示"""
    if not videos_data:
        print("表示するデータがありません")
        return
    
    print("\n" + "=" * 60)
    print("📊 annotakahiro2024 全動画収集結果")
    print("=" * 60)
    
    total_views = sum(video.get('view_count', 0) for video in videos_data)
    
    print(f"対象アカウント: annotakahiro2024")
    print(f"収集動画数: {len(videos_data)}本")
    print(f"総再生回数: {total_views:,}回")
    
    if len(videos_data) > 0:
        avg_views = total_views // len(videos_data)
        print(f"平均再生回数: {avg_views:,}回")
    
    print("\n📋 再生回数上位10本:")
    sorted_videos = sorted(videos_data, key=lambda x: x.get('view_count', 0), reverse=True)
    
    for i, video in enumerate(sorted_videos[:10], 1):
        view_count = video.get('view_count', 0)
        video_id = video.get('video_id', 'Unknown')
        print(f"{i:2d}. {view_count:,}回再生 (ID: {video_id})")
        print(f"    URL: {video.get('video_url', '')}")
    
    print(f"\n📁 全データをCSVファイルに保存しました")

def main():
    print("🎯 annotakahiro2024 TikTok全動画収集ツール")
    print("=" * 60)
    print("機能: プロフィールページから全動画のURL・再生回数を取得")
    print("対象: annotakahiro2024アカウントのみ")
    print()
    
    csv_filename, videos_data = collect_all_videos()
    
    if csv_filename and videos_data:
        display_summary(videos_data)
        
        print("\n" + "=" * 60)
        print(f"✅ 収集完了: {csv_filename}")
        print("📋 このCSVファイルで全動画データを確認してください")
        print("✅ 確認後、詳細データ取得やSpreadsheet送信を実装します")
        print("=" * 60)
    else:
        print("\n❌ 動画収集に失敗しました")

if __name__ == '__main__':
    main()
