"""
Simple Tor Form Submitter (No Control Port Required)
Just uses Tor's SOCKS proxy - no configuration needed!
Requires: pip install requests[socks]
"""

import time
import requests
import random

# Configure session to use Tor's SOCKS proxy
session = requests.Session()
session.proxies = {
    'http': 'socks5h://127.0.0.1:9150',   # Tor Browser default
    'https': 'socks5h://127.0.0.1:9150'
}

# Random data generators (100+ combinations)
FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Ayaan", "Krishna", "Ishaan",
    "Shaurya", "Atharva", "Advik", "Pranav", "Aayansh", "Arnav", "Shlok", "Rudra", "Shivansh", "Vedant",
    "Diya", "Saanvi", "Ananya", "Aadhya", "Pari", "Riya", "Myra", "Kavya", "Anika", "Kiara",
    "Navya", "Aaradhya", "Sara", "Isha", "Pihu", "Shanaya", "Avni", "Zara", "Siya", "Anvi",
    "Aryan", "Ayush", "Harsh", "Kunal", "Manav", "Naman", "Parth", "Rishabh", "Sarthak", "Tushar"
]

LAST_NAMES = [
    "Patel", "Sharma", "Singh", "Kumar", "Gupta", "Verma", "Reddy", "Nair", "Joshi", "Mehta",
    "Shah", "Agarwal", "Mishra", "Rao", "Chopra", "Desai", "Malhotra", "Kapoor", "Pandey", "Iyer",
    "Yadav", "Khan", "Saxena", "Bhatt", "Trivedi", "Rana", "Chauhan", "Sinha", "Dubey", "Menon"
]

BRANCHES = [
    "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Computer Engineering", "Electronics & Telecommunication", "CSE (Data Science)",
    "CSE (Artificial Intelligence)", "Information Technology", "IIOT"
]

SEMESTERS = ["I", "III", "V", "VII"]

def get_current_ip():
    """Check current Tor IP"""
    try:
        response = session.get('https://api.ipify.org?format=json', timeout=15)
        return response.json()['ip']
    except Exception as e:
        return f"Error: {e}"

def generate_random_data():
    """Generate random student data"""
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    name = f"{first} {last}"
    
    phone = f"{random.choice([7,8,9])}{random.randint(100000000, 999999999)}"
    
    # Varied email formats
    email_formats = [
        f"{first.lower()}.{last.lower()}{random.randint(1, 9999)}@gmail.com",
        f"{first.lower()}{last.lower()}{random.randint(1, 9999)}@gmail.com",
        f"{first.lower()}_{last.lower()}@yahoo.com",
        f"{first.lower()}.{last.lower()}@outlook.com"
    ]
    email = random.choice(email_formats)
    
    branch = random.choice(BRANCHES)
    sem = random.choice(SEMESTERS)
    
    return {
        'name': name,
        'phone': phone,
        'email': email,
        'branch': branch,
        'sem': sem
    }

def generate_random_rating():
    """Generate rating 1-5 with high bias (3-5)"""
    rand = random.random()
    if rand < 0.3:
        return 3
    elif rand < 0.7:
        return 4
    else:
        return 5

