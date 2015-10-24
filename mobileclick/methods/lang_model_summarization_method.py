# -*- coding: utf-8 -*-
from ..summary import Summary
from .base_summarization_method import BaseSummarizationMethod
from .lang_model_ranking_method import LangModelRankingMethod

class LangModelSummarizationMethod(BaseSummarizationMethod):
    '''
    Rank iUnits based on the LM-based method used in iUnit ranking,
    and put the iUnits in the first layer in the ranking order.
    '''

    def __init__(self, parser, min_count=3, smoothing=1):
        '''
        parser: must have "word_tokenize" method
        min_count: minumum frequncy for words to be used
        smoothing: added to the frequency of each word for smoothing
        '''
        self.ranking = LangModelRankingMethod(parser, min_count, smoothing)

    def init(self, tasks):
        '''
        Count the frequency of words
        '''
        print "Initializing ..."
        self.ranking.init(tasks)

    def summarize(self, task):
        '''
        Output iUnits in order of the log odds ratio in the first layer
        '''
        print "Processing %s" % task.query.qid
        iunit_score_list = self.ranking.rank(task)
        return Summary(task.query.qid, [iunit for iunit, score in iunit_score_list])
