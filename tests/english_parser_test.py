# -*- coding:utf-8 -*-
import nose
import unittest
from mobileclick.nlp import EnglishParser

class MethodTestCase(unittest.TestCase):

    def setUp(self):
        self.ep = EnglishParser()
        self.txt = "At 8 o'clock on Thursday morning Arthur didn't feel very good."

    def test_english_parser_parse(self):
        '''
        EnglishParser.parse
        '''
        result = self.ep.parse(self.txt)
        self.assertEqual(result[0], ('At', 'IN'))


if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
