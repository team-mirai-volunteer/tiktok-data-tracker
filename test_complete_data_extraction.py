#!/usr/bin/env python3
"""
完全なデータ抽出機能のテスト
修正されたスクレイパーが正確なタイトルとエンゲージメント指標を取得できるかテスト
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from tiktok_tracker.scrapers.profile_scraper import TikTokProfileScraper

def test_complete_data_extraction():
    """完全なデータ抽出をテスト"""
    print("🚀 完全なデータ抽出機能のテスト開始")
    print("=" * 60)
    
    try:
        with TikTokProfileScraper() as scraper:
            print("📊 annotakahiro2024の完全な動画データを取得中...")
            videos = scraper.get_complete_video_data_from_profile('annotakahiro2024')
            
            if videos:
                print(f"✅ 取得した動画数: {len(videos)}")
                
                print("\n📋 最初の3動画のサンプルデータ:")
                for i, video in enumerate(videos[:3], 1):
                    print(f"\n動画 {i}:")
                    print(f"  タイトル: {video.get('title', 'N/A')}")
                    print(f"  再生回数: {video.get('view_count', 0):,}")
                    print(f"  いいね数: {video.get('like_count', 0):,}")
                    print(f"  コメント数: {video.get('comment_count', 0):,}")
                    print(f"  シェア数: {video.get('share_count', 0):,}")
                    print(f"  URL: {video.get('video_url', 'N/A')}")
                
                print("\n📊 データ品質統計:")
                non_zero_views = sum(1 for v in videos if v.get('view_count', 0) > 0)
                non_empty_titles = sum(1 for v in videos if v.get('title', '').strip())
                non_zero_likes = sum(1 for v in videos if v.get('like_count', 0) > 0)
                non_zero_comments = sum(1 for v in videos if v.get('comment_count', 0) > 0)
                non_zero_shares = sum(1 for v in videos if v.get('share_count', 0) > 0)
                
                print(f"  再生回数が0以外: {non_zero_views}/{len(videos)} ({non_zero_views/len(videos)*100:.1f}%)")
                print(f"  タイトルが空でない: {non_empty_titles}/{len(videos)} ({non_empty_titles/len(videos)*100:.1f}%)")
                print(f"  いいね数が0以外: {non_zero_likes}/{len(videos)} ({non_zero_likes/len(videos)*100:.1f}%)")
                print(f"  コメント数が0以外: {non_zero_comments}/{len(videos)} ({non_zero_comments/len(videos)*100:.1f}%)")
                print(f"  シェア数が0以外: {non_zero_shares}/{len(videos)} ({non_zero_shares/len(videos)*100:.1f}%)")
                
                print("\n📈 エンゲージメント統計:")
                total_views = sum(v.get('view_count', 0) for v in videos)
                total_likes = sum(v.get('like_count', 0) for v in videos)
                total_comments = sum(v.get('comment_count', 0) for v in videos)
                total_shares = sum(v.get('share_count', 0) for v in videos)
                
                print(f"  総再生回数: {total_views:,}")
                print(f"  総いいね数: {total_likes:,}")
                print(f"  総コメント数: {total_comments:,}")
                print(f"  総シェア数: {total_shares:,}")
                
                if len(videos) > 0:
                    print(f"  平均再生回数: {total_views // len(videos):,}")
                    if total_views > 0:
                        print(f"  エンゲージメント率: {((total_likes + total_comments + total_shares) / total_views * 100):.2f}%")
                
                print("\n🔍 データ品質評価:")
                if non_empty_titles > len(videos) * 0.8:
                    print("  ✅ タイトル抽出: 良好")
                else:
                    print("  ⚠️ タイトル抽出: 改善が必要")
                
                if non_zero_likes > len(videos) * 0.5:
                    print("  ✅ いいね数抽出: 良好")
                else:
                    print("  ⚠️ いいね数抽出: 改善が必要")
                    
            else:
                print("❌ 動画データを取得できませんでした")
                
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_complete_data_extraction()
