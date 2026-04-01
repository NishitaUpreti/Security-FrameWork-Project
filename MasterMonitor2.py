import sys
import pexpect
from datetime import datetime

VICTIM_PATH = "/home/nishita_upreti/SecurityProject/victim"
LOG_PATH = "/home/nishita_upreti/SecurityProject/security_alerts"

def run_monitor():

	try:
		child = pexpect.spawn(VICTIM_PATH, encoding='utf-8')
		child.logfile_read = sys.stdout


		child.expect("Enter the length of your name: ");
		ui_len = int(input());
		child.sendline(str(ui_len));

		ui_name = input("Enter name: ");
		child.sendline(ui_name);


		if ui_len < len(ui_name):
			alert = f"\n[!!!] ALERT : POTENTIAL OVERFLOW ATEMPT! | Time: {datetime.now()}"
			print(alert)
			with open(LOG_PATH, "a") as f:
				f.write(alert + "\n")

		if ui_name.count("%p") > 2 or ui_name.count("%x")>2:
			alert = f"\n[!!!] ALERT : POTENTIAL FORMAT STRING ATTACK! | Time: {datetime.now()}"
			print(alert)
			with open(LOG_PATH, "a") as f:
				f.write(alert + "\n")

		while True:
			child.expect("Do you want to buy a book?")
			ui_ch = input()
			child.sendline(ui_ch)

			if ui_ch == "n":
				print("\n---------Exiting shop---------\n")
				break


			child.expect("Which book would you like to buy?")
			ui_book_choice = int(input())
			child.sendline(str(ui_book_choice))

			child.expect("How many books would you like to buy?")
			ui_quantity = int(input())
			child.sendline(str(ui_quantity))

			if ui_quantity>17179870:
				alert = f"\n[!!!] ALERT : POTENTIAL INTEGER WRAP TRIGGER! | Time: {datetime.now()}"
				print(alert)
				with open(LOG_PATH, "a") as f:
					f.write(alert + "\n")
		child.expect(pexpect.EOF)
		#python might lose the terminal before total_cost is printed thus end of file(cpp reacher return 0) is required.

	except pexpect.exceptions.EOF:
		print("\n[!] The C++ program terminated unexpectedly.")
		#Crash detector:- catches EOF if it happens in the middle of conversation.

	except pexpect.exceptions.TIMEOUT:
		print("\n[!] The python script got stuck waiting for C++ program")
		#Typo/timeout:- the python script got stuck waiting for the C++ program.

	except Exception as e:
		print(f"\n[!] An error occured:  {e}")
		#Crash detector:- standerd exception handling.

if __name__ == "__main__":
	run_monitor()
