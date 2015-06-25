# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Task
from .testutils import create_query_subset, drop_query_subset

class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            './data/MC2-training-documents/1C2-E.INDX/')

    def tearDown(self):
        drop_query_subset()

    def test_task_read(self):
        '''
        Task.read
        '''
        tasks = Task.read(self.queryfilepath,
            './data/MC2-training/en/1C2-E-iunits.tsv',
            './data/MC2-training-documents/1C2-E.INDX/',
            './data/MC2-training-documents/1C2-E.HTML/')
        self.assertEqual(len(tasks), 5)
        self.assertEqual(tasks[0].query.qid, '1C2-E-0001')
        self.assertEqual(len(tasks[0].iunits), 19)
        self.assertEqual(tasks[0].iunits[0].qid, '1C2-E-0001')
        self.assertEqual(tasks[0].iunits[0].uid, '1C2-E-0001-0001')
        self.assertEqual(len(tasks[0].indices), 213)
        self.assertEqual(tasks[0].indices[0].qid, '1C2-E-0001')
        self.assertEqual(tasks[0].indices[0].rank, 1)

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
