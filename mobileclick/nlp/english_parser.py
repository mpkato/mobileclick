# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import stopwords

class EnglishParser(object):
    def parse(self, sentence):
        '''
        Parse sentences and output pos-tagged tokens.
        '''
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)
        return tagged_tokens

    def noun_parse(self, sentence):
        '''
        Extract only nouns
        '''
        tagged_tokens = self.parse(sentence)
        nouns = self.noun_filter(tagged_tokens)
        nouns = self.stopword_filter(nouns, key=lambda x: x[0])
        nouns = self.normalize(nouns, key=lambda x: x[0])
        return nouns

    def stopword_filter(self, tokens, key=lambda x: x):
        '''
        Filter out stopword tokens
        '''
        return [token for token in tokens
            if not key(token) in stopwords.words("english")]

    def noun_filter(self, tokens):
        '''
        Filter out non-noun tokens (pos starts with N)
        '''
        return [token for token in tokens
            if token[1].startswith('N')]

    def normalize(self, tokens, key=lambda x: x):
        '''
        Convert tokens to lowercase
        '''
        return [key(token).lower() for token in tokens]

if __name__ == '__main__':
    ep = EnglishParser()
    tokens = ep.parse("At 8 o'clock on Thursday morning Arthur didn't feel very good.")
    stopped = ep.stopword_filter(tokens, key=lambda x: x[0])
    nouns = ep.noun_filter(stopped)
