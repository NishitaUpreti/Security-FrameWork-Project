# AUTOMATED SECURITY PROXY AND VULNERABILITY MONITOR

An interactive Inter-Process Communication (IPC) wrapper written in python that acts as a real-time security monitor for vulnerable C/C++ applications.

This project demonstrates how to intercept user input, scan it for malicious inputs(Buffer Overflows, Format Strings, Integer Wraps), and log attacksin real time before they can exploit the underlying executable.

##Core Features:-
1) Real Time Interception:- Utilizes `pexpect` to create a live proxy between the user's keyboard and the target C++ binary.
2) Buffer Overflow Detection:- Dynamically compares the mathematical length of an inputted string against the user's declared allocation size before paassing it to memory.
3) Format String Prevention:- Scans inputs for malicious memory-leak format specifiers(e.g., `%p`,`%x`).
4) Integer Wrap:- Monitors mathematical inputs (like qtuantity/price multipliers) to prevent maximum integer boudary bypassing.
5) Automated Forensic Logging:- Silently appends all triggered security alerts to a background `.log` file with precise timestamps.

##Prerequsites:-
To run this MasterMonitor, you need a Linux environment with the following installed:-
* `python3`
* `g++`
* `pexpect`

```bash
sudo apt update && sudo apt install python3-pexpect
#For installing required python library

## Run:- pyhton3 MasterMonitor2.py

Note:- MasterMonitor.py :- Works like a mail:- takes all the inputs at once and then mails it to MAsterVictim.cpp
	MasterMonitor2.py :- Works like a telephone :- takes one input then sends it to cpp waits for it to process teh code and then asks for another input that cpp needs .
	
