#!/usr/bin/env python3
"""
1秒のsleepを挟んでTikTokスクレイピングをテスト - エラー率確認用（改良版）
"""
import sys
import os
import time
import csv
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from tiktok_tracker.scrapers.profile_scraper import TikTokProfileScraper

def test_with_1sec_delays():
    """1秒のsleepを挟んでスクレイピングをテスト - エラー率レポート付き"""
    print("🚀 1秒delay付きTikTokスクレイピングテスト開始")
    print("=" * 60)
    
    try:
        with TikTokProfileScraper() as scraper:
            print("📊 annotakahiro2024から1秒delay付きで完全データ抽出中...")
            
            results, success_count, error_count = scraper.get_complete_video_data_from_profile_with_delays('annotakahiro2024')
            
            if not results:
                print("❌ データが取得できませんでした")
                return
            
            total_videos = len(results)
            
            csv_filename = f"annotakahiro2024_1sec_delays_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            headers = [
                'timestamp', 'platform', 'video_url', 'video_id', 'title',
                'view_count', 'like_count', 'comment_count', 'share_count',
                'author', 'duration', 'upload_date', 'last_updated'
            ]
            
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(results)
            
            print("=" * 60)
            print("📊 1秒delay付きスクレイピング結果")
            print("=" * 60)
            print(f"総動画数: {total_videos}件")
            print(f"成功: {success_count}件")
            print(f"エラー: {error_count}件")
            print(f"成功率: {(success_count / total_videos * 100):.1f}%")
            print(f"エラー率: {(error_count / total_videos * 100):.1f}%")
            print()
            
            successful_titles = sum(1 for r in results if r.get('title', '').strip() and 'エラー' not in r.get('title', ''))
            successful_likes = sum(1 for r in results if r.get('like_count', 0) > 0)
            successful_comments = sum(1 for r in results if r.get('comment_count', 0) > 0)
            successful_shares = sum(1 for r in results if r.get('share_count', 0) > 0)
            successful_views = sum(1 for r in results if r.get('view_count', 0) > 0)
            
            print("📋 データ品質分析:")
            print(f"タイトル抽出成功: {successful_titles}/{total_videos}件 ({(successful_titles/total_videos*100):.1f}%)")
            print(f"いいね数取得成功: {successful_likes}/{total_videos}件 ({(successful_likes/total_videos*100):.1f}%)")
            print(f"コメント数取得成功: {successful_comments}/{total_videos}件 ({(successful_comments/total_videos*100):.1f}%)")
            print(f"シェア数取得成功: {successful_shares}/{total_videos}件 ({(successful_shares/total_videos*100):.1f}%)")
            print(f"再生回数取得成功: {successful_views}/{total_videos}件 ({(successful_views/total_videos*100):.1f}%)")
            print()
            
            successful_videos = [r for r in results if r.get('title', '').strip() and 'エラー' not in r.get('title', '')]
            if successful_videos:
                print("✅ 成功した動画の例:")
                for i, video in enumerate(successful_videos[:3], 1):
                    title = video.get('title', 'N/A')[:50] + ('...' if len(video.get('title', '')) > 50 else '')
                    print(f"{i}. {title}")
                    print(f"   再生={video.get('view_count', 0):,}, いいね={video.get('like_count', 0):,}, コメント={video.get('comment_count', 0):,}, シェア={video.get('share_count', 0):,}")
                print()
            
            print(f"📁 CSVファイル生成: {csv_filename}")
            print(f"🎯 結果: {total_videos}件中{error_count}件のエラー")
            
            return csv_filename, results, success_count, error_count
            
    except Exception as e:
        print(f"❌ 全体エラー: {e}")
        import traceback
        traceback.print_exc()
        return None, [], 0, 0

if __name__ == '__main__':
    test_with_1sec_delays()
