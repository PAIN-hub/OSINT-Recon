#!/usr/bin/env python3
import argparse
import json
from osint.modules import user, domain, ip, filemeta

def main():
    parser = argparse.ArgumentParser(
        prog="osint",
        description="🕵️ OSINT Toolkit — Gather public intelligence safely."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # username lookup
    p_user = sub.add_parser("user", help="Check username across platforms")
    p_user.add_argument("username")
    p_user.add_argument("--json-out", help="Export results to JSON file")

    # domain lookup
    p_domain = sub.add_parser("domain", help="Get WHOIS and DNS data")
    p_domain.add_argument("domain")
    p_domain.add_argument("--json-out")

    # ip lookup
    p_ip = sub.add_parser("ip", help="Check IP info + geolocation")
    p_ip.add_argument("ip")
    p_ip.add_argument("--json-out")

    # file metadata
    p_file = sub.add_parser("file", help="Extract file metadata and hashes")
    p_file.add_argument("path")
    p_file.add_argument("--json-out")

    args = parser.parse_args()

    if args.cmd == "user":
        result = user.check_username(args.username)
    elif args.cmd == "domain":
        result = domain.domain_report(args.domain)
    elif args.cmd == "ip":
        result = ip.ip_lookup(args.ip)
    elif args.cmd == "file":
        result = filemeta.extract_metadata(args.path)
    else:
        parser.error("Unknown command")

    print(json.dumps(result, indent=2))
    if getattr(args, "json_out", None):
        with open(args.json_out, "w") as f:
            json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()