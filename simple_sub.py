from string import maketrans
from utility import normalize

def encrypt(plaintext, key):
    return normalize(plaintext).translate(maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', normalize(key)))

#TODO: Attempt decryption without key
def decrypt(cipher, key):
    return normalize(cipher).translate(maketrans(normalize(key),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
