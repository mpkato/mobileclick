# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Measurable

class MeasurableTestCase(unittest.TestCase):
    def test_measurable_length(self):
        '''
        Measurable.length
        '''
        m = Measurable()
        m.body = "(*[I'm a student!!?]*)"
        self.assertEqual(m.len, 10)
        m.body = "Ａ：「今日」は 『良い』　天気です！？"
        self.assertEqual(m.len, 10)

    """
    def test_measurable_length_in_practice(self):
        '''
        Output all the length of iUnits and intents
        '''
        from mobileclick import Iunit
        import os
        filenames = [
            './data/MC2-test/en/MC2-E-iunits.tsv',
            './data/MC2-test/ja/MC2-J-iunits.tsv',
            './data/MC2-test/en/MC2-E-intents.tsv',
            './data/MC2-test/ja/MC2-J-intents.tsv',
            ]
        for filename in filenames:
            iunits = Iunit.read(filename)
            output_filename = './len-%s' % os.path.basename(filename)
            with open(output_filename, 'w') as f:
                for iunit in iunits:
                    f.write('\t'.join((iunit.qid, iunit.uid, str(iunit.len))) + '\n')
    """

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
