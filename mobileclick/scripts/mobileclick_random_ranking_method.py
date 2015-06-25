# -*- coding:utf-8 -*-

def main(argv=None):
    import os, argparse
    from mobileclick.task import Task
    from mobileclick.methods import RandomRankingMethod
    DESC = 'A random baseline for the iUnit ranking subtask.'

    parser = argparse.ArgumentParser(
        prog="mobileclick_random_ranking_method",
        description=DESC)
    parser.add_argument('--runname', required="Run name",
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
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    tasks = Task.read(args.query, args.iunit, args.indexdir, args.pagedir)
    method = RandomRankingMethod()
    run = method.generate_run(args.runname, DESC, tasks)
    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)
    run.save(args.outputdir)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()
