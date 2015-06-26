# -*- coding:utf-8 -*-

def main(argv=None):
    import os
    from mobileclick.task import Task
    from mobileclick.methods import LangModelRankingMethod
    from mobileclick.nlp import EnglishParser
    from .scriptutils import ranking_parser
    DESC = 'A LM-based baseline for the iUnit ranking subtask.'

    parser = ranking_parser(prog="mobileclick_lang_model_ranking_method", desc=DESC)
    parser.add_argument('--language', required=True, 
        choices=['english', 'japanese'],
        help='Language for parser (english or japanese)')
    parser.add_argument('--min_count', type=int, default=3,
        help='minumum frequncy for words to be used')
    parser.add_argument('--smoothing', type=float, default=1,
        help='added to the frequency of each word for smoothing')
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()
    if args.language == 'english':
        parser = EnglishParser()
    elif args.language == 'japanese':
        raise Exception("Not implemented")
    else:
        raise Exception("Unknown language")

    tasks = Task.read(args.query, args.iunit, args.indexdir, args.pagedir)
    method = LangModelRankingMethod(parser,
        min_count=args.min_count, smoothing=args.smoothing)
    run = method.generate_run(args.runname, DESC, tasks)
    if not os.path.exists(args.outputdir):
        os.makedirs(args.outputdir)
    run.save(args.outputdir)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()

