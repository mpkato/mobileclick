# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Task
from .testutils import create_query_subset, drop_tmp_files
from .testutils import create_tmp_intent_file

class TaskIntentTestCase(unittest.TestCase):

    def setUp(self):
        self.queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            './data/MC2-training-documents/1C2-E.INDX/')
        self.intentfilepath = create_tmp_intent_file(self.queryfilepath)

    def tearDown(self):
        drop_tmp_files()

    def test_task_read(self):
        '''
        Task.read
        '''
        tasks = Task.read(self.queryfilepath,
            './data/MC2-training/en/1C2-E-iunits.tsv',
            './data/MC2-training-documents/1C2-E.INDX/',
            './data/MC2-training-documents/1C2-E.HTML/',
            self.intentfilepath)
        self.assertEqual(len(tasks), 5)
        self.assertEqual(tasks[0].query.qid, '1C2-E-0001')
        self.assertEqual(len(tasks[0].intents), 5)
        self.assertEqual(tasks[0].intents[0].qid, '1C2-E-0001')
        self.assertEqual(tasks[0].intents[0].iid, '1C2-E-0001-INTENT0001')

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
