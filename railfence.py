from utility import normalize
from itertools import cycle

def encrypt(plaintext,n):
    plaintext = normalize(plaintext)
    count = cycle(range(0,n) + range(1,n-1)[::-1])
    rails = [''] * n
    for i in plaintext:
        index = count.next()
        rails[index] = rails[index] + i
    return ''.join(rails)

def decrypt(cipher,n):
    #TODO
    return cipher
