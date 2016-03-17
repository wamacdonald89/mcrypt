#alphabetic-substitution-cipher

import string
from utility import normalize

def encrypt(key, str_input):
    alphabet = string.ascii_uppercase
    str_input = normalize(str_input)
    returnlist = []
    for i, c in enumerate(str_input):
        for j, d in enumerate(alphabet):
            if(c == d):
                returnlist.append(key[j])
    return ''.join(returnlist).upper()

def decrypt(key, str_input):
    alphabet = string.ascii_uppercase
    str_input = normalize(str_input)
    returnlist = []
    for i, c in enumerate(str_input):
        for j, d in enumerate(key.upper()):
            if(c == d):
                returnlist.append(alphabet[j])
    return ''.join(returnlist).upper()
                

