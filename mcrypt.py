#Crypto Challenges
import binascii
import argparse
#utility

def hex2b64(h):
    return binascii.b2a_base64(hex2bin(h))

def str2bin(s):
    return [ord(x, 'bin') for x in s]

def bin2str(b):
    return ''.join(chr(x) for x in b)

def str2hex(s):
    return s.encode('hex')

def hex2str(h):
    return h.decode('hex')

def bin2hex(b):
    return hex2str(bin2str(b))

def hex2bin(h):
    return str2bin(hex2str(h))


