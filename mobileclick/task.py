# -*- coding: utf-8 -*-
from .query import Query
from .iunit import Iunit
from .intent import Intent
from .index_factory import IndexFactory
from itertools import groupby

class Task(object):
    '''
    Composite of a query, iUnits, and indices + intents
    '''

    def __init__(self, query, iunits, indices, intents=None):
        self.query = query
        self.iunits = iunits
        self.indices = indices
        if intents is not None:
            self.intents = intents

    @classmethod
    def read(cls, queryfilepath, iunitfilepath, indexdirpath, webpagedirpath,
        intentfilepath=None):
        '''
        Read all the data
        '''
        queries = Query.read(queryfilepath)
        iunitsets = Iunit.read(iunitfilepath)
        qid_iunits = {qid: list(iunits) for qid, iunits
            in groupby(iunitsets, key=lambda x: x.qid)}
        if intentfilepath is not None:
            intentsets = Intent.read(intentfilepath)
            qid_intents = {qid: list(intents) for qid, intents
                in groupby(intentsets, key=lambda x: x.qid)}
        factory = IndexFactory(indexdirpath, webpagedirpath)

        result = []
        for query in queries:
            iunits = qid_iunits[query.qid] if query.qid in qid_iunits else []
            indices = factory.read(query.qid)
            if intentfilepath is not None:
                intents = qid_intents[query.qid]\
                    if query.qid in qid_iunits else []
                task = Task(query, iunits, indices, intents)
            else:
                task = Task(query, iunits, indices)
            result.append(task)
        return result
