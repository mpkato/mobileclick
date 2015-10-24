# -*- coding: utf-8 -*-

class FreqFactory(object):
    '''
    Generate word freqency information
    '''
    def __init__(self, parser):
        self.parser = parser

    def count(self, tasks):
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

    def find_infrequent_words(self, total_word_freq, min_count):
        '''
        Find words whose frequncy is less than min_count
        '''
        return set([w for w, f in total_word_freq.items()
            if f < min_count])
