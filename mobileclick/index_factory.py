# -*- coding: utf-8 -*-
import os, glob, csv
from .index import Index

class IndexFactory(object):
    def __init__(self, indexdir, webpagedir):
        '''
        indexdir: dir including index files
        webpagedir: dir including webpages
        '''
        self.indexdir = indexdir
        self.webpagedir = webpagedir

    def read(self, qid):
        '''
        Read indices for a given QID
        '''
        indexfilepath = glob.glob(os.path.join(self.indexdir, '*%s*' % qid))
        if len(indexfilepath) == 0:
            raise Exception('Index file not found: %s', qid)
        if len(indexfilepath) > 1:
            raise Exception('Duplicate index files: %s', str(indexfilepath))
        indexfilepath = indexfilepath[0]
        indices = self._read_index(qid, indexfilepath)
        return indices

    def _read_index(self, qid, filepath):
        '''
        Read indices from a tsv file
        '''
        result = []
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                index = self._load_index(qid, row)
                result.append(index)
        return result

    def _load_index(self, qid, row):
        '''
        Load an index from a tuple
        '''
        if len(row) != 5:
            raise Exception("Invalid line: %s" % str(row))
        rank, filename, title, url, body = row
        rank = int(rank) # rank must be integer
        filepath = os.path.join(os.path.abspath(self.webpagedir), filename)
        return Index(qid, rank, filepath, title, url, body)
