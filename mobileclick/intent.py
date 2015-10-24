# -*- coding: utf-8 -*-
import csv
from xml.etree.ElementTree import Element

class Intent(object):

    def __init__(self, qid, iid, body):
        self.qid = qid
        self.iid = iid
        self.body = body

    def output(self):
        '''
        Output format for submission
        '''
        return '\t'.join((self.qid, self.iid))

    def to_xml(self):
        return Element('link', iid=self.iid)

    @classmethod
    def read(cls, filepath):
        '''
        Read intents from a tsv file
        '''
        result = []
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                intent = Intent.load(row)
                result.append(intent)
        return result

    @classmethod
    def load(cls, row):
        '''
        Load an intent from a tuple
        '''
        if len(row) != 3:
            raise Exception("Invalid line: %s" % str(row))
        qid, iid, body = row
        return Intent(qid, iid, body)

