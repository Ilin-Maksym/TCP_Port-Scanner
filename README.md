# TCP_Port-Scanner

# Description
  A small, modular, multithreaded TCP port scanner written in Python using only the "socket" and "concurrent.futures" libraries. The project demonstrates how the TCP three‑way handshake works and
shows how to build a simple, user‑friendly CLI tool.

# Features
  * Concurrent TCP port scanning using threads
  * Hostname resolution and reverse lookup
  * Flexible port specification (single, range, comma-separated)
  * Configurable per-port timeout and worker (thread) count
  * CLI entrypoint with human-readable output
  * Minimal external dependencies (standard library only)

# Project structure
  * port_scanner.py — core scanning logic (scan single port, scan multiple ports)
  * utils.py — helpers (host resolution, port-range parsing)
  * scanner.py — CLI entrypoint and orchestration

# Requirements
  * Python 3.8+ (works with modern 3.x)
  * No external packages

# Installation
  git clone "https://github.com/Ilin-Maksym/TCP_Port-Scanner.git"

  cd TCP_Port-Scanner<br />

  chmod +x main.py<br />

Alternatively run with "python3 main.py".

# Usage
  python3 scanner.py TARGET [options]

# Examples
  * Scan default ports 1-1024:
    python3 main.py example.com

  * Scan specific ports and ranges:
    python3 main.py 192.168.1.10 -p 22,80,443,8000-8100

  * Increase concurrency and timeout:
    python3 main.py 10.0.0.5 -p 1-65535 -w 500 -t 0.5

  * Show closed ports as well:
    python3 main.py example.com -s

# CLI options (short + long)
  * host (positional): Target hostname or IP
  * -p / --ports: Ports specification (default: 1-1024). Formats: 22, 20-25, 1-1024,3306,8080
  * -t / --timeout: Per-port timeout in seconds (default: 1.0)
  * -w / --workers: Max concurrent threads (default: 200)
  * -s / --show-closed: Also print closed ports

# Port specification rules
  * Single port: 22
  * Range: 1000-2000 (order-insensitive; 2000-1000 is accepted)
  * Multiple entries: comma-separated, e.g., 22,80,443,8000-8100
  * Ports are clamped to valid TCP port range (1–65535)

# Example output
Scanning example.com (93.184.216.34) 1024 ports with timeout=1.0s workers=200

   22/tcp OPEN

   80/tcp OPEN

  443/tcp OPEN


Scan completed in 2.34s. Open ports: 3
Open port list: 22, 80, 443

# Implementation notes & suggestions
  * Tweak --workers and --timeout for network conditions and target responsiveness.
  * The scanner uses TCP connect scans (SYN+ACK handshake via full connect). It is simple and reliable but slower than raw-socket SYN scans.
  * Consider adding rate limiting, randomized port order, retries, or banner grabbing for improved stealth and information gathering.
  * To export results, add JSON/CSV output options in the CLI.

# Responsible use
Only scan systems you own or are explicitly authorized to test. Unauthorized scanning may be illegal and/or considered malicious.

# Extending the tool
Ideas for enhancements:
  * JSON/CSV output
  * Banner grabbing for open ports (grab service banners)
  * Optional logging with timestamps
  * Limit scan rate and add backoff/retries
  * Asynchronous (asyncio) implementation for high-scale scans
  * Simple web UI or progress meter

# License
This project is licensed under the MIT - see the LICENSE file for details.
