#!/bin/env python3
import argparse;
import sys;
import time;

from src import scan_ports, resolve_host, parse_port_range;

def main():
  p = argparse.ArgumentParser(description="Multithreaded TCP port scanner");

  p.add_argument("host", help="Target hostname or IP");
  p.add_argument("-p", "--ports", default="1-1024", help="Ports (single, range, comma-separated). Default: 1-1024");
  p.add_argument("-t", "--timeout", type=float, default=1.0, help="Per-port timeout (seconds)");
  p.add_argument("-w", "--workers", type=int, default=200, help="Max concurrent threads");
  p.add_argument("-s", "--show-closed", action="store_true", help="Also print closed ports");

  args = p.parse_args();

  try:
    ip, hostname = resolve_host(args.host);
  except ValueError as e:
    print(e, file=sys.stderr);
    sys.exit(1);

  ports = parse_port_range(args.ports);

  if not ports:
    print("No valid ports parsed.", file=sys.stderr);
    sys.exit(1);

  print(f"Scanning {hostname} ({ip}) {len(ports)} ports with timeout={args.timeout}s workers={args.workers}");

  start = time.time();
  results = scan_ports(ip, ports, timeout=args.timeout, max_workers=args.workers);
  elapsed = time.time() - start;

  open_ports = [p for p, open_ in results if open_];

  for port, open_ in results:
    if open_:
      print(f"P{port:5d}/tcp OPEN");
    elif args.show_closed:
      print(f"{port:5d}/tcp closed");

  print(f"\nScan completed in {elapsed:.2f}s. Open ports: {len(open_ports)}");

  if open_ports:
    print("Open port list:", ", ".join(str(p) for p in open_ports));

if __name__ == "__main__":
  main();
