# -*- coding:utf-8 -*-
import unittest
from mobileclick.task import Task
from .testutils import create_query_subset, drop_query_subset

class MethodTestCase(unittest.TestCase):

    def setUp(self):
        self.queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            './data/MC2-training-documents/1C2-E.INDX/')
        self.tasks = Task.read(self.queryfilepath,
            './data/MC2-training/en/1C2-E-iunits.tsv',
            './data/MC2-training-documents/1C2-E.INDX/',
            './data/MC2-training-documents/1C2-E.HTML/')

    def tearDown(self):
        drop_query_subset()

    def read_runfile(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()
        return lines
