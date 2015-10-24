# -*- coding:utf-8 -*-
import unittest
import nose
from mobileclick import Iunit, Intent, Summary, SummaryError

class SummaryTestCase(unittest.TestCase):
    def setUp(self):
        self.qid = 'MC2-E-0001'
        self.i1 = Intent(self.qid, '%s-INTENT0001' % self.qid, 'Link')
        self.i2 = Intent(self.qid, '%s-INTENT0002' % self.qid, 'Link')
        self.u1 = Iunit(self.qid, '%s-0001' % self.qid, 'A')
        self.u2 = Iunit(self.qid, '%s-0002' % self.qid, 'A')
        self.u3 = Iunit(self.qid, '%s-0003' % self.qid, 'A')
        self.u4 = Iunit(self.qid, '%s-0004' % self.qid, 'A')
        self.first = [self.u1, self.i1, self.i2]
        self.seconds = {
            self.i1.iid: [self.u2],
            self.i2.iid: [self.u3, self.u4]
            }
        self.summary = Summary(self.qid, self.first, self.seconds)

    def test_summary_init(self):
        '''
        Summary.__init__ (validation)
        '''
        self.assertRaises(SummaryError, Summary, self.qid, self.first, {})
        self.assertRaises(SummaryError, Summary, self.qid, [], self.seconds)
        self.assertRaises(SummaryError, Summary, self.qid, [1], {})
        self.assertRaises(SummaryError, Summary, self.qid, 
            [self.i1], {self.i1.iid: [self.i2]})
        self.assertRaises(SummaryError, Summary, self.qid, 
            [self.i1, self.i1], {self.i1.iid: [self.u2]})
        self.assertRaises(SummaryError, Summary, self.qid, 
            [Iunit('MC2-E-0002', '0001', 'A')])

    def test_summary_property(self):
        '''
        Summary.first and Summary.second(iid)
        '''
        self.assertEqual(self.summary.qid, self.qid)
        self.assertEqual(len(self.summary.first), 3)
        self.assertIsInstance(self.summary.first, tuple)
        self.assertEqual(self.summary.first[0].uid, 'MC2-E-0001-0001')

        iid = 'MC2-E-0001-INTENT0001'
        self.assertIsInstance(self.summary.second(iid), tuple)
        self.assertEqual(self.summary.second(iid)[0].uid, 'MC2-E-0001-0002')
        iid = 'MC2-E-0001-INTENT0002'
        self.assertEqual(self.summary.second(iid)[0].uid, 'MC2-E-0001-0003')

    def test_summary_add(self):
        '''
        Summary.add
        '''
        s = Summary(self.qid)
        s.add(self.i1)
        self.assertRaises(SummaryError, s.add, self.i1)
        s.add(self.u1)
        s.add(self.u2, self.i1.iid)
        self.assertRaises(SummaryError, s.add, self.u3, self.i2.iid)
        self.assertRaises(SummaryError, s.add, self.i2, self.i2.iid)
        s.add(self.i2)
        s.add(self.u3, self.i2.iid)
        s.add(self.u4, self.i2.iid)
        self.assertRaises(SummaryError, s.add, self.i2)
        self.assertEqual(s.first[0].iid, self.i1.iid)
        self.assertEqual(s.first[1].uid, self.u1.uid)
        self.assertEqual(s.second(self.i1.iid)[0].uid, self.u2.uid)
        self.assertEqual(s.first[2].iid, self.i2.iid)
        self.assertEqual(s.second(self.i2.iid)[0].uid, self.u3.uid)
        self.assertEqual(s.second(self.i2.iid)[1].uid, self.u4.uid)

    def test_summary_to_xml(self):
        '''
        Summary.to_xml
        '''
        from xml.etree.ElementTree import tostring
        xml = self.summary.to_xml()
        xmlstr = tostring(xml, 'utf-8')
        self.assertEqual(xmlstr, 
            '''<result qid="MC2-E-0001"><first><iunit uid="MC2-E-0001-0001" /><link iid="MC2-E-0001-INTENT0001" /><link iid="MC2-E-0001-INTENT0002" /></first><second iid="MC2-E-0001-INTENT0001"><iunit uid="MC2-E-0001-0002" /></second><second iid="MC2-E-0001-INTENT0002"><iunit uid="MC2-E-0001-0003" /><iunit uid="MC2-E-0001-0004" /></second></result>''')

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])


