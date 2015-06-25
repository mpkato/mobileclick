# -*- coding:utf-8 -*-
import os, glob, shutil

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

def drop_query_subset():
    if os.path.exists('./tmp'):
        shutil.rmtree('./tmp')
