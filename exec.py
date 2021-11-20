# Luu Minh Tri, 20/11/2021
# PROC.PY - handling logic for application
from utils import uppercase, lowercase, index, isEven

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

    # def caesarDecode(text: str, key: int) -> str:
    #     result = ''
    #     for letter in text:
    #         if letter in uppercase:
    #             result = result + uppercase[(index('upper', letter) - key) % 26]
    #         elif letter in lowercase:
    #             result = result + lowercase[(index('lower', letter) - key) % 26]
    #     return result

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

    # def railfenceDecode(text: str, key: int) -> str:
    #     pass

    def jointEncode(self, text: str, cKey, rKey):
        return self.railfenceEncode(self.caesarEncode(text, cKey), rKey)

    def decrypt(self, text: str):
        pass