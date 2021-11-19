import random
from math import gcd as bltin_gcd
import Constants as constants

def isCoprime(a, b): #metoda sprawdzająca czy dwie liczby są względnie pierwsze
    return bltin_gcd(a, b) == 1

def setNewSeed(self): #metoda generująca nowy seed
    newSeed = random.randint(2, self.modulus - 1)
    while not isCoprime(newSeed, self.modulus):
        newSeed = random.randint(2, self.modulus - 1)
    return newSeed

class BlumBlumShub(object):
    def __init__(self, a=None):
        self.modulus = constants.firstBlumNumber * constants.secondBlumNumber #inicjalizowanie iloczynu dwóch liczb bluma
        self.state = a if a is not None else setNewSeed(self)
        self.state = (self.state ** 2) % self.modulus

    def bitstream(self): #metoda służąca do obliczenia zaszyfrowanych bitów
        while True:
            yield self.state % 2
            self.state = pow(self.state, 2, self.modulus)

    def bits(self, length): #metoda służąca do zwrócenia zaszyfrowanego ciągu
        outputBits = ''
        for bit in self.bitstream():
            outputBits += str(bit)
            if len(outputBits) == length:
                break

        return outputBits