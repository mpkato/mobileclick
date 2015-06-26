# -*- coding:utf-8 -*-
import nose
import unittest
from mobileclick.nlp import JapaneseParser

class JapaneseParserTestCase(unittest.TestCase):

    def setUp(self):
        self.ep = JapaneseParser()
        self.txt = "今日は良い天気です"

    def test_japanese_parser_unicode(self):
        '''
        JapaneseParser.pos_tokenize
        '''
        result = self.ep.pos_tokenize(u"今日は良い天気です")
        self.assertEqual(result[1], ('今日',
            '名詞,副詞可能,*,*,*,*,今日,キョウ,キョー'))

    def test_japanese_parser_pos_tokenize(self):
        '''
        JapaneseParser.pos_tokenize
        '''
        result = self.ep.pos_tokenize(self.txt)
        self.assertEqual(result[1], ('今日',
            '名詞,副詞可能,*,*,*,*,今日,キョウ,キョー'))

    def test_japanese_parser_stopword_filter(self):
        '''
        JapaneseParser.stopword_filter
        '''
        result = self.ep.stopword_filter(self.ep.pos_tokenize(self.txt),
            lambda x: x[0])
        self.assertEqual(result[1], ('今日',
            '名詞,副詞可能,*,*,*,*,今日,キョウ,キョー'))

    def test_japanese_parser_noun_filter(self):
        '''
        JapaneseParser.noun_filter
        '''
        result = self.ep.noun_filter(self.ep.pos_tokenize(self.txt))
        self.assertEqual(result[1], ('天気',
            '名詞,一般,*,*,*,*,天気,テンキ,テンキ'))

    def test_japanese_parser_noun_tokenize(self):
        '''
        JapaneseParser.noun_parse
        '''
        result = self.ep.noun_tokenize(self.txt)
        self.assertEqual(result[1], '天気')

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
