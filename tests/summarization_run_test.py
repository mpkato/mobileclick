# -*- coding:utf-8 -*-
import nose
import os
import xml.etree.ElementTree as ET
from mobileclick import SummarizationRun, Summary
from .summarization_method_test import SummarizationMethodTestCase

class SummarizationRunTestCase(SummarizationMethodTestCase):

    def test_summarization_run_save_qid(self):
        '''
        SummarizationRun.save (qid test)
        '''
        run = SummarizationRun('ORG-test-1', 'this is a test run')
        for task in self.tasks['E']:
            run.add(task.query.qid, Summary(task.query.qid))
        run.save('./tmp')

        filepath = './tmp/ORG-test-1.xml'
        self.assertTrue(os.path.exists(filepath))
        tree = ET.parse(filepath)
        root = tree.getroot()
        self.assertIsNotNone(root.find('sysdesc'))
        self.assertGreater(len(root.find('sysdesc').text.strip()), 0)
        for task in self.tasks['E']:
            self.assertIsNotNone(
                root.find("result[@qid='%s']" % task.query.qid))

    def test_summarization_run_save_uid_iid(self):
        '''
        SummarizationRun.save (uid and iid test)
        '''
        run = SummarizationRun('ORG-test-1', 'this is a test run')
        for task in self.tasks['J']:
            run.add(task.query.qid, 
                Summary(task.query.qid,
                [task.iunits[0], task.intents[0], task.iunits[1], task.intents[1]],
                {
                    task.intents[0].iid: [task.iunits[2], task.iunits[3]],
                    task.intents[1].iid: [task.iunits[4], task.iunits[5]]
                }))
        run.save('./tmp')

        filepath = './tmp/ORG-test-1.xml'
        self.assertTrue(os.path.exists(filepath))
        tree = ET.parse(filepath)
        root = tree.getroot()
        for task in self.tasks['J']:
            self.assertIsNotNone(
                root.find("result[@qid='%s']" % task.query.qid))
            self.assertIsNotNone(
                root.find("result[@qid='%s']/first" % task.query.qid))
            for i in range(2):
                self.assertIsNotNone(
                    root.find("result[@qid='%s']/first/iunit[@uid='%s']" % (
                        task.query.qid, task.iunits[i].uid)))
                self.assertIsNotNone(
                    root.find("result[@qid='%s']/first/link[@iid='%s']" % (
                        task.query.qid, task.intents[i].iid)))
                self.assertIsNotNone(
                    root.find("result[@qid='%s']/second[@iid='%s']" % (
                        task.query.qid, task.intents[i].iid)))
                for idx in ([[2, 3], [4, 5]][i]):
                    self.assertIsNotNone(
                        root.find("result[@qid='%s']/second[@iid='%s']/iunit[@uid='%s']" % (
                            task.query.qid, task.intents[i].iid,
                            task.iunits[idx].uid)))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
