from Crypto.Cipher import AES
from base64 import b64decode
import binascii
from textwrap import wrap
import random
from math import ceil

def getBytes(bits):
    blocks = wrap(bits,8)
    bytes = []
    for block in blocks:
        bytes.append(int(block,2))
    return bytes

def getBits(bytes):
    outPut =""
    for b in bytes:
        outPut+= str(bin(b)[2:]).zfill(8)
    return outPut

def xor(firstBits,secondBits):
    outPutBits = ""
    for i in range(0,len(firstBits)):
        outPutBits += str(int(firstBits[i]) ^ int(secondBits[i]))
    return outPutBits

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def SaveResult(filePath, content):
    f = open(filePath, "a")
    f.truncate(0)
    f.write(content)
    f.close()

def pad(m): # dopełnienie tekstu do 128 bitowych bloków
    return m+chr(16-len(m)%16)*(16-len(m)%16)

def unpad(ct): # powrót do wiadomości pierwotnej
    return ct[:-ord(ct[-1])]

def prepareText(text):
    paddedText = pad(text)
    return str.encode(paddedText)

def saveDecryptedMessageFromBlocks(blocks, filePath, isEncrypted=True):
    f = open(filePath, "a", encoding="utf-8")
    f.truncate(0)
    returnString = ""
    k = 0
    for block in blocks:
        for char in block:
            returnString+= chr(char)
        returnString += " \n"
    f.write(unpad(returnString)) if not isEncrypted else f.write(returnString)

def generateInitialVector():
    key = ""
    for i in range(0,16):
        key+= str(bin(random.randint(0,255)[2:])).zfill(8)
    return key

def readInput(path):
    with open(path) as f:
        content = f.readlines()
    return str(content[0])