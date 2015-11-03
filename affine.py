#Used for default settings
import random
from utility import score_fitness

def encrypt(plaintext,a=None,b=None):
    if a==None or b == None:
        print 'Some arguments missing. Selecting random...' 
    if a==None: 
        a=random.choice([1,3,5,7,11,13,17,19,23])
        print 'Using a= '+str(a)
    if b==None: 
        b=random.choice(range(1,25))
        print 'Using b= ' + str(b)
    return ''.join([chr( ( (a * ord(x) - 65 + b) % 26) + 65) for x in plaintext.upper() if x.isalpha()])

def decrypt(cipher, a=None, b=None):
    #if unknown a and b, make best guess. More accurate with
    #longer cipher texts
    if a==None or b==None:
        canidates = []
        for i in [1,3,5,7,11,13,17,19,23]:
            for j in range(1,25):
                canidates.append(decrypt(cipher,i,j))
        scores = score_fitness(canidates)
        return canidates[scores.index(max(scores))]
    else:
        a_i = 0
        for i in range(1,25):
            if (a * i) % 26 == 1:
                a_i = i
                break
        return ''.join([chr( ( (a_i * (ord(x) - 65 - b) % 26) + 65) ) for x in cipher.upper() if x.isalpha()])
