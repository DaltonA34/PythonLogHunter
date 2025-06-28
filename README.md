# LogHunter: Python Log File Anomaly Detector

--- 

## Overview
LogHunter is a Python-based tool designed to detect suspicious events in log files, such as brute-force attempts, unauthorized logins, and potential user privilege changes. This project was built to simulate real-world SOC analyst responsibilities using Python scripting and log analysis.

### Features
- Failed login Detection: Identifies IP addresses with multiple failed  SSH login attempts
- Successful Login Tracking: Detects successful logins from previously unseen IPs
- New User Alerts -  Flags lines suggesting creation of new user accounts

---

## How it works
The Python script parses your auth.log file line-by-line and uses regular expressions to extract:
- IP addresses attempting logins
- Indicators of failed/successful login attempts
- User creation events (useradd,  new user)
- All findings are output in a formatted and easy to read anomoly report

--- 

## Technology Used
- Python
- 're' for regex parsing
- 'datetime' for timestamp handling

--- 

## Security Notes
- Do not run this on systems you do not own or have explicit permission to audit
- Always analyze logs in a safe and secure enviornment

--- 

## Future Improvements
- Export report to a text  or HTML file
- Add CLI flags for custom log paths and thresholds
- Add detection for brute for patterns across time

---

## Author
Dalton Armstrong
Cybersecurity Major | Christopher Newport University





















