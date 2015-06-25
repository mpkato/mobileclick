# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from ..ranking_run import RankingRun

class BaseRankingMethod(object):
    '''
    Abstract class for ranking methods
    '''
    __metaclass__ = ABCMeta

    def generate_run(self, name, desc, tasks):
        self.init(tasks)
        result = RankingRun(name, desc)
        for task in tasks:
            ranked_iunits = self.rank(task)
            result.add(task.query.qid, ranked_iunits)
        return result

    @abstractmethod
    def init(self): pass

    @abstractmethod
    def rank(self, task): pass
