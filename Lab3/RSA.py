from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab3 import Helpers


class RSA(object):
    def __init__(self):
        self.p = 31
        self.q = 19
        self.n = self.p * self.q
        self.phi = (self.p-1) * (self.q-1)
        self.e = Helpers.getE(self.phi)
        self.d = Helpers.getD(self.e,self.phi)
        self.encryptedMessage = []
        self.decryptedMessage = []
        self.input = Helpers.readInput("Lab3/input.txt")


    def Encrypt(self):
        temp=""
        for char in str.encode(self.input):
            temp+=str(int(Helpers.digitsSave(char)))
        print("input:")
        print(temp)
        for m in wrap(temp,3):
            self.encryptedMessage.append(int(m)**self.e%self.n)
        print("zaszyfrowana")
        print(self.encryptedMessage)

        Helpers.saveArrayToFile(self.encryptedMessage, "Lab3/Outputs/RsaEncrypted.txt")

    def Decrypt(self):
        for char in self.encryptedMessage:
            decryptedChar = int(char) ** self.d % self.n
            self.decryptedMessage.append(Helpers.digitsSave(decryptedChar, False))
        print("odszyfrowana")
        print(self.decryptedMessage)
        Helpers.saveArrayToFile(self.decryptedMessage, "Lab3/Outputs/RsaDecrypted.txt", True)