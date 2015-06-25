# -*- coding:utf-8 -*-
import nose
import os
from mobileclick import RankingRun
from .method_test import MethodTestCase

class RankingRunTestCase(MethodTestCase):

    def test_task_read(self):
        '''
        Task.read
        '''
        run = RankingRun('ORG-test-1', 'this is a test run')
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
        run = RankingRun('ORG-test-1', 'this is \n a test run')
        run.save('./tmp')
        with open('./tmp/ORG-test-1.tsv', 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)

    def test_all_iunits(self):
        '''
        Ensure all the iUnits are included
        '''
        run = RankingRun('ORG-test-1', 'this is a test run')
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
        run = RankingRun('ORG-test-1', 'this is a test run')
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
        RankingRun.add raises if iUnits were added more than once for the same QID
        '''
        run = RankingRun('ORG-test-1', 'this is a test run')
        run.add('1', [])
        self.assertRaises(Exception, run.add, '1', [])

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
