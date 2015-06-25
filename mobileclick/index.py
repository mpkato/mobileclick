# -*- coding: utf-8 -*-
import csv

class Index(object):

    def __init__(self, rank, filename, title, url, body):
        self.rank = rank
        self.filename = filename
        self.title = title
        self.url = url
        self.body = body

    @classmethod
    def read(cls, filepath):
        '''
        Read indices from a tsv file
        '''
        result = []
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                index = Index.load(row)
                result.append(index)
        return result

    @classmethod
    def load(cls, row):
        '''
        Load an index from a tuple
        '''
        if len(row) != 5:
            raise Exception("Invalid line: %s" % str(row))
        rank, filename, title, url, body = row
        rank = int(rank) # rank must be integer
        return Index(rank, filename, title, url, body)
