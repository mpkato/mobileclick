# -*- coding:utf-8 -*-
DATA_FILENAME = 'MC2-test.tar.gz'
DOC_FILENAME = 'MC2-test-documents.tar.gz'
from .mobileclick_download_data import download_and_deploy, SUBSET_FILENAME

def main(istest=False):
    docfilename = SUBSET_FILENAME if istest else DOC_FILENAME
    download_and_deploy([DATA_FILENAME, docfilename])

if __name__ == '__main__':
    main()
