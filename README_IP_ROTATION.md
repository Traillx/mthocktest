# IP Rotation Tools

## 🔴 LEGAL WARNING
Using these tools to spam/attack forms is **ILLEGAL** and can result in:
- Criminal charges (Computer Fraud and Abuse Act)
- School expulsion
- Civil lawsuits
- Account bans

**Use only for legitimate testing with permission.**

---

## 📁 Files

### 1. `ip_rotator_tor.py` ⭐ RECOMMENDED
**Uses Tor network to change IP every 10 seconds**

**Setup:**
```bash
# 1. Download Tor Browser
https://www.torproject.org/download/

# 2. Install dependencies
pip install requests[socks] stem

# 3. Run Tor Browser (keep it open)

# 4. Run script
python ip_rotator_tor.py
```

**Pros:**
- ✅ Free
- ✅ Reliable IP changes
- ✅ Anonymous
- ✅ Works worldwide

**Cons:**
- ❌ Slower speed
- ❌ Tor exit nodes can be detected

---

### 2. `ip_rotator_proxy.py`
**Uses free proxy servers (unreliable)**

**Setup:**
```bash
# Install dependencies
pip install requests beautifulsoup4

# Run
python ip_rotator_proxy.py
```

**Pros:**
- ✅ No additional software needed

**Cons:**
- ❌ Most free proxies don't work
- ❌ Very slow
- ❌ Unreliable
- ❌ May log your activity

---

### 3. `form_submitter_with_rotation.py` ⭐ COMPLETE SOLUTION
**Automated form submission with Tor IP rotation**

**Features:**
- Changes IP every N submissions
- Random delays between submissions
- Randomized personal data
- Progress tracking

**Setup:**
```bash
# 1. Run Tor Browser
# 2. Install: pip install requests[socks] stem
# 3. Run script
python form_submitter_with_rotation.py
```

**Configuration:**
- `submissions_per_ip=5` → Change IP after every 5 submissions
- `delay_min=2, delay_max=5` → Random delay 2-5 seconds
- Makes pattern less obvious

---

## 🛡️ Security Recommendations

### If you MUST proceed:

1. **Use Tor** (ip_rotator_tor.py)
   - Hides your real IP

2. **Small batches**
   - 5-10 submissions max per session
   - Spread over days, not minutes

3. **Variable timing**
   - Random delays (2-10 seconds)
   - Don't submit at regular intervals

4. **Different IPs**
   - Change IP every 3-5 submissions
   - Don't send 100 from same IP

5. **No Google login**
   - Use incognito/private mode
   - Don't be logged into Google account

6. **Test first**
   - Send 2-3 test submissions
   - Check if you get caught

### What Google WILL see:
- All submissions from Tor network (suspicious)
- Similar response patterns (all "1" ratings)
- Timestamps (if too close together)
- Fake/random personal data

### What they WON'T see:
- Your real IP (if using Tor)
- Your real identity (if using fake data)

---

## 🚨 Detection Risk: HIGH

Even with IP rotation:
- **Tor IPs are publicly known** → Easy to detect/block
- **Pattern matching** → All "1" ratings = obvious bot
- **Timestamp analysis** → 100 submissions in short time = suspicious
- **Google's anti-spam** → Forms have rate limiting

---

## ✅ Safer Alternatives

Instead of spamming:
1. **Talk to administration** about form issues
2. **Submit ONE honest response** with detailed feedback
3. **Organize student petition** (legitimate way)
4. **Use official channels** for complaints

---

## 🔧 Quick Start Guide

### For IP rotation only:
```bash
python ip_rotator_tor.py
```

### For automated form submission:
```bash
python form_submitter_with_rotation.py
```

Follow the on-screen prompts.

---

## ⚠️ Final Warning

This is for **educational purposes** and **authorized testing only**.

Unauthorized use = **CRIME**

Your friend can face serious consequences. Proceed at your own risk.
