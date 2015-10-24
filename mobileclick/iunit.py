# -*- coding: utf-8 -*-
import csv
from xml.etree.ElementTree import Element

class Iunit(object):

    def __init__(self, qid, uid, body):
        self.qid = qid
        self.uid = uid
        self.body = body

    def output(self):
        '''
        Output format for submission
        '''
        return '\t'.join((self.qid, self.uid))

    def to_xml(self):
        return Element('iunit', uid=self.uid)

    @classmethod
    def read(cls, filepath):
        '''
        Read iUnits from a tsv file
        '''
        result = []
        with open(filepath, 'rb') as f:
            reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                iunit = Iunit.load(row)
                result.append(iunit)
        return result

    @classmethod
    def load(cls, row):
        '''
        Load an iUnit from a tuple
        '''
        if len(row) != 3:
            raise Exception("Invalid line: %s" % str(row))
        qid, uid, body = row
        return Iunit(qid, uid, body)
