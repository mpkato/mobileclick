# -*- coding:utf-8 -*-
import nose
import unittest
from mobileclick.nlp import EnglishParser

class EnglishParserTestCase(unittest.TestCase):

    def setUp(self):
        self.ep = EnglishParser()
        self.txt = "At 8 o'clock on Thursday morning Arthur didn't feel very good."

    def test_english_parser_parse(self):
        '''
        EnglishParser.parse
        '''
        result = self.ep.parse(self.txt)
        self.assertEqual(result[0], ('At', 'IN'))

    def test_english_parser_stopword_filter(self):
        '''
        EnglishParser.stopword_filter
        '''
        result = self.ep.stopword_filter(self.ep.parse(self.txt),
            lambda x: x[0])
        self.assertEqual(result[0], ('At', 'IN'))

    def test_english_parser_noun_filter(self):
        '''
        EnglishParser.noun_filter
        '''
        result = self.ep.noun_filter(self.ep.parse(self.txt))
        self.assertEqual(result[0], ('Thursday', 'NNP'))

    def test_english_parser_normalize(self):
        '''
        EnglishParser.normalize
        '''
        result = self.ep.normalize(self.ep.parse(self.txt),
            lambda x: x[0])
        self.assertEqual(result[0], 'at')

    def test_english_parser_noun_parse(self):
        '''
        EnglishParser.noun_parse
        '''
        result = self.ep.noun_parse(self.txt)
        self.assertEqual(result[0], 'thursday')

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
