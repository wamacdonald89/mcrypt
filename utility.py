from math import log10

def score_fitness(texts, ngram_file):
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
