from datetime import datetime

def parse_log(line):
    timestamp, ip, user, status = line.strip().split(',')
    return {
        "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "user": user,
        "status": status
    }
