#!/usb/bin/python3

def encrypt(string, key): 
    ciphertext = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext)) 
      
# This function decrypts the  
# encrypted text and returns  
# the original text 
def decrypt(string, key): 
    plaintext = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        plaintext.append(chr(x)) 
    return("" . join(plaintext)) 
