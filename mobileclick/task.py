# -*- coding: utf-8 -*-
from .query import Query
from .iunit import Iunit
from .index_factory import IndexFactory
from itertools import groupby

class Task(object):
    '''
    Composite of a query, iUnits, and indices
    '''

    def __init__(self, query, iunits, indices):
        self.query = query
        self.iunits = iunits
        self.indices = indices

    @classmethod
    def read(cls, queryfilepath, iunitfilepath, indexdirpath, webpagedirpath):
        '''
        Read all the data
        '''
        queries = Query.read(queryfilepath)
        iunitsets = Iunit.read(iunitfilepath)
        qid_iunits = {qid: list(iunits) for qid, iunits
            in groupby(iunitsets, key=lambda x: x.qid)}
        factory = IndexFactory(indexdirpath, webpagedirpath)

        result = []
        for query in queries:
            iunits = qid_iunits[query.qid]
            indices = factory.read(query.qid)
            task = Task(query, iunits, indices)
            result.append(task)
        return result

