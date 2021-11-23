from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil
from Lab2 import Helpers


class ECBCipher(object):
    def __init__(self, enc):
        self.encryptedBlocksArray = enc
        self.decryptedBlocksArray = []
        self.cipherKey = b'syf23a2dDf9QklOp'
        self.textToEncrypt = Helpers.prepareText(Helpers.readInput("Lab2/input.txt"))


    def Encrypt(self):
        cipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in (list(Helpers.split(self.textToEncrypt,ceil(len(self.textToEncrypt)/16)))):
            returnArray = []
            for bit in cipher.encrypt(block):
                returnArray.append(bit)
            self.encryptedBlocksArray.append(returnArray)


    def Decrypt(self):
        decipher = AES.new(self.cipherKey, AES.MODE_ECB)
        for block in self.encryptedBlocksArray:
            returnArray = []
            blockOffset = 16 - len(block)
            while len(block)!=16:
                block.append(blockOffset)
            for byte in decipher.decrypt(bytes(block)):
                returnArray.append(byte)
            self.decryptedBlocksArray.append(returnArray)
