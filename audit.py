import os
import subprocess
from datetime import datetime

report = []
score = 0
total_checks = 0

def log(message):
    print(message)
    report.append(message)

def run_cmd(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        return result.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return ""

def check_firewall():
    global score, total_checks
    total_checks += 1
    fw = run_cmd("sudo ufw status")
    if "Status: active" in fw:
        log("✅ Firewall is active.")
        score += 1
    else:
        log("❌ Firewall is NOT active.")
    
def check_ssh_settings():
    global score, total_checks
    total_checks += 1
    sshd_config = "/etc/ssh/sshd_config"
    if os.path.exists(sshd_config):
        content = open(sshd_config).read()
        if "PermitRootLogin no" in content:
            log("✅ SSH root login is disabled.")
            score += 1
        else:
            log("❌ SSH root login is ENABLED (risk).")
    else:
        log("❌ SSH config file not found.")

def check_file_permissions():
    global score, total_checks
    critical_files = {
        "/etc/passwd": "644",
        "/etc/shadow": "640"
    }

    for file, expected_perm in critical_files.items():
        total_checks += 1
        try:
            stat = os.stat(file)
            actual_perm = oct(stat.st_mode)[-3:]
            if actual_perm == expected_perm:
                log(f"✅ {file} permissions are correct ({actual_perm}).")
                score += 1
            else:
                log(f"❌ {file} permissions are {actual_perm}, expected {expected_perm}.")
        except:
            log(f"❌ Could not read permissions for {file}.")

def check_rootkit_signs():
    global score, total_checks
    total_checks += 1
    suspicious_files = [
        "/dev/.udev", "/dev/.init", "/dev/.tmp", "/dev/.kit"
    ]
    found = False
    for path in suspicious_files:
        if os.path.exists(path):
            found = True
            log(f"❌ Suspicious rootkit path found: {path}")

    if not found:
        log("✅ No common rootkit indicators found.")
        score += 1

def generate_report():
    log("\n--- AUDIT COMPLETE ---")
    log(f"Score: {score}/{total_checks}")
    log("Security Compliance: {:.0f}%".format((score/total_checks)*100 if total_checks else 0))

    # Save to file
    filename = f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for line in report:
            f.write(line + "\n")
    print(f"\n🔒 Report saved as: {filename}")

if __name__ == "__main__":
    log("🔍 Starting Linux Security Audit...\n")
    check_firewall()
    check_ssh_sett
