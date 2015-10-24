# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Intent

class IntentTestCase(unittest.TestCase):
    def test_intent_read(self):
        '''
        Intent.read
        '''
        intents = Intent.read('./data/MC2-test/en/MC2-E-intents.tsv')
        self.assertEqual(intents[0].qid, 'MC2-E-0001')
        self.assertEqual(intents[0].iid, 'MC2-E-0001-INTENT0001')
        self.assertEqual(intents[0].body, 'Profile')
        self.assertEqual(len(intents), 448)

    def test_intent_load(self):
        '''
        Intent.load
        '''
        intent = Intent.load(('1', '2', '3'))
        self.assertEqual(intent.qid, '1')
        self.assertRaises(Exception, Intent.load, ('1', '2', '3', '4'))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
