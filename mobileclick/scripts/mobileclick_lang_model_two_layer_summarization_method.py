# -*- coding:utf-8 -*-

def main(argv=None):
    from mobileclick.methods import LangModelTwoLayerSummarizationMethod
    from .scriptutils import (summarization_parser, get_parser,
        get_length_limit,
        load_data_generate_summarization_run, add_lang_model_params)
    DESC = 'A LM-based two-layer baseline for the iUnit summarization subtask.'

    parser = summarization_parser(prog="mobileclick_lang_model_two_layer_summarization_method", desc=DESC)
    parser = add_lang_model_params(parser)
    parser.add_argument('--length_limit',
        help='Length limit for each layer (default: 420 for English and 280 for Japanese)')
    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    # set the length limit
    length_limit = args.length_limit
    if length_limit is None:
        length_limit = get_length_limit(args.language)

    method = LangModelTwoLayerSummarizationMethod(get_parser(args.language),
        length_limit,
        min_count=args.min_count, smoothing=args.smoothing)
    load_data_generate_summarization_run(args, DESC, method)

if __name__ == '__main__':
    import sys
    sys.path.append('./')
    main()
