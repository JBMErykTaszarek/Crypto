import Lab1.Tests as tests
import Lab1.StreamCipher as stCi
import Lab1.BBS as bbs
import Lab2.ECB as ecb
import Lab2.CBC as cbc
import Lab2.PBC as pbc
import Lab3.RSA as rsa
from Lab2 import Helpers


def Lab1(bbs):
    streamCipher = stCi.streamCipher(path="Lab1/someText.txt")
    decrypted = streamCipher.decrypt()
    print(len(streamCipher.publicBinaryMessage))
    bbs = bbs.BlumBlumShub()
    binary = bbs.bits(20000)
    print(bbs.bits(1000000))

    f = open("Lab1/Outputs/someTextEncrypted.txt", "a")
    f.truncate(0)
    f.write(binary)
    f.close()

    f = open("Lab1/Outputs/someTextDecrypted.txt", "a")
    f.truncate(0)
    f.write(decrypted)
    f.close()

    test = tests.StandardTests("Lab1/Outputs/someTextEncrypted.txt")

    test.oneBitTest()
    test.seriesTest()
    test.longSeriesTest()
    test.pokerTest()

def Lab2():
    ecbObj = ecb.ECBCipher("asdghe3#$%aasd6rgdFWW$#$yerye6434^#$#4teqRhjSRTnfzetye6s4z5t", "xyzW3abdefsykl12")
    ecbObj.Encrypt()
    ecbObj.Decrypt()
    Helpers.saveDecryptedMessageFromBlocks(ecbObj.encryptedBlocksArray, "Lab2/Outputs/EcbEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(ecbObj.decryptedBlocksArray, "Lab2/Outputs/EcbDecrypted.txt", False)

    cbcObj = cbc.CBCCipher("asdghe3#$%aasd6rgdFWW$#$yerye6434^#$#4teqRhjSRTnfzetye6s4z5t", "xyzW3abdefsykl12")
    cbcObj.Encrypt()
    cbcObj.Decrypt()
    Helpers.saveDecryptedMessageFromBlocks(cbcObj.encryptedBlocksArray, "Lab2/Outputs/CbcEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(cbcObj.decryptedBlocksArray, "Lab2/Outputs/CbcDecrypted.txt", False)

    pbcObj = pbc.PBCCipher("asdghe3#$%aasd6rgdFWW$#$yerye6434^#$#4teqRhjSRTnfzetye6s4z5t", "xyzW3abdefsykl12")
    pbcObj.Encrypt()
    pbcObj.Decrypt()
    Helpers.saveDecryptedMessageFromBlocks(pbcObj.encryptedBlocksArray, "Lab2/Outputs/PbcEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(pbcObj.decryptedBlocksArray, "Lab2/Outputs/PbcDecrypted.txt", False)

def Lab3():

    rsaObj = rsa.RSA()
    rsaObj.Encrypt()
    rsaObj.Decrypt()

if __name__ == '__main__':
    #Lab1(bbs)

    #Lab2()

    Lab3()
    #zadanie 2
    '''
    blockA = bc.blockCipher(text ="asdghe3#$%aasd6rgdFWW$#$yerye6434^#$#4teqRhjSRTnfzetye6s4z5t", key = "xyzW3abdefsykl12")
    blockA.ecbEncrypt()
    blockA.cipherArray[0].remove(blockA.cipherArray[0][0])
    blockA.ecbDecrypt()

    print(bytes(0).decode())
    blockB = bc.blockCipher(text ="Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%Jestem nddda!@#$%", key = "xyzW3abdefsykl12")
    blockB.cbcEncrypt()
    blockB.cipherArray[3].remove(blockB.cipherArray[3][4])
    blockB.cbcDecrypt()

    blockC = bc.blockCipher(text ="A00000000000000ZA00000000000000ZA00000000000000ZA00000000000000Z", key = "xyzW3abdefsykl12")
    blockC.cfbEncrypt()
    blockC.cipherArray[2].remove(blockC.cipherArray[2][15])
    blockC.cfbDecrypt()
    '''
