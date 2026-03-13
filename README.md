#Security Framework Project
This sytem monitors a C++ application for memory corruptions and logs security alerts in real-time.

##SetUp Instructions
To get this running on your local machine follow these steps:

### 1.Compile the Vulnerable App
Run this command to disable mordern security protectins (required for the demo):
g++ -fno-stack-protector -z execstack -no-pie attacks/overflow_victim.app -o attacks/victim

### 2. Run the Security Monitor
Start the python script it will act as a wrapper for the C++ program:
python3 tools/monitor.py

### 3. Test the Detection
When prompted for a username, enter a long string (eg:-  a name with 30 characters)
The program will crash and the monitor will catch the "Status -7" or "Status -11" and write it on the log.

## File overview
- /attacks: Contains the vulnerable C++ source.
- /tools: Contains the python monitor logic.
- /logs: Stores the history of detected attacks.
