# -*- coding: utf-8 -*-
from .base_ranking_method import BaseRankingMethod

class RandomRankingMethod(BaseRankingMethod):
    '''
    Output iUnits in the same order in the iUnit file (~ random).
    Considered as the simplest baseline method
    '''

    def init(self, tasks): pass

    def rank(self, task):
        '''
        Output iUnits in the same order in the iUnit file
        '''
        print "Processing %s" % task.query.qid
        return [(i, 0) for i in task.iunits]
