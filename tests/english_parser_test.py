# -*- coding:utf-8 -*-
import nose
import unittest
from mobileclick.nlp import EnglishParser

class EnglishParserTestCase(unittest.TestCase):

    def setUp(self):
        self.ep = EnglishParser()
        self.txt = "At 8 o'clock on Thursday morning Arthur didn't feel very good."

    def test_english_parser_pos_tokenize(self):
        '''
        EnglishParser.pos_tokenize
        '''
        result = self.ep.pos_tokenize(self.txt)
        self.assertEqual(result[0], ('At', 'IN'))

    def test_english_parser_stopword_filter(self):
        '''
        EnglishParser.stopword_filter
        '''
        result = self.ep.stopword_filter(self.ep.pos_tokenize(self.txt),
            lambda x: x[0])
        self.assertEqual(result[0], ('At', 'IN'))

    def test_english_parser_noun_filter(self):
        '''
        EnglishParser.noun_filter
        '''
        result = self.ep.noun_filter(self.ep.pos_tokenize(self.txt))
        print result
        self.assertEqual(result[0], ("o'clock", 'NN'))

    def test_english_parser_noun_tokenize(self):
        '''
        EnglishParser.noun_parse
        '''
        result = self.ep.noun_tokenize(self.txt)
        self.assertEqual(result[0], "o'clock")

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
