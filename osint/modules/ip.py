import requests

def ip_lookup(ip):
    data = {"type": "ip", "ip": ip}
    try:
        res = requests.get(f"https://ipapi.co/{ip}/json/", timeout=10)
        if res.status_code == 200:
            data["geolocation"] = res.json()
        else:
            data["error"] = f"Status code {res.status_code}"
    except requests.RequestException as e:
        data["error"] = str(e)
    return data