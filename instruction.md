# Running OSINT Recon Toolkit

This document explains how to set up, run, and test the OSINT Recon project.

## Prerequisite Setup

The toolkit requires Python 3.8+ and its external dependencies. Install the dependencies in your Python environment:

```bash
pip install -r requirements.txt
```

Alternatively, to install the package locally so the custom console command is available:

```bash
pip install -e .
```
*(Note: If your system uses PEP 668 externally-managed environment, you can run inside a virtual environment or run using `--break-system-packages` if safe).*

---

## 1. Running the Interactive Interface

Run the interactive console menu from the root of the repository:

```bash
python3 recon.py
```

This starts a console interface with the following options:
1. **Username Lookup** — Searches username availability on GitHub, Twitter, Instagram, Reddit, and Telegram.
2. **IP Address Lookup** — Performs geolocation lookup on an IP address.
3. **Email Breach Check** — Checks for data breaches of an email via the XposedOrNot public API.
4. **Domain WHOIS Lookup** — Obtains WHOIS information and resolved DNS IPs.
5. **Exit**

---

## 2. Running the Package CLI Directly

You can also run subcommands directly from the command line using python:

- **Username Lookup**:
  ```bash
  python3 -m osint.cli user <username> [--json-out <output_path>]
  ```
- **IP Lookup**:
  ```bash
  python3 -m osint.cli ip <ip_address> [--json-out <output_path>]
  ```
- **Domain WHOIS Lookup**:
  ```bash
  python3 -m osint.cli domain <domain_name> [--json-out <output_path>]
  ```
- **Email Breach Check**:
  ```bash
  python3 -m osint.cli email <email_address> [--json-out <output_path>]
  ```
- **File Metadata & Hash Extraction**:
  ```bash
  python3 -m osint.cli file <file_path> [--json-out <output_path>]
  ```

If you installed the package via `pip install .` or `pip install -e .`, you can use the command entrypoint directly:
```bash
osint-recon
```

---

## 3. Running Unit Tests

To verify that everything is working properly, run the test suite:

```bash
python3 -m pytest
```
