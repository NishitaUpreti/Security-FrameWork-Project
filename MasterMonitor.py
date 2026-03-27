import subprocess
from datetime import datetime

VICTIM_PATH ="/home/nishita_upreti/SecurityProject/victims"
LOG_PATH = "/home/nishita_upreti/SecurityProject/security_alerts.log"

ui_len = int(input("Enter the length of your name: "))
ui_name = input("Enter name: ")
ui_ch = input("Would you like to by a book? [y/n] : ")
ui_book_choice = int(input("Which book would you like to buy? "))
ui_quantity = int(input("How many books would you like to buy? "))


if len(ui_name) > ui_len:
	alert = f"[!!!] ALERT : POTENTIAL OVEFLOW ATTEMPT! | Time : {datetime.now()}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

if ui_name.count("%p")>2 or ui_name.count("%x")>2:
	alert = f"[!!!] ALERT : POTENTIAL STRING FORMAT LEAK! | Time : {datetime.now()}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

if ui_book_choice<0 or ui_book_choice>4:
	alert = f"[!!!] ALERT : POTENTIAL OUT-OF-BOUND ATTACK! | Time : {datetime.now()}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

if ui_quantity>14316558:
	alert = f"[!!!] ALERT : POTENTIAL TRIGGER OF INTEGER WRAP! | Time : {datetime.now()}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

payload = str(ui_len) + "\n" +str(ui_name) + "\n" + str(ui_ch) + "\n" +str(ui_book_choice) + "\n" + str(ui_quantity)


process = subprocess.Popen(VICTIM_PATH, stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output, error = process.communicate(input = payload.encode())


if(process.returncode!=0):
	alert = f"[!!!] ALERT : MEMORY VIIOLATION | Time : {datetime.now()} | Status : {process.returncode}"
	print(alert)

	with open(LOG_PATH,'a') as f:
		f.write(alert+"\n")

print("\n-------OUTPUT--------\n")
print(output.decode())

