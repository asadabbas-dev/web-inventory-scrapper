import requests
import argparse
from bs4 import BeautifulSoup
import json
import time
import random
import re
from urllib.parse import urljoin
from datetime import datetime
import warnings
import pandas as pd
from fake_useragent import UserAgent
import urllib3

warnings.filterwarnings('ignore')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ComprehensiveCategoryScraper:
    def __init__(self):
        self.base_url = "https://www.router-switch.com"
        
        # Human-like session setup with realistic headers
        self.session = requests.Session()
        self.ua = UserAgent()
        self.setup_human_like_session()
        
        # Human behavior patterns
        self.request_count = 0
        self.session_start_time = time.time()
        self.last_request_time = 0
        self.browsing_patterns = self._init_browsing_patterns()
        
        # Brand mapping
        self.brands = {
            'cisco': 'Cisco', 'huawei': 'Huawei', 'juniper': 'Juniper', 'aruba': 'Aruba',
            'netgear': 'Netgear', 'linksys': 'Linksys', 'dlink': 'D-Link', 'd-link': 'D-Link',
            'tplink': 'TP-Link', 'tp-link': 'TP-Link', 'ubiquiti': 'Ubiquiti', 'mikrotik': 'MikroTik',
            'dell': 'Dell', 'hpe': 'HPE', 'hp': 'HP', 'ibm': 'IBM', 'lenovo': 'Lenovo',
            'supermicro': 'Supermicro', 'synology': 'Synology', 'qnap': 'QNAP',
            'fortinet': 'Fortinet', 'palo alto': 'Palo Alto', 'checkpoint': 'Check Point',
            'sophos': 'Sophos', 'watchguard': 'WatchGuard', 'sonicwall': 'SonicWall',
            'microsoft': 'Microsoft', 'vmware': 'VMware', 'oracle': 'Oracle'
        }
        
        # Category mapping for proper hierarchy
        self.category_mapping = {
            'routers': 'Networking',
            'switches': 'Networking', 
            'firewalls': 'Security',
            'wireless': 'Networking',
            'servers': 'Servers',
            'storages': 'Storage',
            'ip phones': 'Unified Communications',
            'accessories': 'Networking',
            'optical network': 'Optical Network'
        }
        
        print("Comprehensive Category Scraper")
        print("Focus: Extract ALL categories with proper hierarchy")
        print("Enhanced with human-like browsing patterns")
    
    def setup_human_like_session(self):
        """Setup session with realistic human-like headers and behavior"""
        try:
            # Rotate user agents to look like different users
            user_agent = self.ua.random
            
            # Realistic headers that mimic a real browser
            self.session.headers.update({
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'max-age=0',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            })
            
            # Disable SSL verification for problematic sites
            self.session.verify = False
            
            print(f"Human-like session initialized with User-Agent: {user_agent[:50]}...")
            
        except Exception as e:
            print(f"Warning: Could not setup advanced headers: {e}")
            # Fallback to basic headers
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
    
    def _init_browsing_patterns(self):
        """Initialize realistic browsing patterns"""
        return {
            'page_load_times': [2.5, 4.2, 3.8, 5.1, 2.9, 4.7, 3.3, 4.8, 3.6, 4.0],
            'reading_times': [8.5, 12.3, 15.7, 9.2, 11.8, 13.4, 10.6, 14.2, 7.9, 16.1],
            'click_delays': [0.8, 1.2, 1.5, 0.9, 1.3, 1.1, 1.4, 0.7, 1.6, 1.0],
            'scroll_pauses': [0.3, 0.7, 0.5, 0.9, 0.4, 0.8, 0.6, 0.2, 1.0, 0.5]
        }
    
    def human_like_delay(self, delay_type='page_load'):
        """Add human-like delays based on browsing patterns"""
        if delay_type == 'page_load':
            delay = random.choice(self.browsing_patterns['page_load_times'])
        elif delay_type == 'reading':
            delay = random.choice(self.browsing_patterns['reading_times'])
        elif delay_type == 'click':
            delay = random.choice(self.browsing_patterns['click_delays'])
        elif delay_type == 'scroll':
            delay = random.choice(self.browsing_patterns['scroll_pauses'])
        else:
            delay = random.uniform(1.0, 3.0)
        
        # Add some randomness to make it more human-like
        delay += random.uniform(-0.5, 0.5)
        delay = max(0.5, delay)  # Minimum delay
        
        print(f"  Human-like {delay_type} delay: {delay:.1f}s")
        time.sleep(delay)
    
    def simulate_human_browsing(self, url, action='browsing'):
        """Simulate human browsing behavior"""
        self.request_count += 1
        current_time = time.time()
        
        # Simulate reading time based on session length
        session_duration = current_time - self.session_start_time
        
        if action == 'first_visit':
            # First visit - take time to explore
            self.human_like_delay('reading')
        elif action == 'category_browse':
            # Browsing categories - moderate time
            self.human_like_delay('page_load')
        elif action == 'product_view':
            # Viewing products - longer time
            self.human_like_delay('reading')
        else:
            # Default browsing
            self.human_like_delay('page_load')
        
        # Simulate occasional longer pauses (like human distraction)
        if random.random() < 0.15:  # 15% chance
            distraction_delay = random.uniform(3.0, 8.0)
            print(f"  Human distraction pause: {distraction_delay:.1f}s")
            time.sleep(distraction_delay)
        
        # Simulate session breaks for longer sessions
        if session_duration > 300 and random.random() < 0.1:  # 10% chance after 5 minutes
            break_delay = random.uniform(10.0, 30.0)
            print(f"  Human break: {break_delay:.1f}s")
            time.sleep(break_delay)
    
    def make_human_like_request(self, url, max_retries=3, action='browsing'):
        """Make HTTP request with human-like behavior"""
        for attempt in range(max_retries):
            try:
                # Simulate human browsing before request
                self.simulate_human_browsing(url, action)
                
                print(f"  Making human-like request to: {url} (attempt {attempt + 1})")
                
                # Add realistic timeout
                timeout = random.uniform(25, 35)
                
                response = self.session.get(url, timeout=timeout)
                
                if response.status_code == 200:
                    print(f"  Success: {len(response.text):,} chars received")
                    
                    # Simulate human reading time based on content length
                    content_length = len(response.text)
                    if content_length > 50000:
                        self.human_like_delay('reading')
                    elif content_length > 20000:
                        self.human_like_delay('page_load')
                    else:
                        self.human_like_delay('click')
                    
                    return response
                    
                elif response.status_code == 403:
                    print(f"  Access denied (403) - simulating human retry behavior")
                    if attempt < max_retries - 1:
                        # Longer delay for 403 errors (like human would wait)
                        retry_delay = random.uniform(15, 25)
                        print(f"  Human-like retry delay: {retry_delay:.1f}s")
                        time.sleep(retry_delay)
                        continue
                        
                elif response.status_code == 429:
                    print(f"  Rate limited (429) - simulating human patience")
                    if attempt < max_retries - 1:
                        # Much longer delay for rate limiting
                        retry_delay = random.uniform(30, 60)
                        print(f"  Human-like patience delay: {retry_delay:.1f}s")
                        time.sleep(retry_delay)
                        continue
                        
                else:
                    print(f"  HTTP {response.status_code} - simulating human retry")
                    if attempt < max_retries - 1:
                        retry_delay = random.uniform(5, 10)
                        time.sleep(retry_delay)
                        continue
                        
            except Exception as e:
                print(f"  Request error: {e}")
                if attempt < max_retries - 1:
                    # Simulate human retry behavior
                    retry_delay = random.uniform(3, 8)
                    print(f"  Human-like error retry delay: {retry_delay:.1f}s")
                    time.sleep(retry_delay)
                    continue
        
        return None
    
    def rotate_user_agent(self):
        """Rotate user agent to look like different users"""
        try:
            new_ua = self.ua.random
            self.session.headers.update({'User-Agent': new_ua})
            print(f"  Rotated to new User-Agent: {new_ua[:50]}...")
        except Exception as e:
            print(f"  Warning: Could not rotate User-Agent: {e}")
    
    def simulate_mouse_movements(self):
        """Simulate mouse movements and scrolling"""
        # Simulate scrolling behavior
        scroll_pauses = random.randint(2, 5)
        for i in range(scroll_pauses):
            self.human_like_delay('scroll')
        
        # Simulate mouse hover behavior
        hover_delay = random.uniform(0.5, 1.5)
        time.sleep(hover_delay)
    
    def run_combined_scraper(self, fast_mode=False):
        """Run hierarchy + comprehensive product scraping and save in one file"""
        try:
            print("="*80)
            print("COMBINED MODE: Hierarchy + Products")
            if fast_mode:
                print("FAST MODE: Reduced limits and delays")
            print("Enhanced with human-like browsing patterns")
            print("="*80)
            
            # Simulate human starting to browse
            print("Simulating human browsing behavior...")
            self.simulate_human_browsing(self.base_url, action='first_visit')
            
            # Fast mode: reduce limits and delays
            if fast_mode:
                hierarchy_rows = self.scrape_category_hierarchy_fast()
                products = self.create_sample_products()  # No HTTP requests
            else:
                hierarchy_rows = self.scrape_category_hierarchy()
                products = self.scrape_all_categories_comprehensive(max_products_per_category=50)
            
            self.save_combined_results(hierarchy_rows, products)
            print(f"Combined rows -> hierarchy: {len(hierarchy_rows)}, products: {len(products)}")
        except Exception as e:
            print(f"Combined scraper failed: {str(e)}")
            import traceback
            traceback.print_exc()

    def scrape_category_hierarchy_fast(self):
        """Ultra-fast version - no HTTP requests, no delays"""
        print("Starting ULTRA-FAST category hierarchy scraping...")
        
        # Just return the 6 main categories without any HTTP requests
        hierarchy_rows = [
            {'category 1': 'Routers', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/routers-price.html'},
            {'category 1': 'Switches', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/switches-price.html'},
            {'category 1': 'Firewalls', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/firewalls-price.html'},
            {'category 1': 'Wireless', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/wireless-price.html'},
            {'category 1': 'Servers', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/servers-price.html'},
            {'category 1': 'Storages', 'category 2': '', 'category 3': '', 'url': 'https://www.router-switch.com/storages-price.html'}
        ]
        
        print(f"Ultra-fast hierarchy rows: {len(hierarchy_rows)}")
        return hierarchy_rows

    def create_sample_products(self):
        """Create sample products without HTTP requests"""
        print("Creating sample products (no HTTP requests)...")
        
        sample_products = [
            {
                "Product Link": "https://www.router-switch.com/sample-router.html",
                "product": "Cisco ISR 4331 Router",
                "price": "$2,500",
                "Call For Price": "",
                "SKU": "ISR4331",
                "Brand": "Cisco",
                "Condition": "New",
                "Availability": "Check Availability",
                "Warranty": "1 Year Limited Warranty",
                "Product Description": "Cisco | Model: ISR4331",
                "image": "",
                "category 1": "Routers",
                "category 2": "Enterprise Routers",
                "category 3": "Cisco Routers"
            },
            {
                "Product Link": "https://www.router-switch.com/sample-switch.html",
                "product": "Cisco Catalyst 9300 Switch",
                "price": "$3,200",
                "Call For Price": "",
                "SKU": "C9300-48P",
                "Brand": "Cisco",
                "Condition": "New",
                "Availability": "Check Availability",
                "Warranty": "1 Year Limited Warranty",
                "Product Description": "Cisco | Model: C9300-48P",
                "image": "",
                "category 1": "Switches",
                "category 2": "Access Switches",
                "category 3": "Cisco Switches"
            },
            {
                "Product Link": "https://www.router-switch.com/sample-firewall.html",
                "product": "Fortinet FortiGate 60E Firewall",
                "price": "$1,800",
                "Call For Price": "",
                "SKU": "FG-60E",
                "Brand": "Fortinet",
                "Condition": "New",
                "Availability": "Check Availability",
                "Warranty": "1 Year Limited Warranty",
                "Product Description": "Fortinet | Model: FG-60E",
                "image": "",
                "category 1": "Firewalls",
                "category 2": "UTM Firewalls",
                "category 3": "Fortinet Firewalls"
            }
        ]
        
        print(f"Created {len(sample_products)} sample products")
        return sample_products

    def scrape_category_hierarchy(self):
        """Scrape Category 2 and Category 3 under the six root categories"""
        print("Starting category hierarchy scraping (Category 1 -> 2 -> 3)...")

        roots = self._get_fixed_root_categories()
        hierarchy_rows = []

        for root in roots:
            cat1_name = root['name']
            cat1_url = root['url']

            print(f"\n{'='*60}")
            print(f"Category 1: {cat1_name} -> {cat1_url}")
            print(f"{'='*60}")

            # Discover Category 2 (subcategories)
            subcategories = self.discover_subcategories(cat1_url, cat1_name)

            # If no explicit subcategories, record the Cat1 only row for completeness
            if not subcategories:
                hierarchy_rows.append({
                    'category 1': cat1_name,
                    'category 2': '',
                    'category 3': '',
                    'url': cat1_url
                })
                continue

            for sub in subcategories:
                cat2_name = sub['name']
                cat2_url = sub['url']

                # Always store Cat1 -> Cat2
                hierarchy_rows.append({
                    'category 1': cat1_name,
                    'category 2': cat2_name,
                    'category 3': '',
                    'url': cat2_url
                })

                # Discover Category 3 under this subcategory
                product_types = self.discover_product_types(cat2_url, cat2_name, cat1_name)
                for ptype in product_types:
                    hierarchy_rows.append({
                        'category 1': cat1_name,
                        'category 2': cat2_name,
                        'category 3': ptype['name'],
                        'url': ptype['url']
                    })

                self.human_like_delay('click')

            self.human_like_delay('reading')
            
            # Occasionally rotate user agent to look like different users
            if random.random() < 0.2:  # 20% chance
                self.rotate_user_agent()

        print(f"\nHierarchy rows collected: {len(hierarchy_rows)}")
        return hierarchy_rows

    def _get_fixed_root_categories(self):
        """Return the six fixed Category 1 roots with their likely landing URLs"""
        return [
            { 'name': 'Routers',   'url': f"{self.base_url}/routers-price.html" },
            { 'name': 'Switches',  'url': f"{self.base_url}/switches-price.html" },
            { 'name': 'Firewalls', 'url': f"{self.base_url}/firewalls-price.html" },
            { 'name': 'Wireless',  'url': f"{self.base_url}/wireless-price.html" },
            { 'name': 'Servers',   'url': f"{self.base_url}/servers-price.html" },
            { 'name': 'Storages',  'url': f"{self.base_url}/storages-price.html" },
        ]

    def save_category_hierarchy_results(self, rows):
        """Save hierarchy rows to JSON and Excel"""
        if not rows:
            print("No hierarchy to save")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        json_filename = f"category_hierarchy_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(rows, f, indent=2, ensure_ascii=False)

        excel_filename = f"category_hierarchy_{timestamp}.xlsx"
        try:
            df = pd.DataFrame(rows)
            with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Hierarchy', index=False)

                # Simple counts per level
                if {'category 1'} <= set(df.columns):
                    c1 = df.groupby('category 1').size().reset_index(name='Count')
                    c1.to_excel(writer, sheet_name='Category1 Counts', index=False)
                if {'category 1', 'category 2'} <= set(df.columns):
                    c2 = df.groupby(['category 1', 'category 2']).size().reset_index(name='Count')
                    c2.to_excel(writer, sheet_name='Category2 Counts', index=False)
                if {'category 1', 'category 2', 'category 3'} <= set(df.columns):
                    c3 = df.groupby(['category 1', 'category 2', 'category 3']).size().reset_index(name='Count')
                    c3.to_excel(writer, sheet_name='Category3 Counts', index=False)

            print(f"Excel file saved: {excel_filename}")
        except Exception as e:
            print(f"Error saving hierarchy Excel: {str(e)}")
            print("JSON file saved successfully")

    def save_combined_results(self, hierarchy_rows, product_rows):
        """Save both hierarchy and products into one JSON and one Excel"""
        if not hierarchy_rows and not product_rows:
            print("No data to save")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        combined = {
            'hierarchy': hierarchy_rows or [],
            'products': product_rows or []
        }

        json_filename = f"combined_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(combined, f, indent=2, ensure_ascii=False)

        excel_filename = f"combined_{timestamp}.xlsx"
        try:
            with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
                if product_rows:
                    df_products = pd.DataFrame(product_rows)
                    df_products.to_excel(writer, sheet_name='Products', index=False)

                    # Summaries
                    cols = df_products.columns
                    if {'category 1'} <= set(cols):
                        df_products.groupby('category 1').size().reset_index(name='Count').to_excel(writer, sheet_name='Cat1 Products', index=False)
                    if {'category 1','category 2'} <= set(cols):
                        df_products.groupby(['category 1','category 2']).size().reset_index(name='Count').to_excel(writer, sheet_name='Cat2 Products', index=False)
                    if {'category 1','category 2','category 3'} <= set(cols):
                        df_products.groupby(['category 1','category 2','category 3']).size().reset_index(name='Count').to_excel(writer, sheet_name='Cat3 Products', index=False)
                    if 'Brand' in cols:
                        df_products.groupby('Brand').size().reset_index(name='Count').to_excel(writer, sheet_name='Brand Products', index=False)

                if hierarchy_rows:
                    df_h = pd.DataFrame(hierarchy_rows)
                    df_h.to_excel(writer, sheet_name='Hierarchy', index=False)
                    cols_h = df_h.columns
                    if {'category 1'} <= set(cols_h):
                        df_h.groupby('category 1').size().reset_index(name='Count').to_excel(writer, sheet_name='Cat1 Hierarchy', index=False)
                    if {'category 1','category 2'} <= set(cols_h):
                        df_h.groupby(['category 1','category 2']).size().reset_index(name='Count').to_excel(writer, sheet_name='Cat2 Hierarchy', index=False)
                    if {'category 1','category 2','category 3'} <= set(cols_h):
                        df_h.groupby(['category 1','category 2','category 3']).size().reset_index(name='Count').to_excel(writer, sheet_name='Cat3 Hierarchy', index=False)

            print(f"Combined Excel saved: {excel_filename}")
            print(f"Combined JSON saved: {json_filename}")
        except Exception as e:
            print(f"Error saving combined Excel: {str(e)}")
            print(f"Combined JSON saved: {json_filename}")

    def discover_all_categories(self):
        """Discover all categories from the main navigation"""
        print("Discovering all categories from main navigation...")
        
        try:
            response = self.make_human_like_request(self.base_url, action='first_visit')
            if not response:
                print(f"Failed to access main page")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            categories = []
            
            # Method 1: Look for main navigation menu
            nav_links = soup.find_all('a', href=True)
            
            for link in nav_links:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                # Check if this is a main category link
                if self._is_main_category_link(href, text):
                    category_url = urljoin(self.base_url, href)
                    category_info = {
                        'name': text,
                        'url': category_url,
                        'level': 1
                    }
                    categories.append(category_info)
                    print(f"Found main category: {text} -> {category_url}")
            
            # Method 2: Look for category patterns in URLs
            category_patterns = [
                'routers', 'switches', 'firewalls', 'wireless', 'servers', 
                'storages', 'ip-phones', 'accessories', 'optical-network'
            ]
            
            for pattern in category_patterns:
                category_url = f"{self.base_url}/{pattern}-price.html"
                category_info = {
                    'name': pattern.replace('-', ' ').title(),
                    'url': category_url,
                    'level': 1
                }
                categories.append(category_info)
                print(f"Added pattern category: {category_info['name']} -> {category_url}")
            
            # Remove duplicates
            seen_urls = set()
            unique_categories = []
            for cat in categories:
                if cat['url'] not in seen_urls:
                    seen_urls.add(cat['url'])
                    unique_categories.append(cat)
            
            print(f"Total unique main categories found: {len(unique_categories)}")
            return unique_categories
            
        except Exception as e:
            print(f"Error discovering categories: {str(e)}")
            return []
    
    def _is_main_category_link(self, href, text):
        """Check if link is a main category"""
        if not href or not text:
            return False
        
        # Look for category indicators in URL
        category_indicators = ['routers', 'switches', 'firewalls', 'wireless', 'servers', 'storages']
        href_lower = href.lower()
        
        if any(indicator in href_lower for indicator in category_indicators):
            return True
        
        # Look for category indicators in text
        text_lower = text.lower()
        if any(indicator in text_lower for indicator in category_indicators):
            return True
        
        return False
    
    def discover_subcategories(self, main_category_url, main_category_name):
        """Discover subcategories for a main category"""
        print(f"Discovering subcategories for: {main_category_name}")
        
        try:
            response = self.make_human_like_request(main_category_url, action='category_browse')
            if not response:
                print(f"Failed to access {main_category_name}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            subcategories = []
            
            # Look for subcategory links
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                if self._is_subcategory_link(href, text, main_category_name):
                    subcategory_url = urljoin(main_category_url, href)
                    subcategory_info = {
                        'name': text,
                        'url': subcategory_url,
                        'parent': main_category_name,
                        'level': 2
                    }
                    subcategories.append(subcategory_info)
                    print(f"  Found subcategory: {text} -> {subcategory_url}")
            
            print(f"Total subcategories found for {main_category_name}: {len(subcategories)}")
            return subcategories
            
        except Exception as e:
            print(f"Error discovering subcategories for {main_category_name}: {str(e)}")
            return []
    
    def _is_subcategory_link(self, href, text, parent_category):
        """Check if link is a subcategory"""
        if not href or not text or len(text) < 3:
            return False
        
        # Skip if it's the same as parent
        if text.lower() == parent_category.lower():
            return False
        
        # Look for category patterns
        href_lower = href.lower()
        text_lower = text.lower()
        
        # Should contain category-related terms
        category_terms = ['router', 'switch', 'server', 'firewall', 'wireless', 'storage']
        if not any(term in text_lower for term in category_terms):
            return False
        
        # Should be a category page (not individual product)
        if any(indicator in href_lower for indicator in ['product', 'item', 'detail']):
            return False
        
        return True
    
    def discover_product_types(self, subcategory_url, subcategory_name, parent_category):
        """Discover product types for a subcategory"""
        print(f"Discovering product types for: {subcategory_name}")
        
        try:
            response = self.make_human_like_request(subcategory_url, action='category_browse')
            if not response:
                print(f"Failed to access {subcategory_name}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            product_types = []
            
            # Look for product type links
            links = soup.find_all('a', href=True)
            
            for link in links:
                href = link.get('href', '')
                text = link.get_text(strip=True)
                
                if self._is_product_type_link(href, text, subcategory_name):
                    product_type_url = urljoin(subcategory_url, href)
                    product_type_info = {
                        'name': text,
                        'url': product_type_url,
                        'parent': subcategory_name,
                        'grandparent': parent_category,
                        'level': 3
                    }
                    product_types.append(product_type_info)
                    print(f"    Found product type: {text} -> {product_type_url}")
            
            print(f"Total product types found for {subcategory_name}: {len(product_types)}")
            return product_types
            
        except Exception as e:
            print(f"Error discovering product types for {subcategory_name}: {str(e)}")
            return []
    
    def _is_product_type_link(self, href, text, parent_subcategory):
        """Check if link is a product type"""
        if not href or not text or len(text) < 5:
            return False
        
        # Skip if it's the same as parent
        if text.lower() == parent_subcategory.lower():
            return False
        
        # Look for brand names or specific product series
        text_lower = text.lower()
        href_lower = href.lower()
        
        # Should contain brand or model indicators
        brand_indicators = ['cisco', 'huawei', 'dell', 'hpe', 'juniper', 'aruba']
        model_indicators = ['ar2200', 'catalyst', 'poweredge', 'proliant', 'netengine']
        
        has_brand = any(brand in text_lower for brand in brand_indicators)
        has_model = any(model in text_lower for model in model_indicators)
        
        if not (has_brand or has_model):
            return False
        
        # Should be a category page (not individual product)
        if any(indicator in href_lower for indicator in ['product', 'item', 'detail']):
            return False
        
        return True
    
    def scrape_all_categories_comprehensive(self, max_products_per_category=100):
        """Comprehensive scraping of all categories with proper hierarchy"""
        print("Starting comprehensive category scraping...")
        print("Using human-like browsing patterns to avoid detection...")
        
        all_products = []
        
        # Simulate human browsing behavior
        self.simulate_human_browsing(self.base_url, action='first_visit')
        
        # Step 1: Discover all main categories
        main_categories = self.discover_all_categories()
        
        if not main_categories:
            print("No main categories found!")
            return []
        
        print(f"\nFound {len(main_categories)} main categories")
        
        # Step 2: For each main category, discover subcategories and product types
        for i, main_cat in enumerate(main_categories):
            if len(all_products) >= max_products_per_category * len(main_categories):
                break
                
            print(f"\n{'='*60}")
            print(f"Processing main category {i+1}/{len(main_categories)}: {main_cat['name']}")
            print(f"{'='*60}")
            
            # Discover subcategories
            subcategories = self.discover_subcategories(main_cat['url'], main_cat['name'])
            
            if not subcategories:
                # If no subcategories, try to scrape products directly from main category
                print(f"No subcategories found for {main_cat['name']}, scraping directly...")
                products = self._scrape_products_from_category(
                    main_cat['url'], 
                    main_cat['name'], 
                    main_cat['name'], 
                    main_cat['name']
                )
                all_products.extend(products)
                continue
            
            # Step 3: For each subcategory, discover product types
            for j, subcat in enumerate(subcategories):
                if len(all_products) >= max_products_per_category * len(main_categories):
                    break
                    
                print(f"\nProcessing subcategory {j+1}/{len(subcategories)}: {subcat['name']}")
                
                # Discover product types
                product_types = self.discover_product_types(subcat['url'], subcat['name'], main_cat['name'])
                
                if not product_types:
                    # If no product types, try to scrape products directly from subcategory
                    print(f"No product types found for {subcat['name']}, scraping directly...")
                    products = self._scrape_products_from_category(
                        subcat['url'], 
                        main_cat['name'], 
                        subcat['name'], 
                        subcat['name']
                    )
                    all_products.extend(products)
                    continue
                
                # Step 4: For each product type, scrape individual products
                for k, product_type in enumerate(product_types):
                    if len(all_products) >= max_products_per_category * len(main_categories):
                        break
                        
                    print(f"\nProcessing product type {k+1}/{len(product_types)}: {product_type['name']}")
                    
                    # Scrape products from this product type
                    products = self._scrape_products_from_category(
                        product_type['url'], 
                        main_cat['name'], 
                        subcat['name'], 
                        product_type['name']
                    )
                    all_products.extend(products)
                    
                    # Human-like rate limiting
                    self.human_like_delay('click')
            
            # Human-like rate limiting between main categories
            self.human_like_delay('reading')
            
            # Occasionally rotate user agent
            if random.random() < 0.15:  # 15% chance
                self.rotate_user_agent()
        
        # Clean and deduplicate products
        final_products = self._clean_products_comprehensive(all_products)
        
        print(f"\n{'='*60}")
        print(f"COMPREHENSIVE SCRAPING COMPLETE!")
        print(f"Total products found: {len(final_products)}")
        print(f"{'='*60}")
        
        return final_products
    
    def _scrape_products_from_category(self, category_url, category1, category2, category3):
        """Scrape products from a specific category page"""
        print(f"    Scraping products from: {category_url}")
        
        try:
            response = self.make_human_like_request(category_url, action='product_view')
            if not response:
                print(f"    Failed to access category")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            products = []
            
            # Method 1: Extract from tables
            table_products = self._extract_from_tables_enhanced(soup, category_url, category1, category2, category3)
            products.extend(table_products)
            
            # Method 2: Extract from product links
            link_products = self._extract_from_product_links(soup, category_url, category1, category2, category3)
            products.extend(link_products)
            
            # Method 3: Extract from text content
            text_products = self._extract_clean_products_from_text(soup, category_url, category1, category2, category3)
            products.extend(text_products)
            
            # Add images
            products_with_images = self._add_images_to_products(products, soup, category_url)
            
            # Simulate human behavior after finding products
            if products_with_images:
                self.simulate_mouse_movements()
                print(f"    Found {len(products_with_images)} products")
            else:
                print(f"    No products found - simulating human disappointment")
                self.human_like_delay('click')
            
            return products_with_images
            
        except Exception as e:
            print(f"    Error scraping category: {str(e)}")
            return []
    
    def _extract_from_product_links(self, soup, source_url, category1, category2, category3):
        """Extract products from individual product links"""
        products = []
        
        # Look for product links
        product_links = soup.find_all('a', href=True)
        
        processed_links = 0
        for link in product_links:
            if processed_links >= 20:  # Limit to avoid too many requests
                break
                
            href = link.get('href')
            text = link.get_text(strip=True)
            
            # Check if this looks like a product page link
            if self._is_product_page_link(href, text):
                product_page_url = urljoin(source_url, href)
                
                try:
                    # Visit individual product page
                    response = self.make_human_like_request(product_page_url, action='product_view')
                    
                    if response:
                        page_soup = BeautifulSoup(response.text, 'html.parser')
                        
                        # Extract product details from individual page
                        product_details = self._extract_from_product_page(page_soup, product_page_url, category1, category2, category3)
                        
                        if product_details:
                            products.append(product_details)
                    
                    processed_links += 1
                    self.human_like_delay('click')  # Human-like rate limiting for individual pages
                    
                except Exception as e:
                    continue
        
        return products
    
    def get_working_category_urls(self):
        """Get working category URLs for price-focused scraping"""
        return [
            f"{self.base_url}/routers-price.html",
            f"{self.base_url}/switches-price.html",
            f"{self.base_url}/firewalls-price.html",
            f"{self.base_url}/wireless-price.html",
            f"{self.base_url}/servers-price.html",
            f"{self.base_url}/storages-price.html"
        ]
    
    def scrape_with_price_focus(self, max_products=1000):
        """Scrape focusing on price extraction and clean product names"""
        print("Starting price-focused scraping...")
        print("Using human-like browsing patterns to avoid detection...")
        
        working_urls = self.get_working_category_urls()
        all_products = []
        
        # Simulate human browsing behavior
        self.simulate_human_browsing(self.base_url, action='first_visit')
        
        for i, url in enumerate(working_urls):
            if len(all_products) >= max_products:
                break
            
            print(f"\nCategory {i+1}/{len(working_urls)}: {url.split('/')[-1]}")
            
            try:
                response = self.make_human_like_request(url, action='category_browse')
                
                if response:
                    print(f"  Success: {len(response.text):,} chars")
                    
                    # Extract products with enhanced price and name cleaning
                    products = self._extract_products_with_price_focus(response.text, url)
                    
                    if products:
                        all_products.extend(products)
                        print(f"  Extracted: {len(products)} products")
                        print(f"  Total so far: {len(all_products)}")
                        
                        # Show price statistics for this category
                        with_prices = sum(1 for p in products if p.get('price'))
                        print(f"  Prices found: {with_prices}/{len(products)} ({with_prices/len(products)*100:.1f}%)")
                    else:
                        print(f"  No products extracted")
                else:
                    print(f"  Failed: HTTP {response.status_code}")
                    
            except Exception as e:
                print(f"  Error: {str(e)}")
            
            # Human-like rate limiting
            self.human_like_delay('reading')
            
            # Occasionally rotate user agent
            if random.random() < 0.1:  # 10% chance
                self.rotate_user_agent()
        
        # Clean and deduplicate
        final_products = self._clean_products_comprehensive(all_products)
        
        print(f"\nFinal results after cleaning: {len(final_products)} products")
        return final_products
    
    def _extract_products_with_price_focus(self, html_content, source_url):
        """Enhanced extraction focusing on prices and clean names"""
        soup = BeautifulSoup(html_content, 'html.parser')
        products = []
        
        # Strategy 1: Enhanced table extraction with aggressive price search
        table_products = self._extract_from_tables_enhanced(soup, source_url)
        products.extend(table_products)
        
        # Strategy 2: Individual product page extraction (higher price success rate)
        individual_products = self._extract_from_individual_pages(soup, source_url)
        products.extend(individual_products)
        
        # Strategy 3: Clean concatenated product text
        text_products = self._extract_clean_products_from_text(soup, source_url)
        products.extend(text_products)
        
        # Add images to all products
        products_with_images = self._add_images_to_products(products, soup, source_url)
        
        return products_with_images
    
    def _extract_from_tables_enhanced(self, soup, source_url, category1=None, category2=None, category3=None):
        """Enhanced table extraction with aggressive price searching"""
        products = []
        tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) < 1:
                    continue
                
                # Get product text from first cell
                product_text = cells[0].get_text(strip=True)
                
                # Clean and split concatenated products
                clean_products = self._clean_concatenated_products(product_text)
                
                for clean_product in clean_products:
                    if self._is_valid_product_name(clean_product):
                        
                        # Aggressive price search across ALL cells and nearby content
                        price = self._find_price_aggressively(row, soup)
                        
                        # Get product link
                        product_link = self._get_product_link_from_element(cells[0], source_url)
                        
                        # Create product
                        product = self._create_product_object(
                            clean_product, price, product_link, source_url, category1, category2, category3
                        )
                        
                        products.append(product)
        
        return products
    
    def _extract_from_individual_pages(self, soup, source_url):
        """Try to find individual product pages (often have prices)"""
        products = []
        
        # Look for links to individual product pages
        product_links = soup.find_all('a', href=True)
        
        processed_links = 0
        for link in product_links:
            if processed_links >= 10:  # Limit to avoid too many requests
                break
                
            href = link.get('href')
            text = link.get_text(strip=True)
            
            # Check if this looks like a product page link
            if self._is_product_page_link(href, text):
                product_page_url = urljoin(source_url, href)
                
                print(f"    Checking product page: {href}")
                
                try:
                    # Visit individual product page
                    response = self.make_human_like_request(product_page_url, action='product_view')
                    
                    if response:
                        page_soup = BeautifulSoup(response.text, 'html.parser')
                        
                        # Extract product details from individual page
                        product_details = self._extract_from_product_page(page_soup, product_page_url)
                        
                        if product_details:
                            products.append(product_details)
                            print(f"      Found product with details")
                            
                            # Check if we found a price
                            if product_details.get('price'):
                                print(f"      Price found: {product_details['price']}")
                    
                    processed_links += 1
                    self.human_like_delay('reading')  # Human-like rate limiting for individual pages
                    
                except Exception as e:
                    print(f"      Error accessing page: {str(e)}")
                    continue
        
        return products
    
    def _extract_clean_products_from_text(self, soup, source_url, category1=None, category2=None, category3=None):
        """Extract clean products from text content"""
        products = []
        
        # Get all text and clean it
        text_content = soup.get_text()
        
        # Remove JavaScript disabled message and navigation
        text_content = self._clean_page_text(text_content)
        
        # Extract products using enhanced patterns
        product_patterns = [
            r'((?:Cisco|Huawei|Dell|HPE|Juniper|Aruba)\s+[A-Z\d][^\n]{10,80})',
            r'([A-Z]{2,}\d+[A-Z\d\-]*\s+[^\n]{10,60})',
            r'(NetEngine\s+[^\n]{5,40})',
            r'(Catalyst\s+[^\n]{5,40})',
            r'(PowerEdge\s+[^\n]{5,40})',
            r'(ProLiant\s+[^\n]{5,40})'
        ]
        
        for pattern in product_patterns:
            matches = re.findall(pattern, text_content, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                clean_match = re.sub(r'\s+', ' ', match.strip())
                if self._is_valid_product_name(clean_match):
                    
                    # Look for price near this product mention
                    price = self._find_price_near_text(clean_match, text_content)
                    
                    product = self._create_product_object(
                        clean_match, price, source_url, source_url, category1, category2, category3
                    )
                    products.append(product)
        
        return products
    
    def _clean_concatenated_products(self, text):
        """Clean concatenated product names like your sample"""
        if not text or len(text) < 10:
            return []
        
        # Remove JavaScript disabled message and common navigation text
        clean_text = self._clean_page_text(text)
        
        if len(clean_text) < 10:
            return []
        
        products = []
        
        # Method 1: Split by product series names
        series_patterns = [
            r'(Cisco\s+[A-Z\d\-\s]+(?:Router|Switch|Server)s?)',
            r'(Huawei\s+[A-Z\d\-\s]+(?:Router|Switch|Server)s?)',
            r'(Dell\s+[A-Z\d\-\s]+(?:Router|Switch|Server)s?)',
            r'([A-Z]{2,}\d+[A-Z\d\-]*\s+[A-Za-z\s]{5,40})',
        ]
        
        for pattern in series_patterns:
            matches = re.findall(pattern, clean_text, re.IGNORECASE)
            for match in matches:
                clean_match = re.sub(r'\s+', ' ', match.strip())
                if 10 <= len(clean_match) <= 80:
                    products.append(clean_match)
        
        # Method 2: Split by brand transitions
        brand_transitions = r'(Cisco|Huawei|Dell|HPE|Juniper|Aruba)'
        parts = re.split(brand_transitions, clean_text)
        
        current_brand = ""
        for part in parts:
            part = part.strip()
            if part in ['Cisco', 'Huawei', 'Dell', 'HPE', 'Juniper', 'Aruba']:
                current_brand = part
            elif current_brand and len(part) > 10:
                # Take first reasonable chunk after brand
                lines = part.split('\n')
                for line in lines:
                    line = line.strip()
                    if 10 <= len(line) <= 80 and not self._is_navigation_text(line):
                        product_name = f"{current_brand} {line}".strip()
                        if len(product_name) <= 80:
                            products.append(product_name)
                            break
        
        # If no good splits, try to extract first reasonable product name
        if not products:
            lines = clean_text.split('\n')
            for line in lines:
                line = line.strip()
                if self._looks_like_single_product(line):
                    products.append(line)
                    break
        
        return products[:5]  # Limit to 5 products per text block
    
    def _clean_page_text(self, text):
        """Remove navigation and JavaScript disabled messages"""
        if not text:
            return ""
        
        # Remove common navigation and header text
        remove_patterns = [
            r'JavaScript seems to be disabled.*?turn on Javascript in your browser\.',
            r'Express shipping to.*?Contact Us.*?Track Order',
            r'USD.*?AED.*?English.*?العربية.*?日本語.*?한국어.*?Polski.*?Slovenčina.*?Kiswahili',
            r'Router-Switch\.com.*?Shop By Categories',
            r'Contact Us.*?Track Order',
            r'Shop By Categories.*?Routers',
            r'USD.*?CHF.*?AED',
            r'English.*?Kiswahili'
        ]
        
        clean_text = text
        for pattern in remove_patterns:
            clean_text = re.sub(pattern, '', clean_text, flags=re.DOTALL | re.IGNORECASE)
        
        # Remove excessive whitespace
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_text = re.sub(r'\n\s*\n', '\n', clean_text)
        
        return clean_text.strip()
    
    def _is_navigation_text(self, text):
        """Check if text is navigation/header content"""
        nav_indicators = [
            'shop by categories', 'contact us', 'track order', 'express shipping',
            'javascript', 'browser', 'usd', 'aud', 'gbp', 'english', 'español',
            'router-switch.com', 'disabled', 'currency', 'language'
        ]
        
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in nav_indicators)
    
    def _looks_like_single_product(self, text):
        """Check if text looks like a single product name"""
        if not text or len(text) < 10 or len(text) > 100:
            return False
        
        # Must have brand or model number
        has_brand = any(brand in text.lower() for brand in self.brands.keys())
        has_model = bool(re.search(r'\b[A-Z]{2,}\d+\b', text.upper()))
        has_product_type = any(ptype in text.lower() for ptype in 
                              ['router', 'switch', 'server', 'firewall'])
        
        # Shouldn't have navigation text
        if self._is_navigation_text(text):
            return False
        
        return has_brand or has_model or has_product_type
    
    def _find_price_aggressively(self, row_element, soup):
        """Aggressively search for prices in and around an element"""
        
        # Strategy 1: Check all cells in the row
        if row_element:
            cells = row_element.find_all(['td', 'th'])
            for cell in cells:
                price = self._extract_price_from_text(cell.get_text())
                if price:
                    return price
        
        # Strategy 2: Check parent and sibling elements
        if row_element and row_element.parent:
            parent_text = row_element.parent.get_text()
            price = self._extract_price_from_text(parent_text)
            if price:
                return price
        
        # Strategy 3: Look for price in nearby elements
        if row_element:
            # Check next few siblings
            next_elem = row_element.find_next_sibling()
            for _ in range(3):
                if next_elem:
                    price = self._extract_price_from_text(next_elem.get_text())
                    if price:
                        return price
                    next_elem = next_elem.find_next_sibling()
        
        return ""
    
    def _find_price_near_text(self, product_text, full_text):
        """Find price near product mention in text"""
        # Find position of product in text
        product_pos = full_text.find(product_text)
        if product_pos == -1:
            return ""
        
        # Check text around the product mention (500 chars before and after)
        start = max(0, product_pos - 500)
        end = min(len(full_text), product_pos + len(product_text) + 500)
        
        surrounding_text = full_text[start:end]
        
        return self._extract_price_from_text(surrounding_text)
    
    def _extract_price_from_text(self, text):
        """Extract price from text using comprehensive patterns"""
        if not text:
            return ""
        
        # Comprehensive price patterns
        price_patterns = [
            r'\$[\d,]+\.?\d*',                      # $1,234.56
            r'USD\s*[\d,]+\.?\d*',                  # USD 1234
            r'[\d,]+\.?\d*\s*USD',                  # 1234 USD
            r'Price:\s*\$?[\d,]+\.?\d*',            # Price: $1234
            r'Cost:\s*\$?[\d,]+\.?\d*',             # Cost: $1234
            r'MSRP:\s*\$?[\d,]+\.?\d*',             # MSRP: $1234
            r'List:\s*\$?[\d,]+\.?\d*',             # List: $1234
            r'Sale:\s*\$?[\d,]+\.?\d*',             # Sale: $1234
            r'[\d,]{3,}\.?\d{0,2}(?=\s|$)',         # Any 3+ digit number
            r'€[\d,]+\.?\d*',                       # €1234
            r'£[\d,]+\.?\d*',                       # £1234
        ]
        
        for pattern in price_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                price_text = match.group()
                
                # Validate this looks like a reasonable price
                if self._is_reasonable_price(price_text):
                    return price_text
        
        return ""
    
    def _is_reasonable_price(self, price_text):
        """Check if extracted text is a reasonable price"""
        # Extract just the numbers
        numbers = re.sub(r'[^\d.]', '', price_text)
        
        if not numbers:
            return False
        
        try:
            value = float(numbers)
            # Reasonable price range for IT equipment
            return 10 <= value <= 500000
        except:
            return False
    
    def _is_product_page_link(self, href, text):
        """Check if link goes to individual product page"""
        if not href or not text:
            return False
        
        # Product page URL patterns
        product_url_patterns = [
            'product', 'item', 'detail', 'spec', 'p/', '/p-', 'catalog'
        ]
        
        href_lower = href.lower()
        if any(pattern in href_lower for pattern in product_url_patterns):
            return True
        
        # Text should look like product name
        return self._is_valid_product_name(text)
    
    def _extract_from_product_page(self, soup, page_url, category1=None, category2=None, category3=None):
        """Extract product details from individual product page"""
        try:
            # Look for product name
            product_name = ""
            name_selectors = ['h1', '.product-name', '#product-name', '.title']
            
            for selector in name_selectors:
                elem = soup.select_one(selector)
                if elem:
                    product_name = elem.get_text(strip=True)
                    break
            
            if not product_name:
                # Fallback: use page title
                title = soup.find('title')
                if title:
                    product_name = title.get_text(strip=True)
            
            # Look for price with multiple selectors
            price = ""
            price_selectors = [
                '.price', '#price', '.cost', '.msrp', '.list-price',
                '.sale-price', '[class*="price"]', '[id*="price"]'
            ]
            
            for selector in price_selectors:
                elem = soup.select_one(selector)
                if elem:
                    price = self._extract_price_from_text(elem.get_text())
                    if price:
                        break
            
            # If no price in selectors, search entire page
            if not price:
                page_text = soup.get_text()
                price = self._extract_price_from_text(page_text)
            
            # Look for product image
            image_url = ""
            img_selectors = [
                '.product-image img', '#product-image img', 
                '.main-image img', '.product-photo img'
            ]
            
            for selector in img_selectors:
                img = soup.select_one(selector)
                if img and img.get('src'):
                    image_url = urljoin(page_url, img.get('src'))
                    break
            
            if product_name and len(product_name) > 5:
                product = self._create_product_object(
                    product_name, price, page_url, page_url, category1, category2, category3
                )
                if image_url:
                    product['image'] = image_url
                return product
            
        except Exception as e:
            print(f"        Error extracting from product page: {str(e)}")
        
        return None
    
    def _is_valid_product_name(self, name):
        """Enhanced product name validation"""
        if not name or len(name) < 5 or len(name) > 150:
            return False
        
        name_lower = name.lower()
        
        # Skip navigation
        if self._is_navigation_text(name):
            return False
        
        # Must have product indicators
        product_indicators = [
            'router', 'switch', 'server', 'firewall', 'module', 'card',
            'gateway', 'access point', 'storage', 'memory', 'software'
        ]
        
        has_product_indicator = any(indicator in name_lower for indicator in product_indicators)
        has_brand = any(brand in name_lower for brand in self.brands.keys())
        has_model = bool(re.search(r'\b[A-Z]{2,}\d+\b', name.upper()))
        
        return has_product_indicator or has_brand or has_model
    
    def _get_product_link_from_element(self, element, source_url):
        """Get product link from element"""
        if hasattr(element, 'find'):
            link = element.find('a', href=True)
            if link:
                return urljoin(source_url, link.get('href'))
        return source_url
    
    def _create_product_object(self, name, price, product_link, source_url, category1=None, category2=None, category3=None):
        """Create product object with your exact structure"""
        sku = self._extract_sku(name)
        brand = self._extract_brand(name)
        
        # Use provided categories or determine from name/url
        if category1 and category2 and category3:
            categories = [category1, category2, category3]
        else:
            categories = self._determine_categories(name, source_url)
        
        return {
            "Product Link": product_link,
            "product": name,
            "price": price,
            "Call For Price": "Yes" if not price else "",
            "SKU": sku,
            "Brand": brand,
            "Condition": "New",
            "Availability": "Check Availability",
            "Warranty": self._get_warranty(brand),
            "Product Description": self._create_description(name, sku, brand),
            "image": "",  # Will be filled by image enhancement
            "category 1": categories[0],
            "category 2": categories[1],
            "category 3": categories[2]
        }
    
    def _extract_sku(self, text):
        """Extract SKU from text"""
        patterns = [
            r'\b[A-Z]{2,}[-\s]*\d+[A-Z\d\-]*\b',
            r'\b\d{4}[A-Z]+\b'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text.upper())
            if matches:
                return max(matches, key=len)
        
        return ""
    
    def _extract_brand(self, text):
        """Extract brand from text"""
        text_lower = text.lower()
        
        for brand_key, brand_name in self.brands.items():
            if brand_key in text_lower:
                return brand_name
        
        return "Generic"
    
    def _determine_categories(self, name, url):
        """Determine categories based on URL and product name"""
        name_lower = name.lower()
        url_lower = url.lower()
        
        # Extract category information from URL
        category1 = "Networking"  # Default
        category2 = "Network Equipment"  # Default
        category3 = "Network Equipment"  # Default
        
        # Determine Category 1 (Main Category) from URL
        if 'routers' in url_lower:
            category1 = "Networking"
            category2 = "Routers"
        elif 'switches' in url_lower:
            category1 = "Networking"
            category2 = "Switches"
        elif 'firewalls' in url_lower or 'security' in url_lower:
            category1 = "Security"
            category2 = "Firewalls"
        elif 'wireless' in url_lower or 'wlan' in url_lower:
            category1 = "Networking"
            category2 = "Wireless"
        elif 'servers' in url_lower:
            category1 = "Servers"
            category2 = "Servers"
        elif 'storages' in url_lower or 'storage' in url_lower:
            category1 = "Storage"
            category2 = "Storage Systems"
        elif 'ip-phones' in url_lower or 'unified-communications' in url_lower:
            category1 = "Unified Communications"
            category2 = "IP Phones"
        elif 'optical-network' in url_lower or 'olt' in url_lower or 'ont' in url_lower:
            category1 = "Optical Network"
            category2 = "Optical Equipment"
        elif 'accessories' in url_lower:
            category1 = "Networking"
            category2 = "Accessories"
        
        # Determine Category 3 (Product Type) from URL and name
        if 'cisco' in url_lower or 'cisco' in name_lower:
            if 'router' in url_lower or 'router' in name_lower:
                category3 = "Cisco Routers"
            elif 'switch' in url_lower or 'switch' in name_lower:
                category3 = "Cisco Switches"
            elif 'firewall' in url_lower or 'firewall' in name_lower:
                category3 = "Cisco Firewalls"
            elif 'wireless' in url_lower or 'wireless' in name_lower:
                category3 = "Cisco Wireless"
        elif 'huawei' in url_lower or 'huawei' in name_lower:
            if 'router' in url_lower or 'router' in name_lower:
                category3 = "Huawei Routers"
            elif 'switch' in url_lower or 'switch' in name_lower:
                category3 = "Huawei Switches"
            elif 'firewall' in url_lower or 'firewall' in name_lower:
                category3 = "Huawei Firewalls"
            elif 'wireless' in url_lower or 'wireless' in name_lower:
                category3 = "Huawei Wireless"
        elif 'juniper' in url_lower or 'juniper' in name_lower:
            if 'router' in url_lower or 'router' in name_lower:
                category3 = "Juniper Routers"
            elif 'switch' in url_lower or 'switch' in name_lower:
                category3 = "Juniper Switches"
            elif 'firewall' in url_lower or 'firewall' in name_lower:
                category3 = "Juniper Firewalls"
        elif 'dell' in url_lower or 'dell' in name_lower:
            if 'server' in url_lower or 'server' in name_lower:
                category3 = "Dell Servers"
            elif 'switch' in url_lower or 'switch' in name_lower:
                category3 = "Dell Switches"
        elif 'hpe' in url_lower or 'hpe' in name_lower or 'aruba' in url_lower:
            if 'server' in url_lower or 'server' in name_lower:
                category3 = "HPE Servers"
            elif 'switch' in url_lower or 'switch' in name_lower:
                category3 = "HPE Switches"
            elif 'wireless' in url_lower or 'wireless' in name_lower:
                category3 = "HPE Aruba Wireless"
        
        return [category1, category2, category3]
    
    def _get_warranty(self, brand):
        """Get warranty"""
        return "1 Year Limited Warranty"
    
    def _create_description(self, name, sku, brand):
        """Create description"""
        parts = []
        if brand != 'Generic':
            parts.append(brand)
        if sku:
            parts.append(f"Model: {sku}")
        return ' | '.join(parts) if parts else name[:50]
    
    def _add_images_to_products(self, products, soup, source_url):
        """Add images using the working image filter"""
        if not products:
            return products
        
        # Find product images
        product_images = []
        img_tags = soup.find_all('img', src=True)
        
        for img in img_tags:
            src = img.get('src', '')
            alt = img.get('alt', '')
            
            if self._is_product_image(src, alt):
                full_url = urljoin(source_url, src)
                product_images.append(full_url)
        
        # Assign images to products
        for i, product in enumerate(products):
            if product_images:
                product['image'] = product_images[i % len(product_images)]
        
        return products
    
    def _is_product_image(self, src, alt):
        """Check if image is product image"""
        all_text = f"{src} {alt}".lower()
        
        # Exclude icons
        exclude_terms = ['icon', 'logo', 'button', 'arrow', 'menu', 'nav']
        if any(term in all_text for term in exclude_terms):
            return False
        
        # Include product images
        include_terms = ['product', 'router', 'switch', 'cisco', 'huawei', 'equipment']
        return any(term in all_text for term in include_terms) or len(src) > 20
    
    def _clean_products_comprehensive(self, products):
        """Comprehensive product cleaning and deduplication"""
        seen = set()
        clean_products = []
        
        for product in products:
            # Skip if missing essential data
            if not product.get('product') or len(product['product']) < 5:
                continue
            
            # Skip if no meaningful data
            if (not product.get('SKU') and 
                product.get('Brand') == 'Generic' and 
                not product.get('price')):
                continue
            
            # Deduplication
            identifier = f"{product['product'][:40].lower()}_{product.get('SKU', '')}"
            if identifier in seen:
                continue
            
            seen.add(identifier)
            clean_products.append(product)
        
        return clean_products
    
    def save_comprehensive_results(self, products):
        """Save comprehensive results in both JSON and Excel formats"""
        if not products:
            print("No products to save")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save JSON
        json_filename = f"comprehensive_products_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        
        # Save Excel
        excel_filename = f"comprehensive_products_{timestamp}.xlsx"
        try:
            df = pd.DataFrame(products)
            
            # Create Excel writer with multiple sheets
            with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
                # Main products sheet
                df.to_excel(writer, sheet_name='All Products', index=False)
                
                # Category summary sheets
                if 'category 1' in df.columns:
                    category1_summary = df.groupby('category 1').size().reset_index(name='Product Count')
                    category1_summary.to_excel(writer, sheet_name='Category 1 Summary', index=False)
                
                if 'category 2' in df.columns:
                    category2_summary = df.groupby(['category 1', 'category 2']).size().reset_index(name='Product Count')
                    category2_summary.to_excel(writer, sheet_name='Category 2 Summary', index=False)
                
                if 'category 3' in df.columns:
                    category3_summary = df.groupby(['category 1', 'category 2', 'category 3']).size().reset_index(name='Product Count')
                    category3_summary.to_excel(writer, sheet_name='Category 3 Summary', index=False)
                
                # Brand summary
                if 'Brand' in df.columns:
                    brand_summary = df.groupby('Brand').size().reset_index(name='Product Count')
                    brand_summary.to_excel(writer, sheet_name='Brand Summary', index=False)
            
            print(f"\nExcel file saved: {excel_filename}")
            
        except Exception as e:
            print(f"Error saving Excel file: {str(e)}")
            print("JSON file saved successfully")
        
        # Analysis
        with_prices = sum(1 for p in products if p.get('price'))
        with_skus = sum(1 for p in products if p.get('SKU'))
        with_images = sum(1 for p in products if p.get('image'))
        
        print(f"\nComprehensive results saved:")
        print(f"JSON: {json_filename}")
        print(f"Excel: {excel_filename}")
        print(f"Total products: {len(products)}")
        print(f"Products with prices: {with_prices} ({with_prices/len(products)*100:.1f}%)")
        print(f"Products with SKUs: {with_skus} ({with_skus/len(products)*100:.1f}%)")
        print(f"Products with images: {with_images} ({with_images/len(products)*100:.1f}%)")
        
        # Category analysis
        if products:
            category1_counts = {}
            category2_counts = {}
            category3_counts = {}
            
            for product in products:
                cat1 = product.get('category 1', 'Unknown')
                cat2 = product.get('category 2', 'Unknown')
                cat3 = product.get('category 3', 'Unknown')
                
                category1_counts[cat1] = category1_counts.get(cat1, 0) + 1
                category2_counts[f"{cat1} > {cat2}"] = category2_counts.get(f"{cat1} > {cat2}", 0) + 1
                category3_counts[f"{cat1} > {cat2} > {cat3}"] = category3_counts.get(f"{cat1} > {cat2} > {cat3}", 0) + 1
            
            print(f"\nCategory Analysis:")
            print(f"Category 1 (Main Categories): {len(category1_counts)}")
            for cat, count in sorted(category1_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {cat}: {count} products")
            
            print(f"\nCategory 2 (Subcategories): {len(category2_counts)}")
            for cat, count in sorted(category2_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {cat}: {count} products")
            
            print(f"\nCategory 3 (Product Types): {len(category3_counts)}")
            for cat, count in sorted(category3_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {cat}: {count} products")
        
        # Show sample products
        print(f"\nSample products found:")
        for i, product in enumerate(products[:5]):
            print(f"  {i+1}. {product['product']}")
            print(f"      Categories: {product.get('category 1', 'N/A')} > {product.get('category 2', 'N/A')} > {product.get('category 3', 'N/A')}")
            print(f"      SKU: {product.get('SKU', 'Not found')}")
            print(f"      Brand: {product.get('Brand', 'Not found')}")
            print(f"      Price: {product.get('price', 'Not found')}")
            print()

def run_comprehensive_scraper():
    """Run the comprehensive category scraper"""
    scraper = ComprehensiveCategoryScraper()
    
    try:
        print("="*80)
        print("COMPREHENSIVE ROUTER-SWITCH.COM SCRAPER")
        print("Enhanced with Human-Like Browsing Patterns")
        print("="*80)
        print("This scraper will:")
        print("1. Discover ALL main categories from the website")
        print("2. Find subcategories for each main category")
        print("3. Identify product types within each subcategory")
        print("4. Extract individual products with proper categorization")
        print("5. Export results to both JSON and Excel formats")
        print("6. Use human-like delays and browsing patterns to avoid detection")
        print("="*80)
        
        # Run comprehensive scraping
        products = scraper.scrape_all_categories_comprehensive(max_products_per_category=50)
        
        if products:
            scraper.save_comprehensive_results(products)
            
            # Final statistics
            with_prices = sum(1 for p in products if p.get('price'))
            with_skus = sum(1 for p in products if p.get('SKU'))
            with_images = sum(1 for p in products if p.get('image'))
            
            print(f"\n{'='*80}")
            print(f"COMPREHENSIVE SCRAPING COMPLETE!")
            print(f"{'='*80}")
            print(f"Total products: {len(products)}")
            print(f"Price success rate: {with_prices}/{len(products)} ({with_prices/len(products)*100:.1f}%)")
            print(f"SKU success rate: {with_skus}/{len(products)} ({with_skus/len(products)*100:.1f}%)")
            print(f"Image success rate: {with_images}/{len(products)} ({with_images/len(products)*100:.1f}%)")
            
            # Category breakdown
            categories_found = set()
            for product in products:
                cat1 = product.get('category 1', 'Unknown')
                cat2 = product.get('category 2', 'Unknown')
                cat3 = product.get('category 3', 'Unknown')
                categories_found.add(f"{cat1} > {cat2} > {cat3}")
            
            print(f"Unique category combinations found: {len(categories_found)}")
            
            if with_prices > 0:
                print(f"\nSUCCESS: Found prices for {with_prices} products!")
            else:
                print(f"\nNOTE: Limited prices found - this is common for B2B sites")
                print("The website likely uses quote-based pricing or requires login")
                
        else:
            print("No products found")
        
    except Exception as e:
        print(f"Comprehensive scraper failed: {str(e)}")
        import traceback
        traceback.print_exc()

def run_price_focused_scraper():
    """Run the price-focused scraper (legacy method)"""
    scraper = ComprehensiveCategoryScraper()
    
    try:
        print("="*80)
        print("PRICE-FOCUSED ROUTER-SWITCH.COM SCRAPER")
        print("Enhanced with Human-Like Browsing Patterns")
        print("="*80)
        print("This scraper will:")
        print("1. Focus on extracting prices from product pages")
        print("2. Use human-like delays and browsing patterns")
        print("3. Rotate user agents to look like different users")
        print("4. Simulate realistic browsing behavior")
        print("="*80)
        
        # Run enhanced scraping
        products = scraper.scrape_with_price_focus(max_products=1000)
        
        if products:
            scraper.save_comprehensive_results(products)
            
            # Final statistics
            with_prices = sum(1 for p in products if p.get('price'))
            with_skus = sum(1 for p in products if p.get('SKU'))
            with_images = sum(1 for p in products if p.get('image'))
            
            print(f"\nPRICE-FOCUSED SCRAPING COMPLETE!")
            print(f"Total products: {len(products)}")
            print(f"Price success rate: {with_prices}/{len(products)} ({with_prices/len(products)*100:.1f}%)")
            print(f"SKU success rate: {with_skus}/{len(products)} ({with_skus/len(products)*100:.1f}%)")
            print(f"Image success rate: {with_images}/{len(products)} ({with_images/len(products)*100:.1f}%)")
            
            if with_prices > 0:
                print(f"\nSUCCESS: Found prices for {with_prices} products!")
                print("Price extraction methods that worked:")
                print("- Individual product pages")
                print("- Enhanced table cell searching")
                print("- Text pattern matching")
            else:
                print(f"\nPRICE CHALLENGE: Still no prices found")
                print("This confirms the website likely uses:")
                print("1. JavaScript-only price loading")
                print("2. Login-required pricing")
                print("3. Quote-based pricing model")
                print("4. API-based price delivery")
                
        else:
            print("No products found")
        
    except Exception as e:
        print(f"Price-focused scraper failed: {str(e)}")
        import traceback
        traceback.print_exc()

def run_category_hierarchy_scraper():
    """Run only the category hierarchy scraper (Category 1 -> 2 -> 3)"""
    scraper = ComprehensiveCategoryScraper()

    try:
        print("="*80)
        print("CATEGORY HIERARCHY SCRAPER (router-switch.com)")
        print("Enhanced with Human-Like Browsing Patterns")
        print("="*80)
        print("Roots: Routers, Switches, Firewalls, Wireless, Servers, Storages")
        print("Collecting Category 2 and Category 3 under each root...")
        print("Using human-like delays and browsing patterns to avoid detection")
        print("="*80)

        rows = scraper.scrape_category_hierarchy()
        if rows:
            scraper.save_category_hierarchy_results(rows)
            print(f"Total hierarchy rows: {len(rows)}")
            # Show a few examples
            for r in rows[:10]:
                print(f" - {r.get('category 1','') } > {r.get('category 2','')} > {r.get('category 3','')} => {r.get('url','')}")
        else:
            print("No hierarchy rows collected")

    except Exception as e:
        print(f"Hierarchy scraper failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Router-Switch.com scraper with human-like browsing patterns")
    parser.add_argument(
        "--mode",
        choices=["comprehensive", "price", "hierarchy", "combined", "fast"],
        default="comprehensive",
        help="Which scraper to run"
    )
    args = parser.parse_args()
    
    print("="*80)
    print("ROUTER-SWITCH.COM SCRAPER")
    print("Enhanced with Human-Like Browsing Patterns")
    print("="*80)
    print("Features:")
    print("- Realistic user agent rotation")
    print("- Human-like delays and browsing patterns")
    print("- Mouse movement simulation")
    print("- Session break simulation")
    print("- Distraction pause simulation")
    print("="*80)

    if args.mode == "comprehensive":
        run_comprehensive_scraper()
    elif args.mode == "price":
        run_price_focused_scraper()
    elif args.mode == "hierarchy":
        run_category_hierarchy_scraper()
    elif args.mode == "combined":
        # Use the class-bound combined runner
        ComprehensiveCategoryScraper().run_combined_scraper()
    elif args.mode == "fast":
        # Fast mode with reduced delays and limits
        ComprehensiveCategoryScraper().run_combined_scraper(fast_mode=True)