# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick.scripts.mobileclick_download_data import main

class DownloadScriptTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_download_mobileclick_data(self):
        '''
        Download a subset of the full training data
        '''
        import os
        files = [
            './data/MC2-training/en/1C2-E-iunits.tsv', 
            './data/MC2-training-documents/1C2-E.HTML/1C2-E-0001-1.html'
            ]
        # check if files have been downloaded
        if not all([os.path.exists(f) for f in files]):
            main(istest=True)
            # files to be downloaded
            for f in files:
                self.assertTrue(os.path.exists(f))

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
