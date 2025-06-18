#!/usr/bin/env python3
"""
TikTokプロフィールスクレイパー - annotakahiro2024の全動画を取得
"""
import logging
import time
import re
from typing import List, Dict, Any
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_scraper import BaseScraper

logger = logging.getLogger(__name__)

class TikTokProfileScraper(BaseScraper):
    def __init__(self):
        super().__init__()
        self.collected_urls = set()
    
    def extract_video_id(self, url: str) -> str:
        """URLから動画IDを抽出 (BaseScraper abstract method implementation)"""
        return self._extract_video_id_from_url(url)
    
    def scrape_video_data(self, url: str) -> Dict[str, Any]:
        """単一動画データを取得 (BaseScraper abstract method implementation)"""
        return {
            "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
            "platform": "tiktok",
            "video_url": url,
            "video_id": self.extract_video_id(url),
            "title": "",
            "view_count": 0,
            "like_count": 0,
            "comment_count": 0,
            "share_count": 0,
            "author": "",
            "duration": "",
            "upload_date": "",
            "last_updated": time.strftime('%Y-%m-%dT%H:%M:%S')
        }
        
    def extract_video_urls_from_profile(self, username: str) -> List[str]:
        """プロフィールページから全動画URLを取得"""
        profile_url = f"https://www.tiktok.com/@{username}"
        logger.info(f"Scraping profile: {profile_url}")
        
        try:
            self.driver.get(profile_url)
            self._wait_for_page_load()
            time.sleep(15)  # より長い初期待機時間
            
            video_urls = []
            last_count = 0
            scroll_attempts = 0
            max_scroll_attempts = 10
            
            while scroll_attempts < max_scroll_attempts:
                current_urls = self._extract_video_urls_from_current_page()
                video_urls.extend(current_urls)
                
                if len(video_urls) == last_count:
                    scroll_attempts += 1
                else:
                    scroll_attempts = 0
                    last_count = len(video_urls)
                
                self._scroll_to_load_more()
                time.sleep(2)
                
            video_urls = list(dict.fromkeys(video_urls))
            logger.info(f"Found {len(video_urls)} videos for @{username}")
            return video_urls
            
        except Exception as e:
            logger.error(f"Failed to scrape profile @{username}: {e}")
            raise
    
    def _extract_video_urls_from_current_page(self) -> List[str]:
        """現在のページから動画URLを抽出"""
        urls = []
        
        try:
            video_selectors = [
                'a[href*="/video/"]',
                'div[data-e2e="user-post-item"] a',
                'div[aria-label="Watch in full screen"] a'
            ]
            
            for selector in video_selectors:
                try:
                    video_elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for element in video_elements:
                        href = element.get_attribute('href')
                        if href and '/video/' in href and href not in self.collected_urls:
                            urls.append(href)
                            self.collected_urls.add(href)
                    
                    if urls:
                        break
                        
                except NoSuchElementException:
                    continue
                    
        except Exception as e:
            logger.warning(f"Error extracting video URLs: {e}")
            
        return urls
    
    def _scroll_to_load_more(self):
        """ページをスクロールして追加動画を読み込み - 効率的な動作"""
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            self.driver.execute_script("window.scrollBy(0, -200);")
            time.sleep(1)
            
        except Exception as e:
            logger.warning(f"Error during scrolling: {e}")
    
    def get_video_basic_data_from_profile(self, username: str) -> List[Dict[str, Any]]:
        """プロフィールページから基本的な動画データを取得"""
        profile_url = f"https://www.tiktok.com/@{username}"
        logger.info(f"Getting basic video data from: {profile_url}")
        
        try:
            self.driver.get(profile_url)
            self._wait_for_page_load()
            time.sleep(15)  # より長い初期待機時間
            
            videos_data = []
            last_count = 0
            scroll_attempts = 0
            max_scroll_attempts = 8
            
            while scroll_attempts < max_scroll_attempts:
                current_videos = self._extract_video_data_from_current_page(username)
                
                for video in current_videos:
                    if not any(v['video_url'] == video['video_url'] for v in videos_data):
                        videos_data.append(video)
                
                logger.info(f"Current video count: {len(videos_data)}")
                
                if len(videos_data) == last_count:
                    scroll_attempts += 1
                    logger.info(f"No new videos found, scroll attempt {scroll_attempts}/{max_scroll_attempts}")
                else:
                    scroll_attempts = 0
                    last_count = len(videos_data)
                
                if scroll_attempts < max_scroll_attempts:
                    self._scroll_to_load_more()
                    time.sleep(2)
            
            logger.info(f"Collected {len(videos_data)} videos with basic data")
            return videos_data
            
        except Exception as e:
            logger.error(f"Failed to get video data from profile @{username}: {e}")
            raise
    
    def _extract_video_data_from_current_page(self, username: str) -> List[Dict[str, Any]]:
        """現在のページから動画データを抽出 - デバッグ済みセレクター使用"""
        videos = []
        
        try:
            video_containers = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-e2e="user-post-item"]')
            logger.info(f"Found {len(video_containers)} video containers with data-e2e selector")
            
            if not video_containers:
                video_containers = self.driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Watch in full screen"]')
                logger.info(f"Found {len(video_containers)} video containers with aria-label selector")
            
            for container in video_containers:
                try:
                    video_data = self._extract_single_video_data(container, username)
                    if video_data and video_data['video_url'] not in [v['video_url'] for v in videos]:
                        videos.append(video_data)
                        
                except Exception as e:
                    logger.warning(f"Error extracting single video data: {e}")
                    continue
                    
        except Exception as e:
            logger.warning(f"Error finding video containers: {e}")
            
        return videos
    
    def _extract_single_video_data(self, container, username: str) -> Dict[str, Any]:
        """単一の動画データを抽出"""
        try:
            video_url = None
            try:
                link_element = container.find_element(By.CSS_SELECTOR, 'a')
                href = link_element.get_attribute('href')
                if href and '/video/' in href:
                    video_url = href
            except:
                return None
            
            if not video_url:
                return None
            
            video_id = self._extract_video_id_from_url(video_url)
            
            view_count = 0
            try:
                strong_elements = container.find_elements(By.CSS_SELECTOR, 'strong')
                for elem in strong_elements:
                    text = elem.text.strip()
                    if text and (text.isdigit() or 'K' in text or 'M' in text or '万' in text):
                        view_count = self._parse_view_count(text)
                        if view_count > 0:
                            break
                
                if view_count == 0:
                    all_text = container.text
                    import re
                    numbers = re.findall(r'\d+', all_text)
                    for num in numbers:
                        if int(num) > 50:  # 50以上の数値を再生回数として扱う
                            view_count = int(num)
                            break
                            
            except Exception as e:
                logger.warning(f"Error extracting view count: {e}")
            
            return {
                "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
                "platform": "tiktok",
                "video_url": video_url,
                "video_id": video_id,
                "title": "",
                "view_count": view_count,
                "like_count": 0,
                "comment_count": 0,
                "share_count": 0,
                "author": username,
                "duration": "",
                "upload_date": "",
                "last_updated": time.strftime('%Y-%m-%dT%H:%M:%S')
            }
            
        except Exception as e:
            logger.warning(f"Error extracting video data from container: {e}")
            return None
    
    def _extract_video_id_from_url(self, url: str) -> str:
        """URLから動画IDを抽出"""
        match = re.search(r'/video/(\d+)', url)
        return match.group(1) if match else ""
    
    def _parse_view_count(self, text: str) -> int:
        """K/M表記の再生回数を数値に変換"""
        try:
            text = text.upper().replace(',', '').replace(' ', '')
            if 'K' in text:
                return int(float(text.replace('K', '')) * 1000)
            elif 'M' in text:
                return int(float(text.replace('M', '')) * 1000000)
            elif '万' in text:
                return int(float(text.replace('万', '')) * 10000)
            elif text.isdigit():
                return int(text)
            else:
                numbers = ''.join(filter(str.isdigit, text))
                return int(numbers) if numbers else 0
        except:
            return 0
