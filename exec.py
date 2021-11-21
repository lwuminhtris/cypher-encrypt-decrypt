# Luu Minh Tri, 20/11/2021
# PROC.PY -- handling logic for application
from utils import uppercase, lowercase, index, isEven, chiSquareCalc, generateFreqDict
import ngram_score as ns
from string import ascii_lowercase 

class Exec: 
    def __init__(self):
        pass

    def caesarEncode(text: str, key: int) -> str:
        result = ''
        for letter in text:
            if letter in uppercase:
                result = result + uppercase[(index('upper', letter) + key) % 26]
            elif letter in lowercase:
                result = result + lowercase[(index('lower', letter) + key) % 26]
        return result

    def railfenceEncode(text: str, key: int) -> str:
        listResult = ['']*key
        for index in range(0, len(text)):
            if index % (key - 1) == 0 and isEven(index /(key - 1)):
                listResult[0] += text[index]
            elif index % (key - 1) == 0 and isEven(index /(key - 1)) == False:
                listResult[key - 1] += text[index]
            elif index % (key - 1) != 0 and isEven(round(index / (key - 1) - 0.5)):
                listResult[index % (key - 1)] += text[index]
            elif index % (key - 1) != 0 and isEven(round(index / (key - 1) - 0.5)) == False:
                listResult[key - 1 - index % (key - 1)] += text[index]
        return ''.join(listResult)

    def railfenceDecode(text: str, key: int) -> str:
        if key == 1:
            return text
        ci = 0
        tLen = len(text)
        plainMsg = [""] * tLen
        for i in range(1, key + 1):
            flag = True
            pi = i - 1
            while pi < tLen:
                plainMsg[pi] = text[ci]
                ci += 1
                if i == 1 or i == key:
                    pi += (key - 1) * 2
                else:
                    if flag:
                        pi += (key - i) * 2
                        flag = False
                    else:
                        pi += 2 * (i - 1)
                        flag = True

        return "".join(plainMsg)




    def jointEncode(text: str, cKey: int, rKey: int):
        return Exec.railfenceEncode(Exec.caesarEncode(text, cKey), rKey)

    def decrypt(text: str):
        # generate frequency dict for each letter in text
        freq = generateFreqDict(text)
        # set minimum score as cypher text score
        minChi = chiSquareCalc(freq)
        # caesar brute force
        cKey = 0
        for key in range(1, 26):
            # generate frequency dict for each 
            tempFreq = generateFreqDict(Exec.caesarEncode(text, -key))
            tempChi = chiSquareCalc(tempFreq)
            if tempChi < minChi:
                minChi = tempChi
                cKey = key
        cDecryptedMsg = Exec.caesarEncode(text, -cKey)

        # rail fence brute force
        # get score of cDecryptedMsg
        maxNgram = ns.ngram_score().score(cDecryptedMsg)
        rKey = 1
        for key in range(2, len(cDecryptedMsg)):
            tempMsg = Exec.railfenceDecode(cDecryptedMsg, key)
            tempNgram = ns.ngram_score().score(tempMsg)
            # if tempNgram bigger then set new rKey value
            if tempNgram > maxNgram:
                maxNgram = tempNgram
                rKey = key
        plainMsg = Exec.railfenceDecode(cDecryptedMsg, rKey)

        return cKey, rKey, plainMsg
        