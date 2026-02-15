from mitigation import blocked_ips

def show_dashboard():
    print("\n--- BLOCKED IPs ---")
    for ip, expiry in blocked_ips.items():
        print(f"{ip} blocked until {expiry}")
