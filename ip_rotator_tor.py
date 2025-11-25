"""
IP Rotator using Tor Network
Requires: pip install requests[socks] stem
Also needs: Tor Browser or Tor service running
"""

import time
import requests
from stem import Signal
from stem.control import Controller

class TorIPRotator:
    def __init__(self, tor_password='', tor_port=9051, socks_port=9050):
        """
        tor_password: Password set in torrc (leave empty if not set)
        tor_port: Tor control port (default 9051)
        socks_port: Tor SOCKS proxy port (default 9050)
        """
        self.tor_password = tor_password
        self.tor_port = tor_port
        self.socks_port = socks_port
        self.session = requests.Session()
        self.session.proxies = {
            'http': f'socks5://127.0.0.1:{socks_port}',
            'https': f'socks5://127.0.0.1:{socks_port}'
        }
    
    def get_current_ip(self):
        """Check current public IP"""
        try:
            response = self.session.get('https://api.ipify.org?format=json', timeout=10)
            return response.json()['ip']
        except Exception as e:
            return f"Error: {e}"
    
    def renew_connection(self):
        """Request new Tor circuit (new IP)"""
        try:
            with Controller.from_port(port=self.tor_port) as controller:
                controller.authenticate(password=self.tor_password)
                controller.signal(Signal.NEWNYM)
                print("✓ New Tor circuit requested")
                time.sleep(5)  # Wait for new circuit to establish
        except Exception as e:
            print(f"✗ Error renewing connection: {e}")
            print("Make sure Tor is running and control port is accessible")
    
    def start_rotation(self, interval=10):
        """Rotate IP every interval seconds"""
        print("=" * 50)
        print("TOR IP ROTATOR STARTED")
        print("=" * 50)
        print(f"Rotation interval: {interval} seconds")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                current_ip = self.get_current_ip()
                timestamp = time.strftime("%H:%M:%S")
                print(f"[{timestamp}] Current IP: {current_ip}")
                
                time.sleep(interval)
                
                print(f"[{timestamp}] Requesting new IP...")
                self.renew_connection()
                
        except KeyboardInterrupt:
            print("\n\nRotation stopped by user")

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("SETUP INSTRUCTIONS:")
    print("=" * 50)
    print("1. Download Tor Browser: https://www.torproject.org/download/")
    print("2. Open Tor Browser (this starts Tor service)")
    print("3. Run: pip install requests[socks] stem")
    print("4. Run this script")
    print("=" * 50 + "\n")
    
    input("Press ENTER when Tor Browser is running...")
    
    rotator = TorIPRotator()
    
    # Test initial connection
    print("\nTesting Tor connection...")
    initial_ip = rotator.get_current_ip()
    print(f"Initial IP: {initial_ip}\n")
    
    if "Error" in str(initial_ip):
        print("✗ Cannot connect to Tor. Make sure Tor Browser is running.")
    else:
        rotator.start_rotation(interval=10)
