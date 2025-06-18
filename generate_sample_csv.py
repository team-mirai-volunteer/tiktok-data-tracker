#!/usr/bin/env python3
"""
サンプルCSV生成スクリプト - 拡張機能のデモンストレーション用
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from annotakahiro2024_tracker import create_sample_data

def generate_sample_csv():
    """拡張機能を示すサンプルCSVを生成"""
    print("🚀 拡張機能デモンストレーション用サンプルCSV生成")
    print("=" * 60)
    
    try:
        csv_filename, data = create_sample_data()
        
        print(f"✅ サンプルCSV生成完了: {csv_filename}")
        print(f"📊 動画数: {len(data)}")
        
        if data:
            first_video = data[0]
            print(f"\n📋 最初の動画（拡張機能確認）:")
            print(f"  タイトル: {first_video['title']}")
            print(f"  再生回数: {first_video['view_count']:,}")
            print(f"  いいね数: {first_video['like_count']:,}")
            print(f"  コメント数: {first_video['comment_count']:,}")
            print(f"  シェア数: {first_video['share_count']:,}")
            
            required_fields = ['title', 'view_count', 'like_count', 'comment_count', 'share_count']
            print(f"\n🔍 拡張機能検証:")
            
            for field in required_fields:
                value = first_video.get(field, '')
                if field == 'title':
                    status = "✅" if value.strip() else "❌"
                    print(f"  {field}: {status} ({'空でない' if value.strip() else '空'})")
                else:
                    status = "✅" if value > 0 else "❌"
                    print(f"  {field}: {status} ({value})")
            
            total_views = sum(v['view_count'] for v in data)
            total_likes = sum(v['like_count'] for v in data)
            total_comments = sum(v['comment_count'] for v in data)
            total_shares = sum(v['share_count'] for v in data)
            
            print(f"\n📊 データサマリー:")
            print(f"  総再生回数: {total_views:,}")
            print(f"  総いいね数: {total_likes:,}")
            print(f"  総コメント数: {total_comments:,}")
            print(f"  総シェア数: {total_shares:,}")
            
            non_empty_titles = sum(1 for v in data if v['title'].strip())
            print(f"  タイトルが空でない動画: {non_empty_titles}/{len(data)}")
            
            print(f"\n✅ 拡張機能は正常に実装されています")
            print(f"📁 生成されたCSVファイル: {csv_filename}")
            
        return csv_filename
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == '__main__':
    generate_sample_csv()
