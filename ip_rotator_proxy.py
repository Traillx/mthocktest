"""
IP Rotator using Free Proxy Servers
Warning: Free proxies are unreliable and may not work
Requires: pip install requests beautifulsoup4
"""

import time
import requests
from bs4 import BeautifulSoup
import random

class ProxyIPRotator:
    def __init__(self):
        self.proxies = []
        self.current_proxy = None
        self.working_proxies = []
    
    def fetch_free_proxies(self):
        """Scrape free proxies from multiple sources"""
        print("Fetching free proxies...")
        proxies = []
        
        try:
            # Source 1: Free-proxy-list.net
            url = 'https://free-proxy-list.net/'
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for row in soup.find('table').find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 7:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    https = cols[6].text.strip()
                    
                    proxy = f"{ip}:{port}"
                    proxies.append(proxy)
                    
                    if len(proxies) >= 50:  # Limit to 50 proxies
                        break
        except Exception as e:
            print(f"Error fetching proxies: {e}")
        
        print(f"✓ Found {len(proxies)} proxies")
        self.proxies = proxies
        return proxies
    
    def test_proxy(self, proxy):
        """Test if proxy works"""
        try:
            proxies = {
                'http': f'http://{proxy}',
                'https': f'http://{proxy}'
            }
            response = requests.get('https://api.ipify.org?format=json', 
                                   proxies=proxies, 
                                   timeout=5)
            if response.status_code == 200:
                ip = response.json()['ip']
                return True, ip
        except:
            pass
        return False, None
    
    def get_working_proxies(self, count=10):
        """Find working proxies"""
        print(f"\nTesting proxies (finding {count} working ones)...")
        working = []
        
        for proxy in self.proxies:
            if len(working) >= count:
                break
                
            is_working, ip = self.test_proxy(proxy)
            if is_working:
                working.append(proxy)
                print(f"✓ Working: {proxy} -> IP: {ip}")
            else:
                print(f"✗ Failed: {proxy}")
        
        self.working_proxies = working
        print(f"\n✓ Found {len(working)} working proxies")
        return working
    
    def get_current_ip(self, proxy=None):
        """Get current public IP"""
        try:
            if proxy:
                proxies = {
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}'
                }
                response = requests.get('https://api.ipify.org?format=json', 
                                       proxies=proxies, 
                                       timeout=10)
            else:
                response = requests.get('https://api.ipify.org?format=json', timeout=10)
            
            return response.json()['ip']
        except Exception as e:
            return f"Error: {e}"
    
    def start_rotation(self, interval=10):
        """Rotate through proxies every interval seconds"""
        if not self.working_proxies:
            print("No working proxies available!")
            return
        
        print("\n" + "=" * 50)
        print("PROXY IP ROTATOR STARTED")
        print("=" * 50)
        print(f"Rotation interval: {interval} seconds")
        print(f"Available proxies: {len(self.working_proxies)}")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                proxy = random.choice(self.working_proxies)
                current_ip = self.get_current_ip(proxy)
                timestamp = time.strftime("%H:%M:%S")
                print(f"[{timestamp}] Proxy: {proxy} -> IP: {current_ip}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n\nRotation stopped by user")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("FREE PROXY IP ROTATOR")
    print("=" * 50)
    print("Warning: Free proxies are often slow/unreliable")
    print("For better results, use Tor (ip_rotator_tor.py)")
    print("=" * 50 + "\n")
    
    rotator = ProxyIPRotator()
    
    # Show real IP first
    print("Your real IP:", rotator.get_current_ip())
    
    # Fetch and test proxies
    rotator.fetch_free_proxies()
    rotator.get_working_proxies(count=10)
    
    if rotator.working_proxies:
        input("\nPress ENTER to start rotation...")
        rotator.start_rotation(interval=10)
    else:
        print("\n✗ No working proxies found. Try again later.")
