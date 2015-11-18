from utility import score_fitness

#Ceaser Shifts the alphabet by X characters
def encrypt(plaintext, shift):                                                     return ''.join([chr(((ord(x)-65+shift) % 26) + 65) for x in plaintext.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

#decrypt with known shift length
def decrypt(cipher, shift=None):
    ciphers = []
    if shift == None:
        for i in range(0, 26):
            ciphers.append(decrypt(cipher, i))
        scores = score_fitness(ciphers)
        return ciphers[scores.index(max(scores))]
    else:
        return ''.join([chr(((ord(x)-65-shift) % 26) + 65) for x in cipher.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

