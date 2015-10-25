# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import RandomSummarizationMethod
    from .scriptutils import summarization_parser, load_data_generate_summarization_run
    DESC = 'A random baseline for the iUnit summarization subtask.'

    parser = summarization_parser(prog="mobileclick_random_summarization_method", desc=DESC)
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    method = RandomSummarizationMethod()
    load_data_generate_summarization_run(args, DESC, method)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()
