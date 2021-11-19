from textwrap import wrap
import Lab1.BBS as gen

def getBinaryText(self, text): #metoda służąca do generowania ciągu binarnego z tekstu
    binStr = ""
    for char in text:
        binStr = binStr + str(bin(ord(char))[2:]).zfill(7)
    return binStr

def getBBSKey(self, length): #metoda do generowania klucza
    bbs = gen.BlumBlumShub()
    return bbs.bits(length)


class streamCipher(object):

    def __init__(self, path=""):
        with open(path) as f:
            self.plainText = f.read()
            f.close()
        self.publicBinaryMessage = getBinaryText(self, self.plainText)  #inicjalizacja binarnego ciągu z tekstu jawnego
        self.BBSKey = ""  #inicjalizacja klucza bbs
        self.cipherText = ""  #inicjalizacja szyfrogramu

    def setBBSKey(self):  #metoda służąca do ustawiania klucza
        self.BBSKey = getBBSKey(self, len(self.publicBinaryMessage))

    def setcipherText(self):  #metoda do ustawiania szyfrogramu
        cryptogram = ""
        for i in range(0, len(self.publicBinaryMessage)):
            cryptogram += str(int(self.BBSKey[i]) ^ int(self.publicBinaryMessage[i]))
        self.cipherText = cryptogram

    def decrypt(self):#metoda służąca do odszyfrowania szyfrogramu
        self.setBBSKey()
        self.setcipherText()

        plainBin = ""
        for i in range(0, len(self.cipherText)):
            plainBin += str(int(self.cipherText[i]) ^ int(self.BBSKey[i]))
        plainTxt = ""
        for ascipherText in wrap(plainBin, 7):
            plainTxt += chr(int(ascipherText, 2))

        return plainTxt
