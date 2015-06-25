# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick.iunit import Iunit

class IunitTestCase(unittest.TestCase):
    def test_iunit_read(self):
        '''
        Iunit.read
        '''
        iunits = Iunit.read('./data/MC2-training/en/1C2-E-iunits.tsv')
        self.assertEqual(iunits[0].qid, '1C2-E-0001')
        self.assertEqual(iunits[0].uid, '1C2-E-0001-0001')
        self.assertEqual(iunits[0].body, 'family concerned about murray role')
        self.assertEqual(len(iunits), 4342)

    def test_iunit_load(self):
        '''
        Iunit.load
        '''
        iunit = Iunit.load(('1', '2', '3'))
        self.assertEqual(iunit.qid, '1')
        self.assertRaises(Exception, Iunit.load, ('1', '2', '3', '4'))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

