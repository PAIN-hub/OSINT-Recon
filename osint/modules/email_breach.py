import requests

def email_breach(email):
    """Check if an email address has been compromised in data breaches using XposedOrNot public API."""
    data = {"type": "email_breach", "email": email}
    headers = {"User-Agent": "osint-toolkit/1.0 (+https://github.com/PAIN-hub/osint-toolkit)"}
    try:
        url = f"https://api.xposedornot.com/v1/check-email/{email}"
        res = requests.get(url, headers=headers, timeout=10)
        
        if res.status_code == 200:
            res_data = res.json()
            if "Error" in res_data and res_data["Error"] == "Not found":
                data["breaches"] = []
                data["status"] = "No breaches found"
            else:
                raw_breaches = res_data.get("breaches", [])
                # XposedOrNot returns breaches as a list containing a list of strings
                if raw_breaches and isinstance(raw_breaches[0], list):
                    data["breaches"] = raw_breaches[0]
                else:
                    data["breaches"] = raw_breaches
        else:
            data["error"] = f"Status code {res.status_code}"
    except requests.RequestException as e:
        data["error"] = str(e)
    return data
