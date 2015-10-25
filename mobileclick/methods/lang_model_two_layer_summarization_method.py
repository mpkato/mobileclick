# -*- coding: utf-8 -*-
from ..summary import Summary
from .base_summarization_method import BaseSummarizationMethod
from .lang_model_ranking_method import LangModelRankingMethod

class LangModelTwoLayerSummarizationMethod(BaseSummarizationMethod):
    '''
    Rank iUnits based on the LM-based method used in iUnit ranking,
    put the top-ranked iUnits in the first layer,
    and put lower-ranked iUnits in the second layer relevant to them.
    Considered as a baseline method.

    The first layer and second layer are filled until the length of iUnits
    exceed the length limit.

    For each second layer, this baseline method utilizes the score below:

        Score(u, i) = OR(u) * Sim(u, i)

    where OR(u) is the odd ratio used in the LM-based method,
    and Sim(u, i) is asymmetric similarity between u and i,
    i.e.

        Sim(u, i) = |W_u \cap W_i| / |W_i|

    where W_x is a set of words contained in x.
    iUnits that are not used in the first layer are put in the second layer
    based on Score(u, i)

    All the intents are used as links in the order in the intent file.
    '''

    SMALL_VALUE = 1e-5

    def __init__(self, parser, length_limit, min_count=3, smoothing=1):
        '''
        parser: must have "word_tokenize" method
        min_count: minumum frequncy for words to be used
        smoothing: added to the frequency of each word for smoothing
        '''
        self.ranking = LangModelRankingMethod(parser, min_count, smoothing)
        self.length_limit = length_limit

    def init(self, tasks):
        '''
        Count the frequency of words
        '''
        # duplicate message
        #print "Initializing ..."
        self.ranking.init(tasks)

    def summarize(self, task):
        '''
        Rank iUnits based on the LM-based method used in iUnit ranking,
        put the top-ranked iUnits in the first layer,
        and put lower-ranked iUnits in the second layer relevant to them.
        '''
        # duplicate message
        #print "Processing %s" % task.query.qid
        # get odd ratio
        iunit_score_list = self.ranking.rank(task)
        # add all the intents
        intents = task.intents
        limit = self.length_limit - sum([i.len for i in intents])
        first = list(intents)
        # add iUnits at the top of the first layer
        first_iunits = self._put_in_until_limit(iunit_score_list, limit)
        first = first_iunits + first
        # add iUnits in teh second layer
        remaining_iunit_score_list = filter(lambda x: not x[0] in first_iunits,
            iunit_score_list)
        seconds = {}
        for intent in intents:
            iunit_score_list_for_second = self._score_for_second(
                intent, remaining_iunit_score_list)
            seconds[intent.iid] = self._put_in_until_limit(
                iunit_score_list_for_second, self.length_limit)

        return Summary(task.query.qid, first, seconds)

    def _score_for_second(self, intent, iunit_score_list):
        '''
        Given intent i,
        return [(u, Score(u, i))] where Score(u, i) = OR(u) * Sim(u, i)
        '''
        return [(iunit, score * self._asym_similarity(iunit, intent))
            for iunit, score in iunit_score_list]

    def _put_in_until_limit(self, iunit_score_list, limit):
        '''
        Select iUnits until the total length exceeds the limit.
        '''
        sorted_list = sorted(iunit_score_list, key=lambda x: x[1], reverse=True)
        result = []
        total_length = 0
        for iunit, _ in sorted_list:
            total_length += iunit.len
            if total_length > limit:
                break
            result.append(iunit)
        return result

    def _asym_similarity(self, iunit, intent):
        '''
        Sim(u, i) is asymmetric similarity between u and i, i.e.
            Sim(u, i) = |W_u \cap W_i| / |W_i|
        where W_x is a set of words contained in x.

        To avoid giving all the iUnits 0, SMALL_VALUE is returned 
        if there is no overlap between the iUnit and intent.
        '''
        uwords = set(self.ranking.parser.word_tokenize(iunit.body))
        iwords = set(self.ranking.parser.word_tokenize(intent.body))
        if len(iwords) == 0:
            return 1.0 # the same score for all the iUnits
        else:
            overlap = float(len(uwords & iwords))
            if overlap == 0:
                overlap = self.SMALL_VALUE
            return overlap / len(iwords)
