#!/usr/bin/env python3
import os
import json
import time
from colorama import Fore, Style, init

# Correct package imports
from osint.modules.user import check_username as username_lookup
from osint.modules.ip import ip_lookup
from osint.modules.email_breach import email_breach
from osint.modules.domain import domain_report as domain_whois

init(autoreset=True)

# Doubled backslashes to avoid SyntaxWarning with invalid escape sequences
BANNER = f"""{Fore.RED}
    ____  ___    _____   __   __  ____  ______
   / __ \\/   |  /  _/ | / /  / / / / / / / __ )
  / /_/ / /| |  / //  |/ /  / /_/ / / / / __  |
 / ____/ ___ |_/ // /|  /  / __  / /_/ / /_/ /
/_/   /_/  |_/___/_/ |_/  /_/ /_/\\____/_____/
{Style.RESET_ALL}
by ƤȺIƝ  |  GitHub: PAIN-hub
"""

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)


def save_report(data, filename):
    path = os.path.join(REPORTS_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n{Fore.GREEN}[+] Report saved: {path}{Style.RESET_ALL}")


def menu():
    print(BANNER)
    print(f"""
{Fore.CYAN}[1]{Style.RESET_ALL} Username Lookup
{Fore.CYAN}[2]{Style.RESET_ALL} IP Address Lookup
{Fore.CYAN}[3]{Style.RESET_ALL} Email Breach Check
{Fore.CYAN}[4]{Style.RESET_ALL} Domain WHOIS Lookup
{Fore.CYAN}[5]{Style.RESET_ALL} Exit
""")


def main():
    while True:
        menu()
        choice = input(f"{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        print()

        if choice == "1":
            username = input("Enter username: ").strip()
            data = username_lookup(username)
            save_report(data, f"{username}.json")

        elif choice == "2":
            ip_val = input("Enter IP address: ").strip()
            data = ip_lookup(ip_val)
            save_report(data, f"{ip_val}.json")

        elif choice == "3":
            email_val = input("Enter email: ").strip()
            data = email_breach(email_val)
            save_report(data, f"{email_val.replace('@', '_')}.json")

        elif choice == "4":
            domain_val = input("Enter domain: ").strip()
            data = domain_whois(domain_val)
            save_report(data, f"{domain_val}.json")

        elif choice == "5":
            print(f"{Fore.CYAN}\nGoodbye, hacker 🫡{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Style.RESET_ALL}")
        print()
        time.sleep(1)


if __name__ == "__main__":
    main()
