# -*- coding:utf-8 -*-
import nose
import os
import xml.etree.ElementTree as ET
from mobileclick.nlp import EnglishParser, JapaneseParser
from mobileclick.methods import LangModelSummarizationMethod
from .summarization_method_test import SummarizationMethodTestCase

class LangModelSummarizationMethodTestCase(SummarizationMethodTestCase):

    def test_english_generate_run(self):
        '''
        LangModelSummarizationMethod.generate_run (English)
        '''
        self._generate_run('E', EnglishParser())

    def test_japanese_generate_run(self):
        '''
        LangModelSummarizationMethod.generate_run (Japanese)
        '''
        self._generate_run('J', JapaneseParser())

    def _generate_run(self, lang, parser):
        '''
        Helper method for LangModelSummarizationMethod
        '''
        filepath = './tmp/test.xml'

        method = LangModelSummarizationMethod(parser)
        run = method.generate_run('test', 'test', self.tasks[lang])
        run.save('./tmp')
        self.assertTrue(os.path.exists(filepath))

        tree = ET.parse(filepath)
        root = tree.getroot()
        for task in self.tasks[lang]:
            self.assertIsNotNone(
                root.find("result[@qid='%s']" % task.query.qid))
            self.assertIsNotNone(
                root.find("result[@qid='%s']/first" % task.query.qid))
            for iunit in task.iunits:
                self.assertIsNotNone(
                    root.find("result[@qid='%s']/first/iunit[@uid='%s']" % (
                        task.query.qid, iunit.uid)))
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

