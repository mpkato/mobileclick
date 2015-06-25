# -*- coding:utf-8 -*-
import unittest
import nose
import os, glob, shutil
from mobileclick.task import Task

class TaskTestCase(unittest.TestCase):
    INDX_DIRPATH = './data/MC2-training-documents/1C2-E.INDX/'

    def setUp(self):
        '''
        Create a query file that includes only a subset of the queries
        '''
        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')
        with open('./data/MC2-training/en/1C2-E-queries.tsv', 'r') as f:
            querylines = f.readlines()
        subsetlines = []
        for queryline in querylines:
            qid = queryline.split('\t')[0]
            if len(glob.glob('%s*%s*' % (self.INDX_DIRPATH, qid))) == 1:
                subsetlines.append(queryline)
        with open('./tmp/1C2-E-queries.tsv', 'w') as f:
            for subsetline in subsetlines:
                f.write(subsetline)

    def tearDown(self):
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')

    def test_task_read(self):
        '''
        Task.read
        '''
        tasks = Task.read('./tmp/1C2-E-queries.tsv',
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
