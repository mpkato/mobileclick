# -*- coding:utf-8 -*-
import nose
import os
import xml.etree.ElementTree as ET
from mobileclick.methods import RandomSummarizationMethod
from .summarization_method_test import SummarizationMethodTestCase

class RandomSummarizationMethodTestCase(SummarizationMethodTestCase):
    def test_generate_run(self):
        '''
        RandomSummarizationMethod.generate_run
        '''
        filepath = './tmp/test.xml'

        for lang in ['E', 'J']:
            method = RandomSummarizationMethod()
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

