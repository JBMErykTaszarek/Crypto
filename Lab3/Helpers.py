import random
from math import gcd as bltin_gcd
from textwrap import wrap

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

def isCoprime(a, b):
    return bltin_gcd(a, b) == 1

#def getE(phi):
