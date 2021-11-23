from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab3 import Helpers


class RSA(object):
    def __init__(self, signature = ""):
        self.p = 211 #Helpers.getRandomPrimeNumber()
        self.q = 101 #Helpers.getRandomPrimeNumber()
        self.n = self.p * self.q
        self.phi = (self.p-1) * (self.q-1)
        self.e = Helpers.getE(self.phi)
        self.d = Helpers.getD(self.e,self.phi)
        self.encryptedMessage = []
        self.decryptedMessage = []
        self.signature = signature
        self.encryptedSignature = []
        self.decryptedSignature = []
        self.input = Helpers.readInput("Lab3/input.txt")


    def Encrypt(self):
        temp=""
        for char in str.encode(self.input):
            temp+=str(int(Helpers.digitsSave(char)))
        print("input:")
        print(temp)
        for m in wrap(temp,3):
            self.encryptedMessage.append(int(m)**self.e%self.n)
        for m in wrap(self.signature,1):
            self.encryptedSignature.append(int(ord(m))**self.d%self.n)
        print("zaszyfrowany podpis: ")
        print(self.encryptedSignature)
        print("zaszyfrowana wiadomość: ")
        Helpers.saveArrayToFile(self.encryptedMessage, "Lab3/Outputs/RsaEncrypted.txt")

    def Decrypt(self):
        for char in self.encryptedMessage:
            decryptedChar = int(char) ** self.d % self.n
            self.decryptedMessage.append(Helpers.digitsSave(decryptedChar, False))
        for char in self.encryptedSignature:
            decryptedChar = int(char) ** self.e % self.n
            self.decryptedSignature.append(chr(decryptedChar))
        print("odszyfrowany podpis: ")
        print(self.decryptedSignature)
        print("odszyfrowana wiadomość: ")
        Helpers.saveArrayToFile(self.decryptedMessage, "Lab3/Outputs/RsaDecrypted.txt", True)