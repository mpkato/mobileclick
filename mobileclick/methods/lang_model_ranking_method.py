# -*- coding: utf-8 -*-
from .base_ranking_method import BaseRankingMethod
from .lang_model import LangModel

class LangModelRankingMethod(BaseRankingMethod):
    '''
    Output iUnits based on the odds ratio between a document group on a query 
    and the others.
    Considered as a baseline method

    Let D_q be a document set on query q, and D_o be the other documents.
    A language model P(w|q) can be obtained by MLE:

        P(w|q) = n_{D_q, w} / n_{D_q}

    where n_{D_q, w} is the frequency of word w in D_q,
    and n_{D_q} is the number of words in D_q.
    P(w|o) can be estimated in the same way.

    Log odds ratio of an iUnit u that comprises word set W_u
    is defined as follows:

        LogOdds(u) = \sum_{w in W_u} {lnP(w|q) - lnP(w|o)}

    This method ranks iUnits in order of the log odds ratio.
    The current version just utilizes nouns in titles and summaries of 
    search engine indices to estimate the language models.
    '''

    def __init__(self, parser, min_count=3, smoothing=1):
        '''
        parser: must have "word_tokenize" method
        min_count: minumum frequncy for words to be used
        smoothing: added to the frequency of each word for smoothing
        '''
        self.parser = parser
        self.min_count = min_count
        self.smoothing = smoothing
        self.lm = None

    def init(self, tasks):
        '''
        Count the frequency of words
        '''
        print "Initializing ..."
        self.lm = LangModel(self.parser,
            self.min_count, self.smoothing, tasks)

    def rank(self, task):
        '''
        Output iUnits in order of the log odds ratio
        '''
        print "Processing %s" % task.query.qid
        if self.lm is None:
            raise Exception("Not initialized. Please init LangModel.")
        wlor = self.lm.odds_ratio[task.query.qid]
        result = []
        for iunit in task.iunits:
            words = self.parser.word_tokenize(iunit.body)
            odds_ratio = sum([wlor.get(w, 0.0) for w in words])
            result.append((iunit, odds_ratio))
        return sorted(result, key=lambda x: x[1], reverse=True)
