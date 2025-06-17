#!/usr/bin/env python3
"""
Simple test script to create sample CSV data for annotakahiro2024
Based on the data structure from the existing demo
"""
import csv
import json
from datetime import datetime
from pathlib import Path

ANNOTAKAHIRO2024_SAMPLE_DATA = [
    {
        "timestamp": datetime.now().isoformat(),
        "platform": "tiktok",
        "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226",
        "video_id": "7516514308457598226",
        "title": "東京に出て一番驚いたこと",
        "view_count": 775,
        "like_count": 45,
        "comment_count": 12,
        "share_count": 8,
        "author": "annotakahiro2024",
        "duration": "00:00:30",
        "upload_date": "2024-12-15T10:00:00Z",
        "last_updated": datetime.now().isoformat()
    },
    {
        "timestamp": datetime.now().isoformat(),
        "platform": "tiktok", 
        "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7515369812323880210",
        "video_id": "7515369812323880210",
        "title": "チームみらい名古屋VLOG",
        "view_count": 502,
        "like_count": 28,
        "comment_count": 7,
        "share_count": 5,
        "author": "annotakahiro2024",
        "duration": "00:01:15",
        "upload_date": "2024-12-14T15:30:00Z",
        "last_updated": datetime.now().isoformat()
    },
    {
        "timestamp": datetime.now().isoformat(),
        "platform": "tiktok",
        "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7509864881470934289",
        "video_id": "7509864881470934289", 
        "title": "女好きさん",
        "view_count": 1001,
        "like_count": 67,
        "comment_count": 23,
        "share_count": 15,
        "author": "annotakahiro2024",
        "duration": "00:00:45",
        "upload_date": "2024-12-12T09:15:00Z",
        "last_updated": datetime.now().isoformat()
    },
    {
        "timestamp": datetime.now().isoformat(),
        "platform": "tiktok",
        "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7506527632561868040",
        "video_id": "7506527632561868040",
        "title": "ボランティアのご協力でお願いします",
        "view_count": 457,
        "like_count": 31,
        "comment_count": 9,
        "share_count": 6,
        "author": "annotakahiro2024",
        "duration": "00:00:52",
        "upload_date": "2024-12-10T14:20:00Z",
        "last_updated": datetime.now().isoformat()
    },
    {
        "timestamp": datetime.now().isoformat(),
        "platform": "tiktok",
        "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7506527186426268946",
        "video_id": "7506527186426268946",
        "title": "ぜひこのURLから見てもらって",
        "view_count": 395,
        "like_count": 22,
        "comment_count": 5,
        "share_count": 3,
        "author": "annotakahiro2024",
        "duration": "00:00:38",
        "upload_date": "2024-12-10T14:15:00Z",
        "last_updated": datetime.now().isoformat()
    }
]

def save_to_csv(data, filename="annotakahiro2024_sample_data.csv"):
    """Save data to CSV file"""
    csv_path = Path(filename)
    
    headers = [
        'timestamp', 'platform', 'video_url', 'video_id', 'title',
        'view_count', 'like_count', 'comment_count', 'share_count',
        'author', 'duration', 'upload_date', 'last_updated'
    ]
    
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✅ CSVファイルを保存しました: {csv_path.absolute()}")
        return True
        
    except Exception as e:
        print(f"❌ CSV保存エラー: {e}")
        return False

def display_csv_preview(data):
    """Display CSV data preview"""
    print("\n📋 CSV データプレビュー:")
    print("=" * 80)
    
    headers = [
        'timestamp', 'platform', 'video_url', 'video_id', 'title',
        'view_count', 'like_count', 'comment_count', 'share_count',
        'author', 'duration', 'upload_date', 'last_updated'
    ]
    
    print(" | ".join([h[:12] for h in headers]))
    print("-" * 80)
    
    for row in data:
        values = []
        for header in headers:
            value = str(row.get(header, ''))
            if header == 'title':
                value = value[:20] + "..." if len(value) > 20 else value
            elif header in ['video_url']:
                value = value[:25] + "..." if len(value) > 25 else value
            elif header in ['timestamp', 'upload_date', 'last_updated']:
                value = value[:16] if len(value) > 16 else value
            values.append(value[:12])
        print(" | ".join(values))

def display_summary(data):
    """Display summary statistics"""
    print("\n" + "=" * 50)
    print("📊 annotakahiro2024 データサマリー")
    print("=" * 50)
    
    total_views = sum(item.get('view_count', 0) for item in data)
    total_likes = sum(item.get('like_count', 0) for item in data)
    total_comments = sum(item.get('comment_count', 0) for item in data)
    total_shares = sum(item.get('share_count', 0) for item in data)
    
    print(f"対象アカウント: annotakahiro2024")
    print(f"取得動画数: {len(data)}")
    print(f"総再生回数: {total_views:,}")
    print(f"総いいね数: {total_likes:,}")
    print(f"総コメント数: {total_comments:,}")
    print(f"総シェア数: {total_shares:,}")
    
    if len(data) > 0:
        print(f"平均再生回数: {total_views // len(data):,}")
        print(f"平均いいね数: {total_likes // len(data):,}")

def main():
    print("🚀 annotakahiro2024 TikTokデータ サンプル生成")
    print("=" * 60)
    print("対象アカウント: annotakahiro2024 のみ")
    print(f"サンプル動画数: {len(ANNOTAKAHIRO2024_SAMPLE_DATA)}")
    print()
    
    display_summary(ANNOTAKAHIRO2024_SAMPLE_DATA)
    
    display_csv_preview(ANNOTAKAHIRO2024_SAMPLE_DATA)
    
    csv_filename = f"annotakahiro2024_sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    if save_to_csv(ANNOTAKAHIRO2024_SAMPLE_DATA, csv_filename):
        print(f"\n📁 CSVファイル: {csv_filename}")
        
        json_filename = csv_filename.replace('.csv', '.json')
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(ANNOTAKAHIRO2024_SAMPLE_DATA, f, ensure_ascii=False, indent=2)
        print(f"📁 JSONファイル: {json_filename}")
    
    print("\n✅ サンプルデータ生成完了！")
    print("このCSV形式でデータを取得します。")
    print("実際のスクレイピング機能の修正後、リアルデータに置き換えます。")

if __name__ == '__main__':
    main()
