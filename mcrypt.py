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

#Challenges

#Challenge 1

def challenge1():
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print "Challenge #1"
    print "_" * 20
    print "[+] Converting hex value: " +input +" to Base64"
    output = hex2b64(input)
    print "[+] Base64 Value: " + output
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Montasano Crypto Challenges')
    parser.add_argument("challenge", help="The name of the challenge to run")
    args = parser.parse_args()
    if args.challenge == "1":
        print hex2bin('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')    
        #challenge1()


