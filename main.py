from config import LOG_FILE
from log_parser import parse_log
from detector import detect_bruteforce
from mitigation import block_ip, is_blocked
from alerts import send_alert
from admin_dashboard import show_dashboard

def scan_logs():
    with open(LOG_FILE) as file:
        for line in file:
            entry = parse_log(line)

            if is_blocked(entry["ip"]):
                continue

            if detect_bruteforce(entry):
                block_ip(entry["ip"])
                send_alert(entry["ip"], entry["user"])

while True:
    print("\n=== Brute Force Detection System ===")
    print("1. Scan authentication logs")
    print("2. View blocked IPs")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        scan_logs()
    elif choice == "2":
        show_dashboard()
    elif choice == "3":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")
