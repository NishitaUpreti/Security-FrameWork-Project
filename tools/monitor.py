import subprocess
from datetime import datetime

VICTIM_PATH ="/home/nishita_upreti/SecurityProject/attacks/victims"
LOG_PATH = "/home/nishita_upreti/SecurityProject/logs/security_alerts.log"

process = subprocess.Popen(VICTIM_PATH, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

if(process.returncode!=0):
	alert = f"[!!!] ALERT : MEMORY VIIOLATION | Time : {datetime.now()} | Status : {process.returncode}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

else:
	print("[+] Program finished safely")



