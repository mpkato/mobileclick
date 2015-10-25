# -*- coding: utf-8 -*-
import re
class Measurable(object):
    SYMBOLS = re.compile(ur'''[ !"#$%&'()*+,\-.\/:;<=>?@\[\\\]\^_`{|}~｡｢｣､ｰﾞﾟ･　！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿‘｛｜｝￣、。・゛゜´｀¨ヽヾゝゞ〃仝々〆〇ー―‐＼～〜∥…‥“〔〕〈〉《》「」『』【】±×÷≠≦≧∞∴♂♀°′″℃￠￡§☆★○●◎◇◇◆□■△▲▽▼※〒→←↑↓〓]|[\u2570-\u25ff]|[　−-]''')

    @property
    def len(self):
        '''
        Return the number of words that are not symbols defined here
        '''

        return len([w for w in list(self._to_unicode(self.body))
            if self.SYMBOLS.match(w) is None])

    def _to_unicode(self, s):
        return s if isinstance(s, unicode) else s.decode('utf-8')
