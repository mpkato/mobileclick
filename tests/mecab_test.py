# -*- coding:utf-8 -*-
import unittest
import nose
import MeCab

class MecabTestCase(unittest.TestCase):
    def test_mecab_parse(self):
        '''
        MeCab.Tagger.parse
        '''
        tagger = MeCab.Tagger()
        node = tagger.parseToNode("今日は晴れです")
        result = []
        while node:
            result.append((node.surface, node.feature))
            node = node.next
        self.assertEqual(result[1][0], '今日')


if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

