# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import LangModelRankingMethod
    from .scriptutils import ranking_parser, load_data_generate_run
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

    method = LangModelRankingMethod(_get_parser(args.language),
        min_count=args.min_count, smoothing=args.smoothing)
    load_data_generate_run(args, DESC, method)

def _get_parser(language):
    if language == 'english':
        from mobileclick.nlp import EnglishParser
        parser = EnglishParser()
    elif language == 'japanese':
        from mobileclick.nlp import JapaneseParser
        parser = JapaneseParser()
    else:
        raise Exception("Unknown language")
    return parser

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()

