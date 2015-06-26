# -*- coding: utf-8 -*-
import MeCab

class JapaneseParser(object):
    def __init__(self):
        self.tagger = MeCab.Tagger()

    def word_tokenize(self, sentence):
        '''
        Word tokenization
        '''
        tokens = [w[0] for w in self.pos_tokenize(sentence)]
        tokens = self.stopword_filter(tokens)
        tokens = self.normalize(tokens)
        return tokens

    def pos_tokenize(self, sentence):
        '''
        Parse sentences and output pos-tagged tokens.
        '''
        return self._mecab_tokenize(sentence)

    def noun_tokenize(self, sentence):
        '''
        Extract only nouns
        '''
        tagged_tokens = self.pos_tokenize(sentence)
        nouns = self.noun_filter(tagged_tokens)
        nouns = self.stopword_filter(nouns, key=lambda x: x[0])
        nouns = self.normalize(nouns, key=lambda x: x[0])
        return nouns

    def _mecab_tokenize(self, sentence):
        '''
        Tokenization by MeCab
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

    def normalize(self, tokens, key=lambda x: x):
        '''
        Convert tokens to lowercase
        '''
        return [key(token).lower() for token in tokens]