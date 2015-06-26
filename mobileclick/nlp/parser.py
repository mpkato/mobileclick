# -*- coding: utf-8 -*-

class Parser(object):
    '''
    Base class for parsers
    '''

    def noun_tokenize(self, sentence):
        '''
        Extract only nouns
        '''
        tagged_tokens = self.pos_tokenize(sentence)
        nouns = self.noun_filter(tagged_tokens)
        nouns = self.stopword_filter(nouns, key=lambda x: x[0])
        nouns = self.normalize(nouns, key=lambda x: x[0])
        return nouns

    def normalize(self, tokens, key=lambda x: x):
        '''
        Convert tokens to lowercase
        '''
        return [key(token).lower() for token in tokens]
