from datetime import datetime, timedelta
from config import BLOCK_DURATION_SECONDS

blocked_ips = {}

def block_ip(ip):
    blocked_ips[ip] = datetime.now() + timedelta(seconds=BLOCK_DURATION_SECONDS)

def is_blocked(ip):
    if ip in blocked_ips and blocked_ips[ip] > datetime.now():
        return True
    blocked_ips.pop(ip, None)
    return False
