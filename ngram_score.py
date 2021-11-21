# Luu Minh Tri, 20/11/2021
# NGRAM_SCORE.PY -- scoring of text using n-gram probabilities
# References: http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/

from math import log10

class ngram_score(object):
    def __init__(self, ngramfile='./quadgrams.txt', sep=' '):
        self.ngrams = {}
        for line in open(ngramfile, 'r'):
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        # calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        self.floor = log10(0.01 / self.N)

    def score(self, raw_text):
        ''' compute the score of text '''
        text = raw_text.upper()
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngrams:
                score += ngrams(text[i:i + self.L])
            else:
                score += self.floor
        return score