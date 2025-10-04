import socket
import whois

def domain_report(domain):
    data = {"type": "domain", "domain": domain}

    # WHOIS lookup
    try:
        w = whois.whois(domain)
        data["whois"] = {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "emails": w.emails,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
        }
    except Exception as e:
        data["whois_error"] = str(e)

    # DNS lookup
    try:
        host_data = socket.gethostbyname_ex(domain)
        data["dns"] = {"hostname": host_data[0], "aliases": host_data[1], "ips": host_data[2]}
    except Exception as e:
        data["dns_error"] = str(e)

    return data