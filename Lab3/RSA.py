from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab2 import Helpers


class RSA(object):
    def __init__(self, text="", key=""):
        self.p = 31
        self.q = 19
        self.n = self.p * self.q
        self.fi = (self.p-1) * (self.q-1)

        if key != "":  # jeżeli użytkownik żadnego nie podał
            tempKey = str.encode(key)
            if len(tempKey) != 16:
                print("Klucz nie składa się z 16 bajtów !! Użyto domyślnego")
            else:
                self.cipherKey = tempKey
        if len(text) == 0:
            print("Nie podano wiadomości do szyfrowania!!")
        else:
            self.textToEncrypt = Helpers.prepareText(text)  # przygotowanie tekstu do szyfrowania - dopełnienie i zmiana na bajty


    def Encrypt(self):
        blocks = list(Helpers.split(self.textToEncrypt, ceil(len(self.textToEncrypt) / 16)))
        for block in blocks:
            tempToEncrypt =  Helpers.xor(Helpers.getBits(block),Helpers.getBits(self.currentCipherIV))
            returnArray = []
            cipher = AES.new(self.cipherKey, AES.MODE_ECB)
            for byt in cipher.encrypt(bytes(Helpers.getBytes(tempToEncrypt))):
                returnArray.append(byt)
            self.encryptedBlocksArray.append(returnArray)
            self.currentCipherIV = returnArray

    def Decrypt(self):
        self.currentCipherIV = self.cipherIV
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in self.encryptedBlocksArray:
            returnArray = []
            blockOffset = 16 - len(block)
            while len(block)!=16:
                block.append(blockOffset)
            for byt in decipher.decrypt(bytes(block)):
                returnArray.append(byt)
            xoredResult = Helpers.xor(Helpers.getBits(self.currentCipherIV), Helpers.getBits(returnArray))
            self.currentCipherIV = block
            print(xoredResult)
            self.decryptedBlocksArray.append(Helpers.getBytes(xoredResult))
            print(self.decryptedBlocksArray)