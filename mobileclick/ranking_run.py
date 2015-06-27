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

    def add(self, qid, iunit_scores):
        '''
        Add a sorted iUnit list
        Do not add iUnits more than once for the same QID
        '''
        if qid in self.results:
            raise Exception("Duplicate addition: %s" % qid)
        self.results[qid] = iunit_scores

    def save(self, dirpath='./'):
        '''
        Save the current results
        '''
        qids = sorted(self.results.keys())
        filename = self.FILENAME_TEMPLATE % safe_filename(self.name)
        filepath = os.path.join(dirpath, filename)
        with open(filepath, 'w') as f:
            # desc line
            f.write(remove_breaks(self.desc) + '\n')
            for qid in qids:
                iunit_scores = self.results[qid]
                for iunit, score in iunit_scores:
                    f.write('%s\t%s\n' % (iunit.output(), score))
        return filepath

    def validation(self, queries):
        '''
        Return True if all the queries have been added
        '''
        return all([q.qid in self.results for q in queries])
