# -*- coding:utf-8 -*-
import unittest
import nose
import os
from mobileclick.task import Task
from mobileclick.retrieval_run import RetrievalRun
from .testutils import create_query_subset, drop_query_subset

class RetrievalRunTestCase(unittest.TestCase):
    INDX_DIRPATH = './data/MC2-training-documents/1C2-E.INDX/'

    def setUp(self):
        self.queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            self.INDX_DIRPATH)
        self.tasks = Task.read(self.queryfilepath,
            './data/MC2-training/en/1C2-E-iunits.tsv',
            './data/MC2-training-documents/1C2-E.INDX/',
            './data/MC2-training-documents/1C2-E.HTML/')
        if not os.path.exists('./tmp'):
            os.mkdir('./tmp')

    def tearDown(self):
        drop_query_subset()

    def test_task_read(self):
        '''
        Task.read
        '''
        run = RetrievalRun('ORG-test-1', 'this is a test run')
        for task in self.tasks:
            run.add(task.query.qid, task.iunits)
        run.save('./tmp')
        self.assertTrue(os.path.exists('./tmp/ORG-test-1.tsv'))
        with open('./tmp/ORG-test-1.tsv', 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines),
            sum([len(t.iunits) for t in self.tasks]) + 1)
        self.assertEqual(lines[0].strip(), 'this is a test run')
        self.assertEqual(len(lines[1].split('\t')), 2)

    def test_bad_break(self):
        '''
        Ensure no break in the first line
        '''
        run = RetrievalRun('ORG-test-1', 'this is \n a test run')
        run.save('./tmp')
        with open('./tmp/ORG-test-1.tsv', 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)

    def test_all_iunits(self):
        '''
        Ensure all the iUnits are included
        '''
        run = RetrievalRun('ORG-test-1', 'this is a test run')
        iunits = []
        for task in self.tasks:
            run.add(task.query.qid, task.iunits)
            for i in task.iunits:
                iunits.append(i.uid)
        run.save('./tmp')
        output_iunits = set()
        with open('./tmp/ORG-test-1.tsv', 'r') as f:
            for lineno, line in enumerate(f):
                if lineno != 0:
                    uid = line.split('\t')[1].strip()
                    output_iunits.add(uid)
        self.assertEqual(len(set(iunits)), len(output_iunits))
        for i in iunits:
            self.assertIn(i, output_iunits)

    def test_validation(self):
        '''
        Test the validation
        '''
        run = RetrievalRun('ORG-test-1', 'this is a test run')
        for task in self.tasks[:-2]:
            print task.query.qid
            run.add(task.query.qid, task.iunits)
        queries = [t.query for t in self.tasks]
        self.assertFalse(run.validation(queries))
        for task in self.tasks[-2:]:
            run.add(task.query.qid, task.iunits)
        self.assertTrue(run.validation(queries))

    def test_duplicate_addition(self):
        '''
        RetrievalRun.add raises if iUnits were added more than once for the same QID
        '''
        run = RetrievalRun('ORG-test-1', 'this is a test run')
        run.add('1', [])
        self.assertRaises(Exception, run.add, '1', [])

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
