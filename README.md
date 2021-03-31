# Simple-Python-Password-Manager
A terminal password manager written in python

What is this program?
This program's purpose is to store passwords. It will list what type of account(e.g. facebook account), username/email used to enter, and the password.
The data will be stored in a csv file but it will be encrypted. To decrypt it, the data must be read by the program.

How to run?
For the best experience, just double click the main.py. Of course it can be ran in any Python IDE.

How to use?
The user must enter the Master Key first. If nothing is set, the program will ask the user to set one. The user will only have 3 attempts to enter the master key if all of these attempts are used up, all the data in the program will be deleted including the master key. Thus, the program will be on  a "factory reset" mode.


[1] Add Account
This lets the user to add new entry. The user must enter the account type, username/email, and password. It will return to the menu and show the newly added entry.

[2]Edit Account
Choose the index to edit. Then the user can view the current data and enter a new one.

[3]Delete Account
Choose the index of the account to delete and it will be deleted.

[4]Change Master Key
Use this option to change the password needed to use this program

If any other key beside the ones above, the program will be terminated. 
