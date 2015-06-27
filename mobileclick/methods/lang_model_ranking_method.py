# -*- coding: utf-8 -*-
from .base_ranking_method import BaseRankingMethod
import numpy as np

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

    def init(self, tasks):
        '''
        Count the frequency of words
        '''
        print "Initializing ..."
        self.wfreqs, self.total_wfreqs = self._count_word_freq(tasks)
        self.infreqwords = self._find_infrequent_words(self.total_wfreqs)

    def rank(self, task):
        '''
        Output iUnits in order of the log odds ratio
        '''
        print "Processing %s" % task.query.qid
        wlor = self._learn_word_log_odds_ratio(task.query.qid)
        result = []
        for iunit in task.iunits:
            words = self.parser.word_tokenize(iunit.body)
            odds_ratio = sum([wlor.get(w, 0.0) for w in words])
            result.append((iunit, odds_ratio))
        return sorted(result, key=lambda x: x[1], reverse=True)

    def _learn_word_log_odds_ratio(self, qid):
        '''
        Learn word_log_odds_ratio(w) = lnP(w|q) - lnP(w|o)
        '''
        q_num = sum([f for w, f in self.wfreqs[qid].items()
            if not w in self.infreqwords])
        o_num = sum([f for w, f in self.total_wfreqs.items()
            if not w in self.infreqwords]) - q_num
        w_num = len(self.total_wfreqs) - len(self.infreqwords)
        result = {}
        for w in self.total_wfreqs:
            if not w in self.infreqwords:
                pwq = np.log(self.wfreqs[qid].get(w, 0) + self.smoothing)\
                    - np.log(q_num + self.smoothing * w_num)
                nwo = self.total_wfreqs.get(w, 0) - self.wfreqs[qid].get(w, 0)
                pwo = np.log(nwo + self.smoothing)\
                    - np.log(o_num + self.smoothing * w_num)
                result[w] = pwq - pwo
        return result

    def _count_word_freq(self, tasks):
        '''
        Count the frequency of words
        Return: (task_word_freq, total_word_freq)
        '''
        task_word_freq = {}
        total_word_freq = {}
        for task in tasks:
            wfreq = {}
            for i in task.indices:
                txt = i.title + ' ' + i.body
                txt = txt.decode('utf-8')
                words = self.parser.word_tokenize(txt)
                for w in words:
                    wfreq[w] = wfreq.get(w, 0) + 1
                    total_word_freq[w] = total_word_freq.get(w, 0) + 1
            task_word_freq[task.query.qid] = wfreq
        return (task_word_freq, total_word_freq)

    def _find_infrequent_words(self, total_word_freq):
        '''
        Find words whose frequncy is less than min_count
        '''
        return set([w for w, f in total_word_freq.items()
            if f < self.min_count])
