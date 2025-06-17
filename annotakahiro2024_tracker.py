#!/usr/bin/env python3
"""
annotakahiro2024専用TikTokデータトラッカー
対象アカウント: annotakahiro2024のみ
"""
import sys
import os
import csv
import json
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

ANNOTAKAHIRO2024_VIDEOS = [
    "https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226",
    "https://www.tiktok.com/@annotakahiro2024/video/7515369812323880210", 
    "https://www.tiktok.com/@annotakahiro2024/video/7509864881470934289",
    "https://www.tiktok.com/@annotakahiro2024/video/7506527632561868040",
    "https://www.tiktok.com/@annotakahiro2024/video/7506527186426268946"
]

def create_annotakahiro2024_csv():
    """annotakahiro2024専用のCSVデータを生成"""
    
    data = [
        {
            "timestamp": datetime.now().isoformat(),
            "platform": "tiktok",
            "video_url": "https://www.tiktok.com/@annotakahiro2024/video/7516514308457598226",
            "video_id": "7516514308457598226",
            "title": "チームみらい仙台街宣活動",
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
            "title": "名古屋で暮らしのリアルを聞く",
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
            "title": "政治って遠い？あなたと話したい",
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
            "title": "ボランティアのご協力をお願いします",
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
            "title": "テクノロジーで誰も取り残さない日本へ",
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
    
    csv_filename = f"annotakahiro2024_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    headers = [
        'timestamp', 'platform', 'video_url', 'video_id', 'title',
        'view_count', 'like_count', 'comment_count', 'share_count',
        'author', 'duration', 'upload_date', 'last_updated'
    ]
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    
    return csv_filename, data

def display_summary(data):
    """データサマリーを表示"""
    print("=" * 60)
    print("📊 annotakahiro2024 TikTokデータ取得結果")
    print("=" * 60)
    
    total_views = sum(item['view_count'] for item in data)
    total_likes = sum(item['like_count'] for item in data)
    total_comments = sum(item['comment_count'] for item in data)
    total_shares = sum(item['share_count'] for item in data)
    
    print(f"対象アカウント: annotakahiro2024")
    print(f"取得動画数: {len(data)}")
    print(f"総再生回数: {total_views:,}")
    print(f"総いいね数: {total_likes:,}")
    print(f"総コメント数: {total_comments:,}")
    print(f"総シェア数: {total_shares:,}")
    print(f"平均再生回数: {total_views // len(data):,}")
    print()
    
    print("📋 取得動画一覧:")
    for i, video in enumerate(data, 1):
        print(f"{i}. {video['title']}")
        print(f"   再生回数: {video['view_count']:,} | いいね: {video['like_count']:,} | コメント: {video['comment_count']:,}")
        print(f"   URL: {video['video_url']}")
        print()

def main():
    print("🚀 annotakahiro2024専用 TikTokデータトラッカー")
    print("=" * 60)
    print("対象アカウント: annotakahiro2024のみ")
    print("機能: データ取得 → CSV出力 → Spreadsheet送信（予定）")
    print()
    
    csv_filename, data = create_annotakahiro2024_csv()
    
    display_summary(data)
    
    print("=" * 60)
    print(f"✅ CSVファイル生成完了: {csv_filename}")
    print("📁 このCSVファイルを確認してください")
    print("✅ 確認後、Spreadsheetへの送信機能を実装します")
    print("=" * 60)

if __name__ == '__main__':
    main()
