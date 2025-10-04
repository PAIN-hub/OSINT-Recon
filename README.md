# OSINT Recon Tool

**OSINT Recon Tool is a Python-based intelligence gathering framework that collects data from various online sources to help identify digital footprints, linked accounts, emails, usernames, IPs, and more — all legally and ethically.**

## legal concept.

> This tool is built for researchers, ethical hackers, and cybersecurity students who want to streamline their reconnaissance workflow using open-source data.

## features

1. Username Lookup — Finds linked accounts across 100+ platforms.

2. IP Lookup — Pulls IP geolocation, ISP, ASN, and proxy/VPN detection.

3. Email Enumeration — Checks email breaches using HaveIBeenPwned API.

4. Social Media Recon — Basic metadata scraping from public profiles.

5. Output Export — Save all findings in structured JSON or TXT.

6. Modular System — Easy to expand with new recon modules.

### Use Cases

1. Digital footprint analysis

2. Threat intelligence enrichment

3. Penetration testing prep

4. Cybersecurity research

5. Personal privacy audit

# Installation

1. Clone the repo and install dependencies:
```
git clone https://github.com/PAIN-hub/OSINT-Recon.git
cd OSINT-Recon
```
2. Install requirements
```
pip install -r requirements.txt
```
3. python version requirement:

Make sure you’re on `Python 3.9+.`

# Usage

1. Run the tool from terminal:

2. python3 recon.py

3. Then follow the on-screen prompts:

[1] Username Lookup
[2] IP Address Lookup
[3] Email Breach Check
[4] Domain WHOIS
[5] Exit

## Example

$ python3 recon.py

Enter target username: johndoe

[+] Checking across platforms...
- Twitter: Found ✅
- Instagram: Not found ❌
- GitHub: Found ✅
- Reddit: Found ✅

[+] Report saved: /reports/johndoe.json

### Project Structure

```
OSINT-Recon/
├── recon.py               # main tool entry point
├── modules/
│   ├── username_lookup.py
│   ├── ip_lookup.py
│   ├── email_breach.py
│   ├── domain_whois.py
├── reports/               # output folder
├── requirements.txt
└── README.md`
```

## Dependencies

`requests` `colorama` `json` `ipwhois` `python-whois` `Install all with:``
 
 ** All in one Installation **
 ```
pip install -r requirements.txt
```

⚠️ Legal Disclaimer

> This tool is strictly for educational and ethical testing.
Do not use it on targets without explicit consent.
The author and contributors are not responsible for any misuse.

# Contributing

Want to make it better? Fork the repo and send a pull request.
Add a new module under /modules/ — e.g. LinkedIn scraping, phone lookup, or subdomain finder.

** Author **

ƤȺIƝ
** 💻 CyberSec Student & Web Developer **
** 🐙 GitHub: PAIN-hub **

### ⭐ Support

If you like the project, give it a ⭐ on GitHub — it helps more people discover it!

### Contact Me @
<a href='https://x.com/0x_beely'>X (Twitter) </a>
<a href='https://m.facebook.com/ƤȺIƝ Ise'> Facebook </a>
<a href='https://Instagram.com/0x_beely'> Instagram </a>