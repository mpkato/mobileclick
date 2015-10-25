# -*- coding: utf-8 -*-
from ..summary import Summary
from .base_summarization_method import BaseSummarizationMethod

class RandomSummarizationMethod(BaseSummarizationMethod):
    '''
    Add iUnits in the same order in the iUnit file to the first layer (~ random).
    Considered as the simplest baseline method
    '''

    def init(self, tasks): pass

    def summarize(self, task):
        '''
        Output iUnits in the same order in the iUnit file
        '''
        print "Processing %s" % task.query.qid
        return Summary(task.query.qid, task.iunits)
