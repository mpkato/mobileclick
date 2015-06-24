# -*- coding: utf-8 -*-
import csv

class Query(object):

    def __init__(self, qid, body):
        self.qid = qid
        self.body = body

    @classmethod
    def read(cls, filepath):
        '''
        Read queries from a tsv file
        '''
        result = []
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                query = Query.load(row)
                result.append(query)
        return result

    @classmethod
    def load(cls, row):
        '''
        Load a query from a tuple
        '''
        if len(row) != 2:
            raise Exception("Invalid line: %s" % str(row))
        qid, body = row
        return Query(qid, body)

