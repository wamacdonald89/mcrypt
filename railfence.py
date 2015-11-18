from utility import normalize, score_fitness
from itertools import cycle

def encrypt(plaintext,n):
    plaintext = normalize(plaintext)
    count = cycle(range(0,n) + range(1,n-1)[::-1])
    rails = [''] * n
    for i in plaintext:
        index = count.next()
        rails[index] = rails[index] + i
    return ''.join(rails)

def decrypt(cipher,n=None):
    if n == None:
        ciphers = []
        for i in range(1, len(cipher)):
            ciphers.append(decrypt(cipher, i))
        scores = score_fitness(ciphers)
        return ciphers[scores.index(max(scores))]
    else:
        cipherlen = len(cipher)
        parts = [''] * n
        count = cycle(range(0,n) + range(1,n-1)[::-1])
        for i in cipher:
            index = count.next()
            parts[index] += 'x'
        for i in range(0,n):
            parts[i] = cipher[:len(parts[i])]
            cipher = cipher[len(parts[i]):]
        count = cycle(range(0,n) + range(1,n-1)[::-1])
        plaintext = ''
        for i in range(0, cipherlen):
            index = count.next()
            plaintext += parts[index][0]
            parts[index] = parts[index][1:]
        return plaintext
