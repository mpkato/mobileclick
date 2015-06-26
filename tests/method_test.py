# -*- coding:utf-8 -*-
import unittest
from mobileclick.task import Task
from .testutils import create_query_subset, drop_query_subset

class MethodTestCase(unittest.TestCase):

    def setUp(self):
        self.tasks = {}
        for lang in [('en', 'E'), ('ja', 'J')]:
            queryfilepath = create_query_subset(
                './data/MC2-training/%s/1C2-%s-queries.tsv' % lang,
                './data/MC2-training-documents/1C2-%s.INDX/' % lang[1])
            self.tasks[lang[1]] = Task.read(queryfilepath,
                './data/MC2-training/%s/1C2-%s-iunits.tsv' % lang,
                './data/MC2-training-documents/1C2-%s.INDX/' % lang[1],
                './data/MC2-training-documents/1C2-%s.HTML/' % lang[1])

    def tearDown(self):
        drop_query_subset()

    def read_runfile(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
        return lines
