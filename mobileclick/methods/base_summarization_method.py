# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from ..summarization_run import SummarizationRun

class BaseSummarizationMethod(object):
    '''
    Abstract class for summarization methods
    '''
    __metaclass__ = ABCMeta

    def generate_run(self, name, desc, tasks):
        self.init(tasks)
        result = SummarizationRun(name, desc)
        for task in tasks:
            summary = self.summarize(task)
            result.add(task.query.qid, summary)
        return result

    @abstractmethod
    def init(self): pass

    @abstractmethod
    def summarize(self, task): pass

