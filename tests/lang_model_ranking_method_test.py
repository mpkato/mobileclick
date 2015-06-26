# -*- coding:utf-8 -*-
import nose
import os
from mobileclick.methods import LangModelRankingMethod
from mobileclick.nlp import EnglishParser, JapaneseParser
from .method_test import MethodTestCase

class LangModelRankingMethodTestCase(MethodTestCase):
    def test_english_generate_run(self):
        '''
        LangModelRankingMethod.generate_run (English)
        '''
        self._generate_run('E', EnglishParser())

    def test_japanese_generate_run(self):
        '''
        LangModelRankingMethod.generate_run (Japanese)
        '''
        self._generate_run('J', JapaneseParser())

    def _generate_run(self, lang, parser):
        '''
        Helper method for LangModelRankingMethod
        '''
        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')
        method = LangModelRankingMethod(parser)
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

