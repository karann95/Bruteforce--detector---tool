from collections import defaultdict, deque
from config import MAX_FAILED_ATTEMPTS, TIME_WINDOW_SECONDS

failed_attempts = defaultdict(deque)

def detect_bruteforce(entry):
    if entry["status"] != "FAIL":
        return False

    key = (entry["ip"], entry["user"])
    attempts = failed_attempts[key]
    attempts.append(entry["timestamp"])

    while (attempts[-1] - attempts[0]).seconds > TIME_WINDOW_SECONDS:
        attempts.popleft()

    return len(attempts) >= MAX_FAILED_ATTEMPTS
