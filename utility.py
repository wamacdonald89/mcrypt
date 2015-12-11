from math import log10
import binascii

def hex2b64(h):
    return binascii.b2a_base64(hex2bin(h))

def str2bin(s):
    return [ord(x, 'bin') for x in s]

def str2hex(s):
    return s.encode('hex')

def hex2str(h):
    return h.decode('hex')

def bin2hex(b):
    return hex2str(bin2str(b))

def hex2bin(h):
    return str2bin(hex2str(h))

def xor(buffer1, buffer2):
    return "".join(["%x" % (int(x,16) ^ int(y,16)) for (x, y) in zip(buffer1, buffer2)])

def repeat_key(key, length):
    return ''.join([key[i % len(key)] for i in range(0, length)])

def normalize(text):
    return ''.join([x for x in text if x.isalpha()]).upper()

def score_fitness(texts, ngram_file='english_quadgrams.txt'):
    if type(texts) is str:
        texts = [texts]
    ngrams = {}
    for line in open(ngram_file):
        key, count = line.split(' ')
        ngrams[key] = int(count)
    L = len(key)
    N = sum(ngrams.itervalues())
    for key in ngrams.keys():
        ngrams[key] = log10(float(ngrams[key]) / N)
    fl = log10(0.01 / N)
    scores = []
    for text in texts:
        score = 0
        for i in xrange(len(text) - L + 1):
            if text[i:i + L] in ngrams:
                score += ngrams[text[i:i + L]]
            else:
                score += fl
        scores.append(score)
    return scores
