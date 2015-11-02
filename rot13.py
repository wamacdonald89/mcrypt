#ROT13 Shifts the alphabet by 13 characters
def encrypt(plaintext):                                                     
    return ''.join([chr(((ord(x)-52) % 26) + 65) for x in plaintext.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

def decrypt(cipher):
    return encrypt(cipher)
