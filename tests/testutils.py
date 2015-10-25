# -*- coding:utf-8 -*-
import os, glob, shutil

TEST_INTENT_FILE = './tmp/TEST-intents.tsv'

def create_query_subset(queryfilepath, indexdirpath):
    '''
    Create a query file that includes only a subset of the queries
    '''
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    with open(queryfilepath, 'r') as f:
        querylines = f.readlines()
    subsetlines = []
    for queryline in querylines:
        qid = queryline.split('\t')[0]
        if len(glob.glob('%s*%s*' % (indexdirpath, qid))) == 1:
            subsetlines.append(queryline)
    outputfilename = os.path.basename(queryfilepath)
    with open('./tmp/%s' % outputfilename, 'w') as f:
        for subsetline in subsetlines:
            f.write(subsetline)
    return './tmp/%s' % outputfilename

def create_tmp_intent_file(subset_queryfilepath):
    '''
    Create an intent file for only queries in the subset
    '''
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    with open(subset_queryfilepath, 'r') as f:
        querylines = f.readlines()
    with open(TEST_INTENT_FILE, 'w') as f:
        for queryline in querylines:
            qid = queryline.split('\t')[0]
            for i in range(4):
                f.write('\t'.join(
                    (qid, '%s-INTENT%04d' % (qid, i+1), 'Test%04d' % (i+1))) + '\n')
            # for testing two layer summarization
            f.write('\t'.join(
                (qid, '%s-INTENT%04d' % (qid, 5), 'album')) + '\n')
    return TEST_INTENT_FILE

def drop_tmp_files():
    if os.path.exists('./tmp'):
        shutil.rmtree('./tmp')
