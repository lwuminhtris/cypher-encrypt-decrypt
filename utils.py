# Luu Minh Tri, 20/11/2021
# UTILS.PY - helper file for EXEC.PY

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


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