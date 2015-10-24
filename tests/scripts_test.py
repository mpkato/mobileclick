# -*- coding:utf-8 -*-
import unittest
import nose
from .testutils import create_query_subset, drop_tmp_files

class ScriptsTestCase(unittest.TestCase):

    def test_mobileclick_download_training_data(self):
        '''
        Download a subset of the full training data
        '''
        import os
        from mobileclick.scripts.mobileclick_download_training_data import main
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

    def test_mobileclick_download_test_data(self):
        '''
        Download a subset of the full test data
        '''
        import os
        from mobileclick.scripts.mobileclick_download_test_data import main
        files = [
            './data/MC2-test/en/MC2-E-iunits.tsv', 
            './data/MC2-training-documents/1C2-E.HTML/1C2-E-0001-1.html'
            ]
        # check if files have been downloaded
        if not all([os.path.exists(f) for f in files]):
            main(istest=True)
            # files to be downloaded
            for f in files:
                self.assertTrue(os.path.exists(f))

    def test_mobileclick_random_ranking_method(self):
        '''
        Random ranking method
        '''
        from mobileclick.scripts.mobileclick_random_ranking_method import main
        queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            './data/MC2-training-documents/1C2-E.INDX/')

        main(['--runname', 'test',
            '--query', queryfilepath,
            '--iunit', './data/MC2-training/en/1C2-E-iunits.tsv',
            '--index', './data/MC2-training-documents/1C2-E.INDX/',
            '--pagedir', './data/MC2-training-documents/1C2-E.HTML/',
            '--outputdir', './runs'])

        drop_tmp_files()

    def test_mobileclick_lang_model_ranking_method(self):
        '''
        Lang Model ranking method
        '''
        from mobileclick.scripts.mobileclick_lang_model_ranking_method import main
        queryfilepath = create_query_subset(
            './data/MC2-training/en/1C2-E-queries.tsv',
            './data/MC2-training-documents/1C2-E.INDX/')

        main(['--runname', 'test',
            '--query', queryfilepath,
            '--iunit', './data/MC2-training/en/1C2-E-iunits.tsv',
            '--index', './data/MC2-training-documents/1C2-E.INDX/',
            '--pagedir', './data/MC2-training-documents/1C2-E.HTML/',
            '--outputdir', './runs',
            '--language', 'english'])

        drop_tmp_files()

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
