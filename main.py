import os
import time
from program_functions import *


'''
This file is where the flow of the program is. The operations are in the program_functions.py module.
In short this module if for calling functions only.
'''

running = True

def stopProgram():
    global running
    running = False

def invalidChoice(): #error catcher for the <dict>.get() function
    print('Invalid Choice!')

switchDict = {
    1: addAccount,
    2:editAccount,
    3: deleteAccount,
    4: changeMasterKey,
    5: stopProgram
}


login()

os.system('cls')

#main flow, it will keep running until certain conditions are met
while running:
    print('Accounts Manager version 1.0.0','\nCreated 2021\n\n')
    showAccounts()

    print(
        '\n[1] Add Account',
        '\n[2] Edit Account',
        '\n[3] Delete Account'
        '\n[4] Change Master Key'
        '\n\n[Enter Any Other Key To Exit]'
    )

    try:
        userOption = int(input('\nSelect an Option: '))
    except ValueError:
        break

    switchDict.get(userOption, invalidChoice)()

    os.system('cls')

print('Program Terminating...')
time.sleep(3)