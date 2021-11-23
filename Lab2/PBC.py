from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab2 import Helpers


class PBCCipher(object):
    def __init__(self, enc, key=""):
        self.encryptedBlocksArray = enc
        self.decryptedBlocksArray = []
        self.cipherKey = b'xyzW3abdefsykl12'
        self.cipherIV = b'1122334411223344'
        self.currentCipherIV = self.cipherIV
        self.textToEncrypt = Helpers.prepareText(Helpers.readInput("Lab2/input.txt"))


    def Encrypt(self):
        blocks = list(Helpers.split(self.textToEncrypt, ceil(len(self.textToEncrypt) / 16)))
        for block in blocks:
            tempToEncrypt =  Helpers.xor(Helpers.getBits(block),Helpers.getBits(self.currentCipherIV))
            returnArray = []
            cipher = AES.new(self.cipherKey, AES.MODE_ECB)
            for byt in cipher.encrypt(bytes(Helpers.getBytes(tempToEncrypt))):
                returnArray.append(byt)
            self.encryptedBlocksArray.append(returnArray)
            self.currentCipherIV = block

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
            self.currentCipherIV = Helpers.getBytes(xoredResult)
            self.decryptedBlocksArray.append(Helpers.getBytes(xoredResult))
