# -*- coding:utf-8 -*-
import os, argparse
from mobileclick.task import Task

def ranking_parser(prog, desc):
    parser = argparse.ArgumentParser(prog=prog, description=desc)
    parser.add_argument('--runname', required=True,
        help='Name of this run (= output filename)')
    parser.add_argument('--query', required=True,
        help='Query filepath')
    parser.add_argument('--iunit', required=True,
        help='iUnit filepath')
    parser.add_argument('--indexdir', required=True,
        help='Index dirpath')
    parser.add_argument('--pagedir', required=True,
        help='Webpage dirpath')
    parser.add_argument('--outputdir', default='./',
        help='Output dirpath')
    return parser

def summarization_parser(prog, desc):
    parser = ranking_parser(prog, desc)
    parser.add_argument('--intent', required=True,
        help='Intent filepath')
    return parser

def add_lang_model_params(parser):
    parser.add_argument('--language', required=True, 
        choices=['english', 'japanese'],
        help='Language for parser (english or japanese)')
    parser.add_argument('--min_count', type=int, default=3,
        help='minumum frequncy for words to be used')
    parser.add_argument('--smoothing', type=float, default=1,
        help='added to the frequency of each word for smoothing')
    return parser

def get_parser(language):
    if language == 'english':
        from mobileclick.nlp import EnglishParser
        parser = EnglishParser()
    elif language == 'japanese':
        from mobileclick.nlp import JapaneseParser
        parser = JapaneseParser()
    else:
        raise Exception("Unknown language")
    return parser

def generate_run(args, desc, method, tasks):
    run = method.generate_run(args.runname, desc, tasks)
    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)
    filepath = run.save(args.outputdir)
    print "Saved results in %s" % filepath

def load_data_generate_ranking_run(args, desc, method):
    tasks = Task.read(args.query, args.iunit, args.indexdir, args.pagedir)
    print "Using the follwoing files/directories:"
    print "\tquery: %s" % args.query
    print "\tiunit: %s" % args.iunit
    print "\tindex: %s" % args.indexdir
    print "\tpage:  %s" % args.pagedir
    generate_run(args, desc, method, tasks)

def load_data_generate_summarization_run(args, desc, method):
    tasks = Task.read(args.query, args.iunit, args.indexdir, args.pagedir,
        args.intent)
    print "Using the follwoing files/directories:"
    print "\tquery: %s" % args.query
    print "\tiunit: %s" % args.iunit
    print "\tintent: %s" % args.intent
    print "\tindex: %s" % args.indexdir
    print "\tpage:  %s" % args.pagedir
    generate_run(args, desc, method, tasks)
