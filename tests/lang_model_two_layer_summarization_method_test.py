# -*- coding:utf-8 -*-
import nose
import os
import xml.etree.ElementTree as ET
from mobileclick.nlp import EnglishParser, JapaneseParser
from mobileclick.methods import LangModelTwoLayerSummarizationMethod
from .summarization_method_test import SummarizationMethodTestCase

class LangModelTwoLayerSummarizationMethodTestCase(SummarizationMethodTestCase):

    def test_english_generate_run(self):
        '''
        LangModelTwoLayerSummarizationMethod.generate_run (English)
        '''
        self._generate_run('E', EnglishParser())

    def test_japanese_generate_run(self):
        '''
        LangModelTwoLayerSummarizationMethod.generate_run (Japanese)
        '''
        self._generate_run('J', JapaneseParser())

    def _generate_run(self, lang, parser):
        '''
        Helper method for LangModelTwoLayerSummarizationMethod
        '''
        filepath = './tmp/test.xml'

        length_limit = 420 if lang == 'E' else 280

        method = LangModelTwoLayerSummarizationMethod(parser, length_limit)
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

            # all the intents must appear
            for intent in task.intents:
                self.assertIsNotNone(
                    root.find("result[@qid='%s']/first/link[@iid='%s']" % (
                        task.query.qid, intent.iid)))
            # iUnits in the first layer must not appear in the second layer
            for iunitnode in root.findall(
                "result[@qid='%s']/first/iunit" % task.query.qid):
                self.assertIsNone(
                    root.find("result[@qid='%s']/second/iunit[@uid='%s']" % (
                        task.query.qid, iunitnode.attrib['uid'])))
            # The second layer for 1C2-E-0002-INTENT0005 must contains
            # different iUnits from the others in 1C2-E-0002
            qid = '1C2-E-0002'
            if task.query.qid == qid:
                iunitnodes = root.findall(
                    "result[@qid='%s']/second[@iid='%s-INTENT0001']/iunit" % (
                    qid, qid))
                uids = set([node.attrib['uid'] for node in iunitnodes])
                albumnodes = root.findall(
                    "result[@qid='%s']/second[@iid='%s-INTENT0005']/iunit" % (
                    qid, qid))
                albumuids = set([node.attrib['uid'] for node in albumnodes])
                self.assertNotEqual(uids, albumuids)

                # The others are the same
                othernodes = root.findall(
                    "result[@qid='%s']/second[@iid='%s-INTENT0002']/iunit" % (
                    qid, qid))
                otheruids = set([node.attrib['uid'] for node in othernodes])
                self.assertEqual(uids, otheruids)

        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])

