# -*- coding: utf-8 -*-
import nltk

class EnglishParser(object):
    def parse(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        tagged_tokens = nltk.pos_tag(tokens)
        return tagged_tokens


if __name__ == '__main__':
    ep = EnglishParser()
    ep.parse("At 8 o'clock on Thursday morning Arthur didn't feel very good.")
