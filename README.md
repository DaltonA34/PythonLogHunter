# LogHunter: Python Log File Anomaly Detector

--- 

##Overview
LogHunter is a Python-based tool designed to detect suspicious events in log files, such as brute-force attempts, unauthorized logins, and potential user privilege changes. This project was built to simulate real-world SOC analyst responsibilities using Python scripting and log analysis.

### Features
- Paarse  sytem authentication logs ('auth.log')
- Detect:
  - Repeated failed login attempts
  - Logins from new or suspicious IP addresses
  - User account changes (added/deleted users)
- Generate a detailed report of anomolies

---

## Project Structure
- logs/ # Sample Log Files
- src/ # Main scripts
- utils/ # Parsing and detection logic
- output/ #Report output

--- 

## Technology Used
- Python
- 're' for regex parsing
- 'datetime' for timestamp handling
- 'matplotlib' and 'pandas' for optimal visualization
- Potentially Used: 'requests' for IP geolocation or threat intel

--- 

## Setup

1. Clone the repo:
  git clone https://github.com/DaltonA34/PythonLogHunter.git
  cd PythonLogHunter
2. Install dependencies:
  pip  install -r requirements.txt
3. Run the tool:
  python src/PythonLogHunter.py logs/auth.log






















