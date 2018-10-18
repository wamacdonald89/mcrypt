# Substitute plaintext characters with a different character
# from a cipher alphabet
# ----------------------------------------------------------
# Example: 
# cipher alphabet:  phqgiumeaylnofdxjkrcvstzwb
# plaintext:        defend the east wall of the castle
# ciphertext:       giuifg cei iprc tpnn du cei qprcni

from utility import normalize, score_fitness
import random, string, sys
def encrypt(plaintext, alphabet):
    return normalize(plaintext).translate(str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', normalize(alphabet)))

# Decrypt with known alphabet or make best guess
# Cipher = ciphertext
# alphabet => optional decryption alphabet
# norm => normalize the text. Set to False for human readable.
def decrypt(cipher, alphabet=None, norm=True):
    # Pick swap two letters at random and check the fitness
    # of the decrypted text. If after 1000 iterations, no
    # improvement of fitness has occurred, decrypt the plaintetxx
    # with the current cipher alphabet.
    if alphabet == None:
        parent = random.sample(list(string.ascii_uppercase), 26)
        max_score = score_fitness(decrypt(cipher, parent))
        i = 0

        # Create space
        print("")
        print("")
        print("")
        print("")

        while i < 999:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parent[:]
            child[a],child[b] = child[b],child[a]
            score = score_fitness(decrypt(cipher, child))
            if score > max_score:
                max_score = score
                parent = child
                i = 0
            i = i + 1

            # Bring cursor up 5 lines
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[F")

            print("Current Cipher Alphabet:    " + ''.join(child) + "      ")
            print("Current Decryption Attempt: " + decrypt(cipher, child)[:40])
            print("Best Cipher Alphabet:       " + ''.join(parent))
            print("Best Decryption Attempt:    " + decrypt(cipher, parent)[:40])
            print("Confidence Level: " + str(i) + "/1000   ")

        print("Local maximum found with: " + ''.join(parent))
        return decrypt(cipher, parent, false)
    else:
        if norm == True:
            return normalize(cipher).translate(str.maketrans(normalize(alphabet), string.ascii_uppercase))
        else:
            return cipher.translate(str.maketrans(alphabet.upper() + alphabet.lower(), string.ascii_uppercase + string.ascii_lowercase))
