'''
This module is responsible for the encryption and decryption of data. import this module and call
Encrypt().encrypt(<arg>) to encrypt and decrypt
'''
class Encrypt:
    def __init__(self):
        self.alphabetOriginal = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.alphabetReverse = sorted(self.alphabetOriginal, reverse=True)
        self.inputList = []
        self.encryptedList = []

    def encrypt(self, userInput):
        for progIteration in range(0, len(userInput)):
            self.inputList.append(userInput[progIteration])

        for indexInput in range(0, len(self.inputList)):
            for indexOriginal in range(0, 62):

                if self.inputList[indexInput] == self.alphabetOriginal[indexOriginal]:
                    self. encryptedList.append(self.alphabetReverse[indexOriginal])
                    break

                elif self.inputList[indexInput] not in self.alphabetOriginal:
                    self.encryptedList.append(self.inputList[indexInput])
                    break

        returnValue = ''

        for append in self.encryptedList:
            returnValue += append

        return returnValue
