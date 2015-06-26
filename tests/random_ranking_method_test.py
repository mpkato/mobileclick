# -*- coding:utf-8 -*-
import nose
import os
from mobileclick.methods import RandomRankingMethod
from .method_test import MethodTestCase

class RandomRankingMethodTestCase(MethodTestCase):
    def test_generate_run(self):
        '''
        RandomRankingMethod.generate_run
        '''
        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')
        for lang in ['E', 'J']:
            method = RandomRankingMethod()
            run = method.generate_run('test', 'test', self.tasks[lang])
            run.save('./tmp')
            self.assertTrue(os.path.exists('./tmp/test.tsv'))
            lines = self.read_runfile('./tmp/test.tsv')
            self.assertEqual(len(lines),
                sum([len(t.iunits) for t in self.tasks[lang]]) + 1)
            if os.path.exists('./tmp/test.tsv'):
                os.remove('./tmp/test.tsv')

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

