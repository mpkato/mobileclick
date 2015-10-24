# -*- coding:utf-8 -*-
import unittest
from mobileclick import Task
from .testutils import create_query_subset, create_tmp_intent_file, drop_tmp_files

class SummarizationMethodTestCase(unittest.TestCase):

    def setUp(self):
        self.tasks = {}
        for lang in [('en', 'E'), ('ja', 'J')]:
            queryfilepath = create_query_subset(
                './data/MC2-training/%s/1C2-%s-queries.tsv' % lang,
                './data/MC2-training-documents/1C2-%s.INDX/' % lang[1])
            intentfilepath = create_tmp_intent_file(queryfilepath)
            self.tasks[lang[1]] = Task.read(queryfilepath,
                './data/MC2-training/%s/1C2-%s-iunits.tsv' % lang,
                './data/MC2-training-documents/1C2-%s.INDX/' % lang[1],
                './data/MC2-training-documents/1C2-%s.HTML/' % lang[1],
                intentfilepath)

    def tearDown(self):
        drop_tmp_files()
