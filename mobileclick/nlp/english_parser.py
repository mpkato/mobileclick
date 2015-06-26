# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import stopwords
from .nlputils import normalize

class EnglishParser(object):
    def __init__(self):
        self.stokenizer = nltk.tokenize.PunktSentenceTokenizer()
        self.wtokenizer = nltk.tokenize.TreebankWordTokenizer()
        self.tagger = nltk.data.load(nltk.tag._POS_TAGGER)

    def word_tokenize(self, sentence):
        '''
        Fastest word tokenization
        '''
        tokens = self._tokenize_sents(sentence)
        tokens = self.stopword_filter(tokens)
        tokens = normalize(tokens)
        return tokens

    def pos_tokenize(self, sentence):
        '''
        Parse sentences and output pos-tagged tokens.
        '''
        tokens = self._tokenize_sents(sentence)
        tagged_tokens = self.tagger.tag(tokens)
        return tagged_tokens

    def noun_tokenize(self, sentence):
        '''
        Extract only nouns
        '''
        tagged_tokens = self.pos_tokenize(sentence)
        nouns = self.noun_filter(tagged_tokens)
        nouns = self.stopword_filter(nouns, key=lambda x: x[0])
        nouns = normalize(nouns, key=lambda x: x[0])
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

    def _tokenize_sents(self, sentence):
        '''
        Sentence tokenization
        '''
        return [token for sent in self.stokenizer.tokenize(sentence)
            for token in self.wtokenizer.tokenize(sent)]
