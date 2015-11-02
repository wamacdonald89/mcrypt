#The Atbash cipher swaps the first letter of an alphabet with the last,
#the second letter with the second-to-last etc.
def encrypt(plaintext):
    return ''.join([chr(65 + (90 - ord(x))) for x in plaintext.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

def decrypt(cipher):
    return encrypt(cipher)
