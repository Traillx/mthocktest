"""
Google Form Submitter with Tor IP Rotation
Combines form submission with automatic IP changing
Requires: pip install requests[socks] stem
"""

import time
import requests
from stem import Signal
from stem.control import Controller
import random

class FormSubmitterWithRotation:
    def __init__(self, form_url, tor_port=9051, socks_port=9050):
        self.form_url = form_url
        self.tor_port = tor_port
        self.socks_port = socks_port
        self.session = requests.Session()
        self.session.proxies = {
            'http': f'socks5://127.0.0.1:{socks_port}',
            'https': f'socks5://127.0.0.1:{socks_port}'
        }
        
        # Data generators
        self.first_names = ["Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", 
                           "Ayaan", "Krishna", "Ishaan", "Diya", "Saanvi", "Ananya", "Aadhya"]
        self.last_names = ["Patel", "Sharma", "Singh", "Kumar", "Gupta", "Verma", "Reddy", 
                          "Nair", "Joshi", "Mehta", "Shah", "Agarwal"]
        self.branches = ["Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
                        "Computer Engineering", "ETC", "CSE (Data Science)", "IIOT"]
        self.semesters = ["III", "V", "VII"]
    
    def renew_tor_ip(self):
        """Get new Tor IP"""
        try:
            with Controller.from_port(port=self.tor_port) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                time.sleep(5)  # Wait for circuit
                return True
        except Exception as e:
            print(f"✗ Error changing IP: {e}")
            return False
    
    def get_current_ip(self):
        """Check current IP"""
        try:
            response = self.session.get('https://api.ipify.org?format=json', timeout=10)
            return response.json()['ip']
        except:
            return "Unknown"
    
    def generate_random_data(self):
        """Generate random student data"""
        first = random.choice(self.first_names)
        last = random.choice(self.last_names)
        name = f"{first} {last}"
        
        phone = f"{random.choice([7,8,9])}{random.randint(100000000, 999999999)}"
        email = f"{first.lower()}.{last.lower()}{random.randint(1, 999)}@gmail.com"
        branch = random.choice(self.branches)
        sem = random.choice(self.semesters)
        
        return {
            'name': name,
            'phone': phone,
            'email': email,
            'branch': branch,
            'sem': sem
        }
    
    def submit_form(self, data):
        """Submit form with given data"""
        form_data = {
            # System fields
            'fvv': '1',
            'pageHistory': '0',
            'fbzx': '-1413619500707926375',
            
            # Personal info
            'entry.1279973486': data['name'],
            'entry.1606620797': '2025-26',
            'entry.1606620797_sentinel': '',
            'entry.855330168': data['branch'],
            'entry.855330168_sentinel': '',
            'entry.1170358699': data['sem'],
            'entry.1170358699_sentinel': '',
            'entry.1059648073': data['phone'],
            'entry.754027993': data['email'],
            
            # All ratings set to 1
            'entry.706612593': '1',
            'entry.706612593_sentinel': '',
            'entry.1949758445': '1',
            'entry.1949758445_sentinel': '',
            'entry.2068019790': '1',
            'entry.2068019790_sentinel': '',
            'entry.1730869355': '1',
            'entry.1730869355_sentinel': '',
            'entry.140983378': '1',
            'entry.140983378_sentinel': '',
            'entry.405415457': '1',
            'entry.405415457_sentinel': '',
            'entry.1682092224': '1',
            'entry.1682092224_sentinel': '',
            'entry.225980514': '1',
            'entry.225980514_sentinel': '',
            'entry.254228138': '1',
            'entry.254228138_sentinel': '',
            'entry.1358656494': '1',
            'entry.1358656494_sentinel': '',
            'entry.1182768751': '1',
            'entry.1182768751_sentinel': '',
            'entry.878164991': '1',
            'entry.878164991_sentinel': '',
        }
        
        try:
            response = self.session.post(self.form_url, data=form_data, timeout=15)
            return response.status_code == 200
        except Exception as e:
            print(f"  ✗ Submission error: {e}")
            return False
    
    def run(self, total_submissions=100, submissions_per_ip=5, delay_min=2, delay_max=5):
        """
        Run form submissions with IP rotation
        
        total_submissions: Total forms to submit
        submissions_per_ip: How many forms to submit before changing IP
        delay_min/max: Random delay between submissions (seconds)
        """
        print("\n" + "=" * 60)
        print("FORM SUBMITTER WITH TOR IP ROTATION")
        print("=" * 60)
        print(f"Total submissions: {total_submissions}")
        print(f"Submissions per IP: {submissions_per_ip}")
        print(f"Delay between submissions: {delay_min}-{delay_max}s")
        print("=" * 60 + "\n")
        
        current_ip = self.get_current_ip()
        print(f"Starting IP: {current_ip}\n")
        
        successful = 0
        failed = 0
        
        try:
            for i in range(total_submissions):
                # Change IP every N submissions
                if i > 0 and i % submissions_per_ip == 0:
                    print(f"\n{'='*60}")
                    print(f"Changing IP (after {submissions_per_ip} submissions)...")
                    self.renew_tor_ip()
                    new_ip = self.get_current_ip()
                    print(f"New IP: {new_ip}")
                    print(f"{'='*60}\n")
                
                # Generate random data
                data = self.generate_random_data()
                
                # Submit form
                timestamp = time.strftime("%H:%M:%S")
                print(f"[{timestamp}] #{i+1}/{total_submissions} - {data['name']} ({data['branch']}) ", end='')
                
                if self.submit_form(data):
                    print("✓")
                    successful += 1
                else:
                    print("✗")
                    failed += 1
                
                # Random delay
                if i < total_submissions - 1:
                    delay = random.uniform(delay_min, delay_max)
                    time.sleep(delay)
            
            print("\n" + "=" * 60)
            print("COMPLETION SUMMARY")
            print("=" * 60)
            print(f"Successful: {successful}")
            print(f"Failed: {failed}")
            print(f"Total: {total_submissions}")
            print("=" * 60)
            
        except KeyboardInterrupt:
            print("\n\nStopped by user")
            print(f"Completed: {successful + failed}/{total_submissions}")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SETUP REQUIRED:")
    print("=" * 60)
    print("1. Download and run Tor Browser")
    print("2. Install: pip install requests[socks] stem")
    print("3. Make sure Tor is running before starting")
    print("=" * 60 + "\n")
    
    input("Press ENTER when Tor Browser is running...")
    
    FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf4pS2K9kr0tykSROOtkGpjzVnPKYlYlZd15Na9nvxa8T9fFw/formResponse"
    
    submitter = FormSubmitterWithRotation(FORM_URL)
    
    # Test connection
    print("\nTesting Tor connection...")
    test_ip = submitter.get_current_ip()
    print(f"Current IP: {test_ip}")
    
    if "Error" not in str(test_ip):
        print("\n✓ Tor connection working!\n")
        
        # Configuration
        TOTAL = int(input("Total submissions (default 100): ") or "100")
        PER_IP = int(input("Submissions per IP (default 5): ") or "5")
        
        submitter.run(
            total_submissions=TOTAL,
            submissions_per_ip=PER_IP,
            delay_min=2,
            delay_max=5
        )
    else:
        print("\n✗ Cannot connect to Tor. Make sure Tor Browser is running.")
