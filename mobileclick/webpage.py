# -*- coding: utf-8 -*-
import os, glob

class Webpage(object):

    def __init__(self, filepath):
        self.filepath = filepath

    @classmethod
    def read(cls, filedir):
        '''
        Scan webpage filepaths
        '''
        result = []
        for filepath in glob.glob(os.path.join(filedir, '*.html')):
            print filepath
        return result
    
