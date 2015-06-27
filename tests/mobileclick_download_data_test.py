# -*- coding:utf-8 -*-
import unittest
import nose
import os, shutil
from mobileclick.scripts.mobileclick_download_data import (
    login, download_file, find_download_links, deploy_data)

class MobileclickDownloadDataTestCase(unittest.TestCase):

    def test_login(self):
        '''
        Login to http://www.mobileclick.org/
        '''
        self.assertTrue(self._login())

    def test_download_file(self):
        '''
        Download data from http://www.mobileclick.org/home/data
        '''
        self._login()
        links = find_download_links(True)
        filepath = download_file(links[0])
        self.assertTrue(os.path.exists(filepath))

    def test_find_download_links(self):
        '''
        Find download links from http://www.mobileclick.org/home/data
        '''
        self._login()
        links = find_download_links(True)
        for link in links:
            self.assertTrue(link.startswith("http"))

    def test_deploy_data(self):
        '''
        Extract files from tar.gz
        '''
        self._login()
        links = find_download_links(True)
        filepath = download_file(links[0]) # MC2-training
        deploy_data(filepath, './tmp')
        self.assertTrue(os.path.exists('./tmp/MC2-training'))
        self.assertTrue(os.path.exists('./tmp/MC2-training/en/1C2-E-queries.tsv'))
        if os.path.exists('./tmp'):
            shutil.rmtree('./tmp')

    def _login(self):
        email = os.environ.get('MOBILECLICK_EMAIL', None)
        password = os.environ.get('MOBILECLICK_PASSWORD', None)
        return login(email, password)
