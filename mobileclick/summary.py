# -*- coding: utf-8 -*-
from .iunit import Iunit
from .intent import Intent
from .summary_error import SummaryError
from xml.etree.ElementTree import Element, SubElement

class Summary(object):
    '''
    Result for each query that consists of two layers
    '''
    def __init__(self, qid, first=None, seconds=None):
        '''
        qid: Query ID (e.g. MC2-E-0001)
        first: a list of Iunit or Intent
        seconds: a dict of {intent ID: [Iunit]}
        '''
        self.qid = qid
        if first is not None:
            self._first = first
        else:
            self._first = []
        if seconds is not None:
            self._seconds = seconds
        else:
            self._seconds = {}
        self._validation()

    @property
    def first(self):
        return tuple(self._first)

    def second(self, iid):
        return tuple(self._seconds[iid])

    def add(self, elem, iid=None):
        '''
        Add Iunit to either the first layer,
        or second layer by specifying intent ID (iid).
        Only Iunit can be added to the second layer
        after adding an Intent for the second layer.
        '''
        if isinstance(elem, Iunit):
            if iid is None:
                self._first.append(elem)
            else:
                if not iid in self._seconds:
                    raise SummaryError("Intent %s must be added first" % iid)
                self._seconds[iid].append(elem)
        else:
            if iid is not None:
                raise SummaryError("iid must be None when adding Intent")
            if elem.iid in self._seconds:
                raise SummaryError("Intent %s has already been added" % elem.iid)
            self._first.append(elem)
            self._seconds[elem.iid] = []

    def to_xml(self):
        '''
        Convert self to XML
        '''
        result = Element('result', qid=self.qid)
        first = SubElement(result, 'first')
        for elem in self._first:
            first.append(elem.to_xml())
        for iid in sorted(self._seconds.keys()):
            iunits = self._seconds[iid]
            second = SubElement(result, 'second', iid=iid)
            for iunit in iunits:
                second.append(iunit.to_xml())
        return result

    def _validation(self):
        '''
        Validation to ensure the format is valid
        '''
        # The first layer consists of only Iunit or Intent
        if not all([isinstance(elem, Iunit) or isinstance(elem, Intent) 
            for elem in self._first]):
            raise SummaryError("The first layer must consist of only Iunit or Intent")
        # The second layer consists of only Iunit
        for second in self._seconds.values():
            if not all([isinstance(elem, Iunit) for elem in second]):
                raise SummaryError("The second layer must consist of only Iunit")
        # The second layer exists for each Intent
        if not all([elem.iid in self._seconds for elem in self._first
            if isinstance(elem, Intent)]):
            raise SummaryError("The second layer must exist for each Intent")
        # A link exists for each second layer
        first_iids = set([elem.iid for elem in self._first
            if isinstance(elem, Intent)])
        if not all([iid in first_iids for iid in self._seconds]):
            raise SummaryError("A link must exist for each second layer")
        # Duplicate Intent is not allowed
        if len(first_iids) != len([elem.iid for elem in self._first
            if isinstance(elem, Intent)]):
            raise SummaryError("Duplicate Intent is not allowed")
        # All the elements belong to qid
        if not all([elem.qid == self.qid for elem in self._first])\
            or not all([all([elem.qid == self.qid for elem in second])
                for second in self._seconds.values()]):
            raise SummaryError(
                "All the elements must belong to qid %s" % self.qid)
