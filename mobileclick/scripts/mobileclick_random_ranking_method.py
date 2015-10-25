# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import RandomRankingMethod
    from .scriptutils import ranking_parser, load_data_generate_ranking_run
    DESC = 'A random baseline for the iUnit ranking subtask.'

    parser = ranking_parser(prog="mobileclick_random_ranking_method", desc=DESC)
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    method = RandomRankingMethod()
    load_data_generate_ranking_run(args, DESC, method)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()
