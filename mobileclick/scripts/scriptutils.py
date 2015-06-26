# -*- coding:utf-8 -*-
import argparse

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
