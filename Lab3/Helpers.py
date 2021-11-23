import random
from math import gcd as bltin_gcd
from textwrap import wrap

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

def isCoprime(a, b):
    return bltin_gcd(a, b) == 1

def getE(phi):
    possiblyNumber = random.randint(3, phi)
    while not isPrime(possiblyNumber) and not isCoprime(possiblyNumber, phi):
        possiblyNumber = random.randint(3, phi)
    return possiblyNumber

def getD(e,phi):
    possiblyNumber = 3
    while (e*possiblyNumber % phi) != 1 and possiblyNumber<phi:
        possiblyNumber = random.randint(3, phi)

    return possiblyNumber if possiblyNumber < phi else getD(e,phi)

def digitsSave(a, isEncrypt = True):
    if(isEncrypt):
        ret = a+254
    else:
        ret = a-254
    return ret

def saveArrayToFile(array, filePath, isDecrypted = False):
    f = open(filePath, "a")
    f.truncate(0)
    print(array)
    for char in array:
        f.write(chr(int(char))) if isDecrypted else f.write(str(char))
    f.close()

def readInput(path):
    with open(path) as f:
        content = f.readlines()
    return str(content[0])

def getRandomPrimeNumber():
    primes = [i for i in range(1000, 9999) if isPrime(i)]
    propabblyPrime = random.choice(primes)
    print(propabblyPrime)
    return propabblyPrime