# Linux Hardening Audit Tool

## 🔐 Overview
This is a Python-based tool that audits a Linux system for basic security compliance based on CIS benchmarks.

It checks:
- Firewall status (ufw)
- SSH root login setting
- File permissions for /etc/passwd and /etc/shadow
- Common rootkit indicators

## 🛠️ How to Use

### 1. Clone the repo or download `audit.py`:
git clone https://github.com/YOUR_USERNAME/linux-hardening-audit-tool.git
cd linux-hardening-audit-tool

2.Run the audit (you may need sudo):
sudo python3 audit.py

3.View the report:
The audit generates a audit_report_YYYYMMDD_HHMMSS.txt file with results.

Example Output
🔍 Starting Linux Security Audit...

✅ Firewall is active.
✅ SSH root login is disabled.
❌ /etc/shadow permissions are 666, expected 640.
✅ No common rootkit indicators found.

--- AUDIT COMPLETE ---
Score: 3/4
Security Compliance: 75%
🔒 Report saved as: audit_report_20250909_154332.txt


