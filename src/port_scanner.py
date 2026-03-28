import socket;

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable, List, Tuple

def scan_port(host: str, port: int, timeout: float = 1.0) -> Tuple[int, bool]:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(timeout);

    try:
      s.connect((host, port));

      return port, True;
    except (socket.timeout, ConnectionRefusedError):
      return port, False;
    except OSError:
      return port, False;

def scan_ports(host: str, ports: Iterable[int], timeout: float = 1.0, max_workers: int = 100) -> List[Tuple[int, bool]]:
  results: List[Tuple[int, bool]] = [];

  with ThreadPoolExecutor(max_workers = max_workers) as ex:
    future_to_port = {ex.submit(scan_port, host, p, timeout): p for p in ports};

    for fut in as_completed(future_to_port):
      try:
        results.append(fut.result());
      except Exception:
        p = future_to_port[fut];
        results.append((p, False));
  return sorted(results, key=lambda x: x[0]);
