# -*- coding: utf-8 -*-
import MeCab
from .parser import Parser

class JapaneseParser(Parser):
    def __init__(self):
        self.tagger = MeCab.Tagger()

    def word_tokenize(self, sentence):
        '''
        Word tokenization
        '''
        tokens = [w[0] for w in self._mecab_tokenize(sentence)]
        tokens = self.stopword_filter(tokens)
        tokens = self.normalize(tokens)
        return tokens

    def pos_tokenize(self, sentence):
        '''
        Parse sentences and output pos-tagged tokens.
        '''
        return self._mecab_tokenize(sentence)

    def stopword_filter(self, tokens, key=lambda x: x):
        '''
        Filter out stopword tokens (Not implemented)
        '''
        return tokens

    def noun_filter(self, tokens):
        '''
        Filter out non-noun tokens (pos starts with 名詞)
        '''
        return [token for token in tokens
            if token[1].startswith('名詞')]

    def _mecab_tokenize(self, sentence):
        '''
        Sentence tokenization
        '''
        if isinstance(sentence, unicode):
            # assume utf-8
            sentence = sentence.encode('utf-8')
        node = self.tagger.parseToNode(sentence)
        result = []
        while node:
            result.append((node.surface, node.feature))
            node = node.next
        return result
