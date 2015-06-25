# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Query

class QueryTestCase(unittest.TestCase):
    def test_query_read(self):
        '''
        Query.read
        '''
        queries = Query.read('./data/MC2-training/en/1C2-E-queries.tsv')
        self.assertEqual(queries[0].qid, '1C2-E-0001')
        self.assertEqual(queries[0].body, 'michael jackson death')
        self.assertEqual(len(queries), 100)

    def test_query_load(self):
        '''
        Query.load
        '''
        query = Query.load(('1', '2',))
        self.assertEqual(query.qid, '1')
        self.assertRaises(Exception, Query.load, ('1',))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

