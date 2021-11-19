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

def saveDecryptedMessageFromBlocks(blocks, filePath):
    f = open(filePath, "a", encoding="utf-8")
    f.truncate(0)
    print(blocks)
    for block in blocks:
        returnString = ""
        for char in block:
            returnString+= chr(char)
        f.write(returnString + "\n")
