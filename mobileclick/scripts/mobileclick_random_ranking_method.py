# -*- coding:utf-8 -*-

def main(argv=None):
    import os
    from mobileclick.task import Task
    from mobileclick.methods import RandomRankingMethod
    from .scriptutils import ranking_parser
    DESC = 'A random baseline for the iUnit ranking subtask.'

    parser = ranking_parser(prog="mobileclick_random_ranking_method", desc=DESC)
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
