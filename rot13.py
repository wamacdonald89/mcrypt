#ROT13 Shifts the alphabet by 13 characters
import string
def encrypt(plaintext):
    return ''.join([chr(((ord(x) - 97 + 13) % 26) + 97) if x in string.ascii_lowercase else chr(((ord(x) - 65 + 13) % 26) + 65) if x in string.ascii_uppercase else x for x in plaintext])

def decrypt(cipher):
    return encrypt(cipher)
