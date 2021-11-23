import Lab1.Tests as tests
import Lab1.StreamCipher as stCi
import Lab1.BBS as bbs
import Lab2.ECB as ecb
import Lab2.CBC as cbc
import Lab2.PBC as pbc
import Lab3.RSA as rsa
from Lab2 import Helpers
import time


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
    ecbObj = ecb.ECBCipher(enc = [[237, 134, 172, 182, 180, 106, 226, 183, 61, 89, 184, 135, 21, 33, 23, 172], [121, 130, 106, 109, 182, 118, 169, 191, 17, 156, 123, 146, 128, 223, 114, 76], [106, 58, 33, 176, 209, 96, 231, 82, 197, 121, 165, 141, 111, 108, 121, 95], [109, 120, 93, 101, 97, 176, 175, 55, 110, 161, 141, 159, 59, 112, 189, 100], [148, 138, 74, 228, 105, 91, 34, 81, 222, 195, 197, 232, 231, 81, 241, 224]]
)

    start = time.time()
    #ecbObj.Encrypt()
    ecbObj.Decrypt()
    end = time.time()

    print(end - start)

    Helpers.saveDecryptedMessageFromBlocks(ecbObj.encryptedBlocksArray, "Lab2/Outputs/EcbEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(ecbObj.decryptedBlocksArray, "Lab2/Outputs/EcbDecrypted.txt", False)

    cbcObj = cbc.CBCCipher(enc = [[80, 60, 243, 207, 43, 68, 185, 243, 15, 3, 170, 68, 248, 2, 33, 88], [232, 220, 23, 247, 153, 161, 186, 7, 245, 244, 159, 118, 210, 123, 28, 39], [239, 29, 94, 98, 23, 93, 229, 3, 165, 74, 52, 169, 229, 64, 133, 136], [148, 5, 251, 237, 222, 66, 57, 114, 2, 165, 235, 97, 92, 176, 158, 149], [152, 246, 104, 164, 147, 101, 160, 253, 20, 99, 71, 1, 156, 127, 71, 131]]
)

    start = time.time()
    #cbcObj.Encrypt()
    cbcObj.Decrypt()
    end = time.time()

    print(end - start)
    Helpers.saveDecryptedMessageFromBlocks(cbcObj.encryptedBlocksArray, "Lab2/Outputs/CbcEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(cbcObj.decryptedBlocksArray, "Lab2/Outputs/CbcDecrypted.txt", False)

    pbcObj = pbc.PBCCipher(enc = [[80, 60, 243, 207, 43, 68, 185, 243, 15, 3, 170, 68, 248, 2, 33, 88], [98, 41, 65, 145, 158, 161, 57, 94, 120, 133, 124, 139, 114, 199, 177, 81], [173, 179, 4, 79, 73, 218, 151, 89, 114, 126, 186, 178, 226, 251, 131, 37], [132, 146, 164, 98, 131, 39, 42, 68, 192, 153, 190, 123, 202, 162, 24, 115], [253, 116, 207, 57, 36, 16, 87, 111, 76, 19, 226, 180, 231, 3, 102, 37]]
)

    start = time.time()
    #pbcObj.Encrypt()
    pbcObj.Decrypt()
    end = time.time()

    print(end - start)
    Helpers.saveDecryptedMessageFromBlocks(pbcObj.encryptedBlocksArray, "Lab2/Outputs/PbcEncrypted.txt")
    Helpers.saveDecryptedMessageFromBlocks(pbcObj.decryptedBlocksArray, "Lab2/Outputs/PbcDecrypted.txt", False)

def Lab3():

    rsaObj = rsa.RSA(signature = "ErykTaszarek")
    rsaObj.Encrypt()
    rsaObj.Decrypt()

if __name__ == '__main__':
    #Lab1(bbs)

    Lab2()

    #Lab3()
