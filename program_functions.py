import csv
from encryption import Encrypt
import os
import time

'''
All the operations such reading, writing, update, and delete of the data.
'''

#reads the accounts.csv and returns a list in the format of [[account, username, password]]
def readAccounts():
    accountsCSV = []

    with open('files\\accounts.csv', 'r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=';')

        accountsCSV = list(csv_reader)

    return accountsCSV

#uses the append feature, prompt for account, username, and password then will append it to the last line of the csv
def addAccount():
    os.system('cls')
    print('Leave the field empty to abort.\n')
    with open('files\\accounts.csv', 'a+', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=';')

        newAccount = Encrypt().encrypt(input('Account: '))
        if newAccount.isspace() or not newAccount : return
        newUsername = Encrypt().encrypt(input('Username/Email: '))
        if newUsername.isspace() or not newUsername : return
        newPassword = Encrypt().encrypt(input('Password: '))
        if newPassword.isspace() or not newPassword : return

        csv_writer.writerow([newAccount, newUsername, newPassword])

#reads the CSV account and print the list in tabular form by using for loop and format
def showAccounts():
    csv_reader = readAccounts()
    index = 0

    print('{:<10} {:<20} {:<30} {:<30}'.format('Index','Account', 'Email/Username', 'Password'), end='\n\n')

    try:
        for line in csv_reader:
            account =   Encrypt().encrypt(line[0])
            username =  Encrypt().encrypt(line[1])
            password =  Encrypt().encrypt(line[2])
            print('{:<10} {:<20} {:<30} {:<30}'.format(index,account, username, password))
            index += 1
    except IndexError:
        pass

#deletes selected account
def deleteAccount():
    os.system('cls')
    print('Leave the field empty to abort.\n')
    index = 0
    csv_reader = readAccounts() #gets a list of all saved data

    showAccounts() 
    
    '''
    The try blocks are to check if the input index is valid. If invalid, it will return to the menu.
    If valid, the selected index will be deleted and the new list will overwrite the current data in the
    accounts.csv
    '''
    try:
        indexToDelete = int(input('\nSelect an index to delete: '))
    except ValueError:
        print('Invalid Index!')
        
    try:
        del csv_reader[indexToDelete]
    except IndexError:
        print('Invalid Index!')
    except UnboundLocalError:
        print('Invalid Index!')

    with open('files\\accounts.csv', 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=';')
        for row in csv_reader:
            csv_writer.writerow(row)

#edits selected account
def editAccount():
    os.system('cls')
    print('Leave the field empty to abort.\n')
    index = 0
    csv_reader = readAccounts()

    showAccounts()

    '''
    The try blocks are to check if the input index is valid. If invalid, it will return to the menu.
    If valid, the selected index will be get all the data and will be edited. The new list will overwrite 
    the current data in theaccounts.csv
    '''

    try:
        indexToEdit = int(input('\nSelect an index to edit: '))
    except ValueError:
        print('Invalid Index!')

    os.system('cls')
    print('Leave the field empty to abort.\n')

    try:
        print('Current Account: ' + Encrypt().encrypt(csv_reader[indexToEdit][0]))
        csv_reader[indexToEdit][0] = Encrypt().encrypt(input('New Account: '))
        if csv_reader[indexToEdit][0].isspace() or not csv_reader[indexToEdit][0] : return

        print('\nCurrent Username/Email: ' + Encrypt().encrypt(csv_reader[indexToEdit][1]))
        csv_reader[indexToEdit][1] = Encrypt().encrypt(input('New Username/Email: '))
        if csv_reader[indexToEdit][1].isspace() or not csv_reader[indexToEdit][1] : return

        print('\nCurrent Password: ' + Encrypt().encrypt(csv_reader[indexToEdit][2]))
        csv_reader[indexToEdit][2] = Encrypt().encrypt(input('New Password : '))
        if csv_reader[indexToEdit][2].isspace() or not csv_reader[indexToEdit][2] : return

        print(csv_reader[indexToEdit])
    except IndexError:
        print('Invalid Index!')
    except UnboundLocalError:
        print('Invalid Index!')

    with open('files\\accounts.csv', 'w', newline='') as csvFile:
        csv_writer = csv.writer(csvFile, delimiter=';')
        for row in csv_reader:
            csv_writer.writerow(row)

#CALL THIS FUNCTION WITH CAUTION!!! THIS DELETES ALL SAVED ACCOUNTS AND THE MASTERKEY
def wipeOut():
    with open('files\\accounts.csv', 'w') as csvFile:
        pass

    with open('files\\Key.txt','w') as passKey:
        pass

'''
reads the key.txt first and check if it's empty or not. If empty the program will not proceed until a master key is
succesfully registered. If Key.txt is not empty, the program will prompt the user to enter the correct key, if the
user got it wrong 3 times, it will delete all data including the master key and making the program start as new.
'''
def login():
    password = ''
    Tries = 3

    with open('files\\Key.txt','r') as passKey:
        password = Encrypt().encrypt(passKey.read())

    if password.isspace() or not password: #checks if Key.txt is empty
        masterKey = ''
        confirmKey = ''
        print('No Master Key Detected ')

        while True:
            while True:
                masterKey = input('Enter a New Master Key to Start: ')

                if not (masterKey.isspace() or not masterKey): break
                else:
                    os.system('cls')
                    print('Empty Master Key Is Not Allowed')

            os.system('cls')

            confirmKey = input('Re-enter to confirm: ')

            if masterKey == confirmKey:
                with open('files\\Key.txt','w') as passKey:
                    passKey.write(Encrypt().encrypt(masterKey))

                print('Signup Successful!\nLogging in...')
                time.sleep(2)
                break
            else:
                os.system('cls')
                print('Keys Did Not Match! Try Again.')

    else: #if not empty, user should enter the correct key
        while Tries >0:
            Password = Encrypt().encrypt(input("Enter Master Key: "))
            for line  in open("files\\Key.txt","r").readlines():
                loginDetail=line.split()
                if Password == loginDetail[0]:
                    print("Master Key Confirmed!")
                    time.sleep(1)
                    return
            Tries -=1
            os.system('cls')
            print("Wrong Key Try again", Tries," Attempt(s) Left")
            Tries +=1
            Tries -=1

        #if user failed, data will all be deleted and program will terminate
        wipeOut()
        print("\nATTEMPTS ALL USED! ALL DATA ARE NOW WIPED OUT!", '\nThis program will terminate after 5 seconds...')
        time.sleep(5)
        quit()

'''
To change the master key, the user must correctly enter the current master key. If failed, it will return to the menu.
If the input is correct, the user can set a new one and re-enter it to confirm. If correct, the master key will be 
updated. If not, the program will return to the menu
'''
def changeMasterKey():
    os.system('cls')
    password = ''

    with open('files\\Key.txt','r') as passKey:
        password = Encrypt().encrypt(passKey.read())

    confirmMasterKey = input('Enter Current Master Key: ')
    if confirmMasterKey.isspace() or not confirmMasterKey: return

    os.system('cls')

    if password == confirmMasterKey:
        newMasterKey = input('Enter new Master Key: ')
        if newMasterKey.isspace() or not newMasterKey: return

        os.system('cls')

        confirmMasterKey = input('Re-enter to confirm: ')

        if newMasterKey == confirmMasterKey:
            with open('files\\Key.txt','w') as passKey:
                passKey.write(Encrypt().encrypt(newMasterKey))
            
            print('Master Key Is Successfuly Updated! Returning to menu...')
            time.sleep(1)
        else:
            print('Keys did not match. Returning to menu...')
            time.sleep(1)

    else:
        print('Wrong Master Key. Returning to menu...')
        time.sleep(1)