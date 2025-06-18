#!/usr/bin/env python3
"""
TikTokセレクターデバッグツール
実際のページ構造を確認してCSS セレクターをテスト
"""
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_selectors():
    """TikTokページでセレクターをテスト"""
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-plugins')
    chrome_options.add_argument('--disable-images')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36')
    
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
    
    try:
        print("🚀 annotakahiro2024プロフィールページにアクセス中...")
        driver.get("https://www.tiktok.com/@annotakahiro2024")
        print("⏳ 初期ロード待機中...")
        time.sleep(15)  # より長い待機時間
        
        print("📜 自然なスクロール動作でコンテンツを読み込み中...")
        for i in range(3):
            driver.execute_script(f"window.scrollTo(0, {500 * (i + 1)});")
            time.sleep(2)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(5)
        
        print("📋 ページタイトル:", driver.title)
        print("📋 現在のURL:", driver.current_url)
        
        selectors_to_test = [
            'div[aria-label="Watch in full screen"]',
            'div[data-e2e="user-post-item"]',
            'a[href*="/video/"]',
            'div[class*="video"]',
            'div[class*="item"]',
            'strong',
            'div[class*="DivContainer"]'
        ]
        
        for selector in selectors_to_test:
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                print(f"✅ セレクター '{selector}': {len(elements)}個の要素を発見")
                
                if elements and len(elements) > 0:
                    print(f"   最初の要素のテキスト: '{elements[0].text[:100]}'")
                    print(f"   最初の要素のHTML: '{elements[0].get_attribute('outerHTML')[:200]}'")
                    
            except Exception as e:
                print(f"❌ セレクター '{selector}': エラー - {e}")
        
        print("\n📋 ページ構造の一部:")
        try:
            body = driver.find_element(By.TAG_NAME, 'body')
            html_snippet = body.get_attribute('innerHTML')[:1000]
            print(html_snippet)
        except:
            print("HTMLの取得に失敗")
            
    finally:
        driver.quit()

if __name__ == '__main__':
    test_selectors()
