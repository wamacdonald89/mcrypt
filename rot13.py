import string
alpha = string.ascii_uppercase + ' '
r13_alpha = "NOPQRSTUVWXYZABCDEFGHIJKLM "

def encrypt(plaintext):                                                     
    plaintext = plaintext.upper()
    return ''.join([r13_alpha[alpha.index(x)] for x in plaintext])
def decrypt(cipher):
    cipher = cipher.upper()
    return ''.join([alpha[r13_alpha.index(x)] for x in cipher])
