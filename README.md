# OSINT Recon Toolkit

[![PyPI](https://img.shields.io/pypi/v/osint-toolkit?label=pyPI&color=informational&logo=python&logoColor=white)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Language: Python](https://img.shields.io/badge/language-Python-3670A0.svg)](https://www.python.org)

A professional, modular, and ethical OSINT (Open-Source Intelligence) toolkit for reconnaissance, digital footprint analysis, and threat intelligence enrichment. Built in Python and designed to be extensible with additional modules.

- Repository: https://github.com/PAIN-hub/OSINT-Recon
- Package name: `osint-toolkit`

Table of contents
- Features
- Installation
- Usage
- Command line entrypoint
- Project structure
- Modules
- Development & testing
- Security & ethics
- License
- Contributing
- Authors & support

---

## Features

- Username lookup across many public platforms
- IP address lookup (geolocation, ISP, ASN, proxy/VPN detection)
- Email breach checks (HaveIBeenPwned-compatible checks)
- Domain WHOIS lookup and basic domain intelligence
- Structured output export (JSON) saved in `reports/`
- Modular architecture: add new modules under `osint/modules`

## Installation

Requirements: Python 3.8+

Recommended (pip from GitHub):

```bash
pip install git+https://github.com/PAIN-hub/OSINT-Recon.git
```

Or install from a local clone:

```bash
git clone https://github.com/PAIN-hub/OSINT-Recon.git
cd OSINT-Recon
pip install -e .
# For development extras (tests, linters)
pip install -e .[dev]
```

You can also use the provided requirements file if you prefer:

```bash
pip install -r requirements.txt
```

## Usage

Run the interactive console interface:

```bash
# From the repository root
python3 recon.py

# Or use the installed console script
osint-recon
```

Follow the on-screen menu to run username, IP, email, and domain lookups. Reports are saved to the `reports/` directory as JSON files.

Example (username lookup):

```
$ python3 recon.py
Select an option: 1
Enter username: johndoe
[+] Checking across platforms...
[+] Report saved: reports/johndoe.json
```

## Command line entrypoint

The package installs a console script `osint-recon` that invokes the tool's main entrypoint. After installing the package, run:

```bash
osint-recon
```

## Project structure

```
OSINT-Recon/
├── osint/                  # Package modules and CLI
│   ├── cli.py              # CLI implementation
│   ├── recon.py            # (if present) older top-level script
│   ├── modules/            # Recon modules (username, ip, email, whois, ...)
│   └── utils/              # Utility helpers
├── reports/                # Generated JSON output
├── tests/                  # Unit tests
├── pyproject.toml          # Build configuration
├── setup.py                # Setuptools compatibility
├── requirements.txt        # Optional requirements list
├── MANIFEST.in             # Files included in source distribution
├── README.md               # This file
└── LICENSE                 # Project license (MIT)
```

## Modules

Add new reconnaissance modules in `osint/modules/`. Each module should expose a simple function interface and return JSON-serializable results. Example module responsibilities:

- `username_lookup.py` — query multiple public services for account matches
- `ip_lookup.py` — geolocation, ASN, ISP, proxy checks
- `email_breach.py` — query breach databases for compromised addresses
- `domain_whois.py` — return parsed WHOIS information

## Development & testing

Run tests with pytest:

```bash
pytest
```

For code style and formatting, recommended tools (available in `[dev]` extras): `black`, `flake8`, `isort`.

## Security & Ethics

This tool is intended for lawful, ethical, and authorized use only. By using this software you agree to:

- Only run recon on systems and accounts for which you have explicit permission.
- Respect privacy and applicable laws in your jurisdiction.
- Not use the tool to harass, stalk, or otherwise harm people or organizations.

The author and contributors are not responsible for misuse.

Refer to `ethics.md` for more detail on responsible OSINT practices.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

Summary (short):

```
MIT License
Copyright (c) PAIN-hub
```

## Contributing

We welcome contributions:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Open a pull request with a clear description

Please follow the existing code style and include unit tests where applicable.

## Authors & Support

- PAIN-hub — project author and maintainer

If you find this project useful, please star the repository ⭐ and consider opening issues or PRs to improve it.

Contact / Social:
- GitHub: https://github.com/PAIN-hub
- X: https://x.com/0x_beely

---

Thank you for using OSINT Recon Toolkit. Use responsibly.
