# -*- coding:utf-8 -*-
import nose
import os
from mobileclick.methods import LangModelRankingMethod
from mobileclick.nlp import EnglishParser
from .method_test import MethodTestCase

class LangModelRankingMethodTestCase(MethodTestCase):
    def test_generate_run(self):
        '''
        RandomRankingMethod.generate_run
        '''
        method = LangModelRankingMethod(EnglishParser())
        run = method.generate_run('test', 'test', self.tasks)
        run.save('./tmp')
        self.assertTrue(os.path.exists('./tmp/test.tsv'))
        lines = self.read_runfile('./tmp/test.tsv')
        self.assertEqual(len(lines),
            sum([len(t.iunits) for t in self.tasks]) + 1)

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

