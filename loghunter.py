import re
from collections import defaultdict
from datetime import datetime

KNOWN_IPS = set() # Tracks known IPs for successful logins

#---------------------------------------------------------------------------------------------------------------
# This function reads in the file for further use in later functions
def parse_log_file(log_path):
    with open(log_path, 'r', encoding = 'utf-8', errors = 'ignore') as file:
        return file.readlines()

# This function reads through the file and find and return a count of all failed login attempts
def detect_failed_logins(log_lines):
    failed_logins =  defaultdict(int)
    for line in log_lines:
        if "Failed password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_logins[ip] += 1
    return failed_logins

# This function reads through the file and returns the number of successful logins
def detect_successful_logins(log_lines):
    new_ips = set()
    successful_logins = []
    for line in log_lines:
        if "Accepted password" in line:
            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip_match:
                ip = ip_match.group(1)
                if ip not in KNOWN_IPS:
                    new_ips.add(ip)
                    KNOWN_IPS.add(ip)
                    successful_logins.append((line.strip(), ip))
    return successful_logins

# This function reads through the file and returns a list of new users that were detected
def detect_new_users(log_lines):
    user_creations = []
    for line in log_lines:
        if "new user" in line or "useradd" in line:
            user_creations.append(line.strip())
    return user_creations
#---------------------------------------------------------------------------------------------------------------

# This function takes all of the information that has been gathered and returns a general report
def generate_report(failed, successful, new_users):
    print("\n=== LogHunter Anomaly Report ===")
    print("\n[!] Failed Login Attempts:")
    for ip, count in failed.items():
        if count > 5:
            print(f" - {ip} had {count} failed login attempts")

    print("\n[+] Successful Logins from New IPs:")
    for entry, ip in successful:
        print(f" - {ip} | {entry}")

    print("\n[!] New User Creations:")
    for entry in new_users:
        print(f" - {entry}")
    print("\n === End of Report === \n")

#---------------------------------------------------------------------------------------------------------------
# Executes all of the functions above
def main():
    log_file_path = "C:/Users/darns/OneDrive/Desktop/Important/PythonProjects/auth.log"
    log_lines = parse_log_file(log_file_path)

    failed = detect_failed_logins(log_lines)
    successful = detect_successful_logins(log_lines)
    new_users = detect_new_users(log_lines)

    generate_report(failed, successful, new_users)

# Calls the main function
if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------------------------------------