import string
alpha = string.ascii_uppercase + " "
r_alpha = string.ascii_uppercase[::-1] + " "

def encrypt(plaintext):
    plaintext = plaintext.upper()
    return ''.join([r_alpha[alpha.index(x)] for x in plaintext])

def decrypt(cipher):
    return ''.join([alpha[r_alpha.index(x)] for x in cipher])
