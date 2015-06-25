# -*- coding:utf-8 -*-
import unittest
import nose
import re
import os
from mobileclick import IndexFactory

class IndexFactoryTestCase(unittest.TestCase):

    def setUp(self):
        indexdir = './data/MC2-training-documents/1C2-E.INDX/'
        webpagedir = './data/MC2-training-documents/1C2-E.HTML/'
        self.factory = IndexFactory(indexdir, webpagedir)
        self.indices = self.factory.read('1C2-E-0001')

    def test_index_factory_read(self):
        '''
        IndexFactory.read
        '''
        self.assertEqual(self.indices[0].rank, 1)
        self.assertEqual(self.indices[0].filepath, 
            os.path.join(
                os.path.abspath(self.factory.webpagedir), '1C2-E-0001-1.html')
            )
        self.assertEqual(self.indices[0].title, 'Death of Michael Jackson')
        self.assertEqual(self.indices[0].url, 'http://en.wikipedia.org/wiki/Death_of_Michael_Jackson')
        body = '''American singer Michael
        Jackson died on June 25, 2009 of propofol intoxication after suffering
        a respiratory arrest at his home on North Carolwood Drive in the Holmby
        ...'''
        body = ' '.join(re.split(r'\s*', body))
        self.assertEqual(self.indices[0].body, body)
        self.assertEqual(len(self.indices), 213)

    def test_index_rank_is_int(self):
        '''
        Index.rank must be integer
        '''
        self.assertIsInstance(self.indices[0].rank, int)

    def test_load_index(self):
        '''
        Index.load
        '''
        index = self.factory._load_index('1C2-E-0002', ('1', '2', '3', '4', '5'))
        self.assertEqual(index.qid, '1C2-E-0002')
        self.assertRaises(Exception, self.factory._load_index, '', ('1', '2', '3', '4'))

    def test_load_index_not_int_exception(self):
        '''
        Index.load raises an exception when the first value is not int
        '''
        self.assertRaises(ValueError, self.factory._load_index, '', ('x', '2', '3', '4', '5'))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
