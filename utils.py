# Luu Minh Tri, 20/11/2021
# UTILS.PY - helper file for EXEC.PY

from math import pow
from string import ascii_lowercase

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

freqEng = {
    'a': 8.167 / 100,
    'b': 1.492 / 100,
    'c': 2.782 / 100,
    'd': 4.253 / 100,
    'e': 12.702 / 100,
    'f': 2.228 / 100,
    'g': 2.205 / 100,
    'h': 6.094 / 100,
    'i': 6.966 / 100,
    'j': 0.153 / 100,
    'k': 0.772 / 100,
    'l': 4.025 / 100,
    'm': 2.406 / 100,
    'n': 6.749 / 100,
    'o': 7.507 / 100,
    'p': 1.929 / 100,
    'q': 0.095 / 100,
    'r': 5.987 / 100,
    's': 6.327 / 100,
    't': 9.056 / 100,
    'u': 2.758 / 100,
    'v': 0.978 / 100,
    'w': 2.360 / 100,
    'x': 0.150 / 100,
    'y': 1.974 / 100,
    'z': 0.074 / 100
}

def index(type: str, letter: str) -> int:
    if type == 'upper':
        return uppercase.index(letter)
    elif type == 'lower':
        return lowercase.index(letter)
    else:
        return 'undetected type'


def isEven(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

def generateFreqDict(text: str) -> dict:
    freq: float = {}
    totalOcur = 0
    for letter in ascii_lowercase:
        # number of appearances
        freq[letter] = text.count(letter) + text.count(letter.upper())
        totalOcur += freq[letter]
    for letter in ascii_lowercase:
        # frequency of each letter
        freq[letter] /= totalOcur
    return freq
    
# calculate chi square sum of a text
def chiSquareCalc(freq: dict) -> int: 
    sum = 0
    for letter in ascii_lowercase:
        sum += pow((freq[letter] - freqEng[letter]), 2)/ (freqEng[letter])
    return sum

def standarnizedInput(text: str) -> str:
    pass