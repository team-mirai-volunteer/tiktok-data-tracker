#!/usr/bin/env python3
"""
Example usage of the TikTok Data Tracker system
"""
import os
import logging
from video_tracker import TikTokTracker

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def example_single_video():
    """Example: Track a single TikTok video"""
    print("=== Example: Track Single TikTok Video ===")
    
    tracker = TikTokTracker()
    
    tiktok_url = "https://www.tiktok.com/@annotakahiro2024/video/1234567890123456789"
    
    try:
        print("Tracking TikTok video...")
        result = tracker.track_single_video(tiktok_url)
        print(tracker.get_video_summary(result))
        
    except Exception as e:
        print(f"Error: {e}")

def example_multiple_videos():
    """Example: Track multiple TikTok videos at once"""
    print("=== Example: Track Multiple TikTok Videos ===")
    
    tracker = TikTokTracker()
    
    urls = [
        "https://www.tiktok.com/@annotakahiro2024/video/1234567890123456789",
        "https://www.tiktok.com/@team_itabashi_mirai/video/2345678901234567890",
        "https://www.tiktok.com/@dy3kj587hd6b/video/3456789012345678901",
        "https://www.tiktok.com/@username/video/9876543210987654321"
    ]
    
    try:
        print(f"Tracking {len(urls)} videos...")
        results = tracker.track_multiple_videos(urls)
        
        print(f"\nSuccessfully tracked {len(results)} videos:")
        for result in results:
            print(tracker.get_video_summary(result))
            
    except Exception as e:
        print(f"Error: {e}")

def example_update_videos():
    """Example: Update existing TikTok video data"""
    print("=== Example: Update Existing TikTok Videos ===")
    
    tracker = TikTokTracker()
    
    urls = [
        "https://www.tiktok.com/@annotakahiro2024/video/1234567890123456789",
        "https://www.tiktok.com/@team_itabashi_mirai/video/2345678901234567890"
    ]
    
    try:
        print(f"Updating {len(urls)} videos...")
        results = tracker.update_existing_videos(urls)
        
        print(f"\nSuccessfully updated {len(results)} videos:")
        for result in results:
            print(tracker.get_video_summary(result))
            
    except Exception as e:
        print(f"Error: {e}")

def example_initialize_spreadsheet():
    """Example: Initialize spreadsheet with headers"""
    print("=== Example: Initialize Spreadsheet ===")
    
    tracker = VideoTracker()
    
    try:
        tracker.initialize_spreadsheet("SNS_Video_Data")
        print("Spreadsheet initialized successfully!")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    setup_logging()
    
    print("SNS Video Tracker - Example Usage")
    print("=" * 50)
    
    print("\nBefore running these examples, make sure you have:")
    print("1. Set up your Google credentials (gcp_credentials.json)")
    print("2. Created a Google Spreadsheet and set SPREADSHEET_URL")
    print("3. Replaced example URLs with real video URLs")
    print("4. Installed required dependencies")
    
    print("\nAvailable examples:")
    print("1. Initialize spreadsheet")
    print("2. Track single video")
    print("3. Track multiple videos")
    print("4. Update existing videos")
    
    choice = input("\nEnter example number (1-4) or 'all' to run all: ").strip()
    
    if choice == '1':
        example_initialize_spreadsheet()
    elif choice == '2':
        example_single_video()
    elif choice == '3':
        example_multiple_videos()
    elif choice == '4':
        example_update_videos()
    elif choice.lower() == 'all':
        example_initialize_spreadsheet()
        example_single_video()
        example_multiple_videos()
        example_update_videos()
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == '__main__':
    main()
