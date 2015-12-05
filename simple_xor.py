from utility import xor, repeat_key, str2hex

def encrypt(plaintext, key):
    key = repeat_key(key, len(plaintext))
    return xor(str2hex(plaintext), str2hex(key))

def decrypt(cipher, key):
    return plaintext
