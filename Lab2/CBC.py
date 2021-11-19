from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab2 import Helpers


class ECBCipher(object):
    def __init__(self, text="", key=""):
        self.encryptedBlocksArray = []
        self.decryptedBlocksArray = []
        self.key = Helpers.generateInitialVector()
        self.cipherKey = b'xyzW3abdefsykl12'  # przypisanie klucza domyślnego
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
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in (list(Helpers.split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16)))):
            returnArray = []
            for bit in cipher.encrypt(block):
                returnArray.append(bit)
            self.encryptedBlocksArray.append(returnArray)

    def Decrypt(self):
        decipher = decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in self.encryptedBlocksArray:
            returnArray = []
            blockOffset = 16 - len(block)
            while len(block)!=16:
                block.append(blockOffset)
            for bit in decipher.decrypt(bytes(block)):
                returnArray.append(bit)
            self.decryptedBlocksArray.append(returnArray)
