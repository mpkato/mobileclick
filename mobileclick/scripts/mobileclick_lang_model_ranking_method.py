# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import LangModelRankingMethod
    from .scriptutils import (ranking_parser, get_parser,
        load_data_generate_ranking_run, add_lang_model_params)
    DESC = 'A LM-based baseline for the iUnit ranking subtask.'

    parser = ranking_parser(prog="mobileclick_lang_model_ranking_method", desc=DESC)
    parser = add_lang_model_params(parser)
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    method = LangModelRankingMethod(get_parser(args.language),
        min_count=args.min_count, smoothing=args.smoothing)
    load_data_generate_ranking_run(args, DESC, method)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()

