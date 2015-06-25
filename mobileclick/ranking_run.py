# -*- coding: utf-8 -*-
import os
from .utils import safe_filename, remove_breaks

class RankingRun(object):
    FILENAME_TEMPLATE = '%s.tsv'

    def __init__(self, name, desc):
        '''
        name is used for the output filename
        desc is written at the first line of the output file
        '''
        self.name = name
        self.desc = desc
        self.results = {}

    def add(self, qid, iunits):
        '''
        Add a sorted iUnit list
        Do not add iUnits more than once for the same QID
        '''
        if qid in self.results:
            raise Exception("Duplicate addition: %s" % qid)
        self.results[qid] = iunits

    def save(self, dirpath='./'):
        '''
        Save the current results
        '''
        qids = sorted(self.results.keys())
        filename = self.FILENAME_TEMPLATE % safe_filename(self.name)
        with open(os.path.join(dirpath, filename), 'w') as f:
            # desc line
            f.write(remove_breaks(self.desc) + '\n')
            for qid in qids:
                iunits = self.results[qid]
                for iunit in iunits:
                    f.write('%s\n' % iunit.output())

    def validation(self, queries):
        '''
        Return True if all the queries have been added
        '''
        return all([q.qid in self.results for q in queries])
