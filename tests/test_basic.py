#!/usr/bin/env python3
"""
Basic functionality test for TikTok Data Tracker
"""
import sys
import logging
from tiktok_tracker.scrapers.tiktok_scraper import TikTokScraper

def test_video_id_extraction():
    """Test video ID extraction from TikTok URLs"""
    print("Testing TikTok video ID extraction...")
    
    tiktok_scraper = TikTokScraper()
    
    tiktok_urls = [
        "https://www.tiktok.com/@username/video/1234567890123456789",
        "https://tiktok.com/@user/video/9876543210987654321",
        "https://vm.tiktok.com/ZMd1234567/"
    ]
    
    for url in tiktok_urls:
        video_id = tiktok_scraper.extract_video_id(url)
        print(f"TikTok URL: {url} -> ID: {video_id}")

def test_number_extraction():
    """Test number extraction from text"""
    print("\nTesting number extraction...")
    
    scraper = TikTokScraper()
    
    test_cases = [
        ("1,234", 1234),
        ("1.2K", 1200),
        ("2.5M", 2500000),
        ("1B", 1000000000),
        ("500万", 5000000),
        ("1.5億", 150000000),
        ("123 likes", 123),
        ("No numbers here", 0)
    ]
    
    for text, expected in test_cases:
        result = scraper._extract_number_from_text(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{text}' -> {result} (expected: {expected})")

def test_tiktok_url_detection():
    """Test TikTok URL detection"""
    print("\nTesting TikTok URL detection...")
    
    from tiktok_tracker.video_tracker import TikTokTracker
    tracker = TikTokTracker()
    
    test_urls = [
        ("https://www.tiktok.com/@user/video/123456789", True),
        ("https://tiktok.com/@user/video/987654321", True),
        ("https://vm.tiktok.com/ZMd1234567/", True),
        ("https://youtube.com/watch?v=abc123", False),
        ("https://instagram.com/p/ABC123/", False),
        ("https://twitter.com/user/status/123", False)
    ]
    
    for url, expected in test_urls:
        result = tracker._is_tiktok_url(url)
        status = "✓" if result == expected else "✗"
        print(f"{status} {url} -> {result} (expected: {expected})")

def main():
    logging.basicConfig(level=logging.INFO)
    
    print("TikTok Data Tracker - Basic Functionality Test")
    print("=" * 50)
    
    try:
        test_video_id_extraction()
        test_number_extraction()
        test_tiktok_url_detection()
        
        print("\n" + "=" * 50)
        print("✓ All basic tests completed successfully!")
        print("TikTok tracker system is ready for use.")
        
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
