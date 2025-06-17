import logging
import time
from datetime import datetime
from typing import List, Dict, Any, Optional
from .config import Config
from .spreadsheet_client import SpreadsheetClient
from .scrapers import TikTokScraper

logger = logging.getLogger(__name__)

class TikTokTracker:
    def __init__(self, credentials_path: str = None, spreadsheet_url: str = None):
        self.spreadsheet_client = SpreadsheetClient(credentials_path, spreadsheet_url)
        self.scraper_class = TikTokScraper
        
    def _is_tiktok_url(self, url: str) -> bool:
        return 'tiktok.com' in url
    
    def track_single_video(self, url: str) -> Dict[str, Any]:
        if not self._is_tiktok_url(url):
            raise ValueError(f"Only TikTok URLs are supported. Got: {url}")
        
        try:
            with self.scraper_class() as scraper:
                video_data = scraper.scrape_with_retry(url)
                self.spreadsheet_client.append_video_data(video_data)
                logger.info(f"Successfully tracked TikTok video: {url}")
                return video_data
                
        except Exception as e:
            logger.error(f"Failed to track TikTok video {url}: {e}")
            raise
    
    def track_multiple_videos(self, urls: List[str]) -> List[Dict[str, Any]]:
        results = []
        failed_urls = []
        
        for url in urls:
            try:
                result = self.track_single_video(url)
                results.append(result)
                time.sleep(Config.REQUEST_DELAY)
                
            except Exception as e:
                logger.error(f"Failed to track video {url}: {e}")
                failed_urls.append(url)
                continue
        
        if failed_urls:
            logger.warning(f"Failed to track {len(failed_urls)} videos: {failed_urls}")
        
        logger.info(f"Successfully tracked {len(results)} out of {len(urls)} videos")
        return results
    
    def update_existing_videos(self, urls: List[str]) -> List[Dict[str, Any]]:
        results = []
        
        for url in urls:
            try:
                if not self._is_tiktok_url(url):
                    logger.warning(f"Only TikTok URLs are supported. Skipping: {url}")
                    continue
                
                with self.scraper_class() as scraper:
                    video_data = scraper.scrape_with_retry(url)
                    
                    updated_data = {
                        'view_count': video_data['view_count'],
                        'like_count': video_data['like_count'],
                        'comment_count': video_data['comment_count'],
                        'share_count': video_data['share_count'],
                        'last_updated': datetime.now().isoformat()
                    }
                    
                    success = self.spreadsheet_client.update_existing_video(url, updated_data)
                    if not success:
                        self.spreadsheet_client.append_video_data(video_data)
                        logger.info(f"Added new TikTok video data for: {url}")
                    else:
                        logger.info(f"Updated existing TikTok video data for: {url}")
                    
                    results.append(video_data)
                    time.sleep(Config.REQUEST_DELAY)
                    
            except Exception as e:
                logger.error(f"Failed to update TikTok video {url}: {e}")
                continue
        
        logger.info(f"Successfully processed {len(results)} TikTok videos for updates")
        return results
    
    def initialize_spreadsheet(self, sheet_name: str = "TikTok_Video_Data"):
        try:
            self.spreadsheet_client.initialize_headers(sheet_name)
            logger.info(f"Spreadsheet initialized with sheet: {sheet_name}")
        except Exception as e:
            logger.error(f"Failed to initialize spreadsheet: {e}")
            raise
    
    def get_video_summary(self, video_data: Dict[str, Any]) -> str:
        return f"""
TikTok Video Summary:
- Author: {video_data.get('author', 'Unknown')}
- Title: {video_data.get('title', 'No title')[:50]}...
- Views: {video_data.get('view_count', 0):,}
- Likes: {video_data.get('like_count', 0):,}
- Comments: {video_data.get('comment_count', 0):,}
- Shares: {video_data.get('share_count', 0):,}
- Last Updated: {video_data.get('last_updated', 'Unknown')}
"""
