#Ceaser Shifts the alphabet by X characters
def encrypt(plaintext, shift):                                                     return ''.join([chr(((ord(x)-65+shift) % 26) + 65) for x in plaintext.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

#decrypt with known shift length
def decrypt(cipher, shift=None):
    if shift == None:
        for i in range(0, 25):
            print decrypt(cipher, i)
    else:
        return ''.join([chr(((ord(x)-65-shift) % 26) + 65) for x in cipher.upper() if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])

