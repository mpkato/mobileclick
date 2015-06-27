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

def load_data_generate_run(args, desc, method):
    tasks = Task.read(args.query, args.iunit, args.indexdir, args.pagedir)
    print "Using the follwoing files/directories:"
    print "\tquery: %s" % args.query
    print "\tiunit: %s" % args.iunit
    print "\tindex: %s" % args.indexdir
    print "\tpage:  %s" % args.pagedir
    run = method.generate_run(args.runname, desc, tasks)
    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)
    filepath = run.save(args.outputdir)
    print "Saved results in %s" % filepath
