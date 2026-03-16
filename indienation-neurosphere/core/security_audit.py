import os
import subprocess

# @sector: 05 (Security Audit)
# @authority: INDIE-Founder

def check_intruders():
    # Mencari proses mencurigakan yang mengakses folder core selain python3
    try:
        cmd = "lsof +D ~/indienation-neurosphere/core | grep -v 'python3' | grep -v 'COMMAND'"
        intruders = subprocess.check_output(cmd, shell=True).decode()
        if intruders:
            print(f"🚨 [S05] Unauthorized Access Detected:\n{intruders}")
            return True
    except:
        pass
    return False

if __name__ == "__main__":
    if check_intruders():
        os.system("~/indienation-neurosphere/core/neuro_stop.sh")
