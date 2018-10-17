from utility import score_fitness
import string

#Ceaser Shifts the alphabet by X characters
def encrypt(plaintext, shift):
    return ''.join([chr(((ord(x) - 97 + int(shift)) % 26) + 97) if x in string.ascii_lowercase else chr(((ord(x) - 65 + 13) % 26) + 65) if x in string.ascii_uppercase else x for x in plaintext])

#decrypt with known or unknown shift length
def decrypt(cipher, shift=None):
    ciphers = []
    if shift == None:
        for i in range(0, 26):
            ciphers.append(decrypt(cipher, i))
        scores = score_fitness(ciphers)
        return ciphers[scores.index(max(scores))]
    else:
        return encrypt(cipher, -1 * int(shift)) 
