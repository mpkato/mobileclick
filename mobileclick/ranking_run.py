# -*- coding: utf-8 -*-
from .utils import remove_breaks
from .run import Run

class RankingRun(Run):
    FILENAME_TEMPLATE = '%s.tsv'

    def save(self, dirpath='./'):
        '''
        Save the current results
        '''
        qids = sorted(self.results.keys())
        filepath = self._get_filepath(dirpath)
        with open(filepath, 'w') as f:
            # desc line
            f.write(remove_breaks(self.desc) + '\n')
            for qid in qids:
                iunit_scores = self.results[qid]
                for iunit, score in iunit_scores:
                    f.write('%s\t%s\n' % (iunit.output(), score))
        return filepath
