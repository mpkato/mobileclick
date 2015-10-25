# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import LangModelSummarizationMethod
    from .scriptutils import (summarization_parser, get_parser,
        load_data_generate_summarization_run, add_lang_model_params)
    DESC = 'A LM-based baseline for the iUnit summarization subtask.'

    parser = summarization_parser(prog="mobileclick_lang_model_summarization_method", desc=DESC)
    parser = add_lang_model_params(parser)
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    method = LangModelSummarizationMethod(get_parser(args.language),
        min_count=args.min_count, smoothing=args.smoothing)
    load_data_generate_summarization_run(args, DESC, method)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()
