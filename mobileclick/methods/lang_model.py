# -*- coding: utf-8 -*-
import numpy as np

class LangModel(object):
    '''
    Compute LM-related values
    '''
    def __init__(self, parser, min_count, smoothing, tasks):
        self.parser = parser
        self.smoothing = smoothing
        self.wfreqs, self.total_wfreqs = self._count(tasks)
        self.infreqwords = self._find_infrequent_words(
            self.total_wfreqs, min_count)

        # learn odds ratio
        self.odds_ratio = {}
        for task in tasks:
            self.odds_ratio[task.query.qid] = self._learn_odds_ratio(task)

    def _learn_odds_ratio(self, task):
        '''
        Learn word_log_odds_ratio(w) = lnP(w|q) - lnP(w|o)
        '''
        wfreq = self.wfreqs[task.query.qid]

        q_num = sum([f for w, f in wfreq.items() if not w in self.infreqwords])
        o_num = sum([f for w, f in self.total_wfreqs.items()
            if not w in self.infreqwords]) - q_num
        w_num = len(self.total_wfreqs) - len(self.infreqwords)
        result = {}
        for w in self.total_wfreqs:
            if not w in self.infreqwords:
                pwq = np.log(wfreq.get(w, 0) + self.smoothing)\
                    - np.log(q_num + self.smoothing * w_num)
                nwo = self.total_wfreqs.get(w, 0) - wfreq.get(w, 0)
                pwo = np.log(nwo + self.smoothing)\
                    - np.log(o_num + self.smoothing * w_num)
                result[w] = pwq - pwo
        return result

    def _count(self, tasks):
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

    def _find_infrequent_words(self, total_word_freq, min_count):
        '''
        Find words whose frequncy is less than min_count
        '''
        return set([w for w, f in total_word_freq.items()
            if f < min_count])
