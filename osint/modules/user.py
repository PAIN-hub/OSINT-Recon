import requests
from concurrent.futures import ThreadPoolExecutor

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Telegram": "https://t.me/{}",
}

HEADERS = {"User-Agent": "osint-toolkit/1.0 (+https://github.com/PAIN-hub/osint-toolkit)"}

def _probe(url):
    try:
        res = requests.head(url, headers=HEADERS, allow_redirects=True, timeout=8)
        return {"url": url, "status": res.status_code, "exists": res.status_code == 200}
    except requests.RequestException as e:
        return {"url": url, "error": str(e)}

def check_username(username):
    """Check if a username exists on known social platforms (public probe only)."""
    results = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(_probe, link.format(username)): name for name, link in PLATFORMS.items()}
        for fut in futures:
            platform = futures[fut]
            results[platform] = fut.result()
    return {"type": "username", "username": username, "results": results}