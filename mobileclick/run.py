# -*- coding: utf-8 -*-
import os
from .utils import safe_filename

class Run(object):
    def __init__(self, name, desc):
        '''
        name is used for the output filename
        desc is written at the first line of the output file
        '''
        self.name = name
        self.desc = desc
        self.results = {}

    def add(self, qid, elem):
        '''
        Add a result (either
            - sorted list of (Iunit, Float) for iUnit Ranking, or
            - Summary for iUnit Summarization
        Do not add a result more than once for the same QID
        '''
        if qid in self.results:
            raise Exception("Duplicate addition: %s" % qid)
        self.results[qid] = elem

    def validation(self, queries):
        '''
        Return True if all the queries have been added
        '''
        return all([q.qid in self.results for q in queries])

    def _get_filepath(self, dirpath):
        filename = self.FILENAME_TEMPLATE % safe_filename(self.name)
        filepath = os.path.join(dirpath, filename)
        return filepath
