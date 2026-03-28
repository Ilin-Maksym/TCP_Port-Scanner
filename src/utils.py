import socket;

from typing import Tuple;

def resolve_host(host: str) -> Tuple[str, str]:
  try:
    ip = socket.gethostbyname(host);

    try:
      hostname = socket.gethostbyaddr(ip)[0];
    except Exception:
      hostname = host;

    return ip, hostname;
  except Exception:
    raise ValueError(f"Cannot resolve host: {host}");

def parse_port_range(r: str) -> list:
  ports = set();
  parts = [p.strip() for p in r.split(",") if p.strip()];

  for part in parts:
    if "-" in part:
      start, end = part.split("-", 1);
      start_i = int(start);
      end_i = int(end);

      if start_i > end_i:
        start_i, end_i = end_i, start_i;

      ports.update(range(max(1, start_i), min(65535, end_i) + 1));
    else:
      pi = int(part);

      if 1 <= pi <= 65535:
        ports.add(pi);

  return sorted(ports);
