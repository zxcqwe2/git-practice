#!/usr/bin/env python3
import subprocess
import time
import os
from prometheus_client import start_http_server, Gauge, Counter, Info

REQUESTS = Counter("hostmetrics_requests_total", "Total number of scrapes")
HOST_TYPE_INFO = Info("host_environment", "Host environment (vm/container/physical)")
HOST_TYPE_GAUGE = Gauge("host_type", "Host type as gauge with label", ["type"])

def _run(cmd):
    try:
        return subprocess.run(cmd, check=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    except Exception:
        return None

def detect_host_type():

    r = _run(["/usr/bin/systemd-detect-virt", "--container"])
    if r and r.returncode == 0:
        return "container"
    r = _run(["/usr/bin/systemd-detect-virt", "--vm"])
    if r and r.returncode == 0:
        return "vm"


    if os.path.exists("/.dockerenv"):
        return "container"
    try:
        with open("/proc/1/cgroup", "r") as f:
            cg = f.read().lower()
            if "docker" in cg or "containerd" in cg or "kubepods" in cg or "podman" in cg or "lxc" in cg:
                return "container"
    except Exception:
        pass


    return "physical"

def set_host_type_metrics(host_type):

    HOST_TYPE_INFO.info({"type": host_type})

    for t in ("vm", "container", "physical"):
        HOST_TYPE_GAUGE.labels(type=t).set(1.0 if t == host_type else 0.0)

def main():
    port = int(os.getenv("PORT", "8080"))
    start_http_server(port)
    host_type = None

    while True:

        new_type = detect_host_type()
        if new_type != host_type:
            host_type = new_type
            set_host_type_metrics(host_type)
        REQUESTS.inc()
        time.sleep(60)

if __name__ == "__main__":
    main()
