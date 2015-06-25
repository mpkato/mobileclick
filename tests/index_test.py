# -*- coding:utf-8 -*-
import unittest
import nose
import re
from mobileclick.index import Index

class IndexTestCase(unittest.TestCase):

    def setUp(self):
        self.indices = Index.read('./data/MC2-training-documents/1C2-E.INDX/1C2-E-0001-index.tsv')

    def test_index_read(self):
        '''
        Index.read
        '''
        self.assertEqual(self.indices[0].rank, 1)
        self.assertEqual(self.indices[0].filename, '1C2-E-0001-1.html')
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

    def test_index_load(self):
        '''
        Index.load
        '''
        index = Index.load(('1', '2', '3', '4', '5'))
        self.assertEqual(index.filename, '2')
        self.assertRaises(Exception, Index.load, ('1', '2', '3', '4'))

    def test_index_load_not_int_exception(self):
        '''
        Index.load raises an exception when the first value is not int
        '''
        self.assertRaises(ValueError, Index.load, ('x', '2', '3', '4', '5'))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])