def submit_form(data):
    """Submit form with random ratings"""
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
        
        # Random ratings (3-5 bias)
        'entry.706612593': str(generate_random_rating()),
        'entry.706612593_sentinel': '',
        'entry.1949758445': str(generate_random_rating()),
        'entry.1949758445_sentinel': '',
        'entry.2068019790': str(generate_random_rating()),
        'entry.2068019790_sentinel': '',
        'entry.1730869355': str(generate_random_rating()),
        'entry.1730869355_sentinel': '',
        'entry.140983378': str(generate_random_rating()),
        'entry.140983378_sentinel': '',
        'entry.405415457': str(generate_random_rating()),
        'entry.405415457_sentinel': '',
        'entry.1682092224': str(generate_random_rating()),
        'entry.1682092224_sentinel': '',
        'entry.225980514': str(generate_random_rating()),
        'entry.225980514_sentinel': '',
        'entry.254228138': str(generate_random_rating()),
        'entry.254228138_sentinel': '',
        'entry.1358656494': str(generate_random_rating()),
        'entry.1358656494_sentinel': '',
        'entry.1182768751': str(generate_random_rating()),
        'entry.1182768751_sentinel': '',
        'entry.878164991': str(generate_random_rating()),
        'entry.878164991_sentinel': '',
    }
    
    try:
        url = "https://docs.google.com/forms/d/e/1FAIpQLSf4pS2K9kr0tykSROOtkGpjzVnPKYlYlZd15Na9nvxa8T9fFw/formResponse"
        # Add cache busting
        timestamp = int(time.time() * 1000) + random.randint(0, 1000)
        url_with_cache = f"{url}?t={timestamp}"
        
        response = session.post(url_with_cache, data=form_data, timeout=20)
        return response.status_code == 200
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("\n" + "=" * 70)
    print("SIMPLE TOR FORM SUBMITTER (Auto IP Change via Tor)")
    print("=" * 70)
    print("\nIMPORTANT: Tor Browser must be running!")
    print("Tor changes your IP automatically with each circuit.\n")
    print("=" * 70 + "\n")
    
    # Test Tor connection
    print("Testing Tor connection...")
    current_ip = get_current_ip()
    print(f"Current Tor IP: {current_ip}\n")
    
    if "Error" in str(current_ip):
        print("✗ Cannot connect to Tor!")
        print("\nTroubleshooting:")
        print("1. Make sure Tor Browser is RUNNING")
        print("2. Tor Browser uses port 9150 by default")
        print("3. Try closing and reopening Tor Browser")
        return
    
    print("✓ Connected to Tor!\n")
    
    # Get user input
    try:
        total = int(input("How many submissions? (Recommended: 5-10): ") or "10")
    except:
        total = 10
    
    try:
        delay_min = int(input("Min delay in seconds (default 3): ") or "3")
        delay_max = int(input("Max delay in seconds (default 8): ") or "8")
    except:
        delay_min, delay_max = 3, 8
    
    print("\n" + "=" * 70)
    print(f"Starting {total} submissions with {delay_min}-{delay_max}s random delays")
    print("Tor will rotate your IP automatically through different circuits")
    print("=" * 70 + "\n")
    
    successful = 0
    failed = 0
    
    try:
        for i in range(total):
            # Generate random data
            data = generate_random_data()
            
            # Show current IP every 3 submissions
            if i % 3 == 0 and i > 0:
                new_ip = get_current_ip()
                print(f"\n🔄 Current Tor IP: {new_ip}\n")
            
            # Submit
            timestamp = time.strftime("%H:%M:%S")
            print(f"[{timestamp}] #{i+1}/{total} - {data['name']} ({data['branch']}) ", end='', flush=True)
            
            if submit_form(data):
                print("✓")
                successful += 1
            else:
                print("✗")
                failed += 1
            
            # Random delay
            if i < total - 1:
                delay = random.uniform(delay_min, delay_max)
                print(f"  ⏳ Waiting {delay:.1f}s...")
                time.sleep(delay)
        
        # Summary
        print("\n" + "=" * 70)
        print("COMPLETION SUMMARY")
        print("=" * 70)
        print(f"✓ Successful: {successful}")
        print(f"✗ Failed: {failed}")
        print(f"Total: {total}")
        print(f"Success Rate: {(successful/total*100):.1f}%")
        print("=" * 70)
        
        # Final IP check
        final_ip = get_current_ip()
        print(f"\nFinal Tor IP: {final_ip}")
        print("\nNote: Tor rotates IPs automatically as you browse.")
        print("Each submission may use a different IP from Tor's circuit pool.\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Stopped by user")
        print(f"Completed: {successful + failed}/{total} submissions")

if __name__ == "__main__":
    print("\n⚠️  REMINDER: Use responsibly and keep submissions LOW (5-10 max)")
    print("Tor provides IP anonymity but doesn't make spam undetectable!\n")
    
    input("Press ENTER to continue...")
    main()
