# -*- coding: utf-8 -*-
from .run import Run
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

class SummarizationRun(Run):
    FILENAME_TEMPLATE = '%s.xml'

    def save(self, dirpath='./'):
        '''
        Save the current results
        '''
        qids = sorted(self.results.keys())
        filepath = self._get_filepath(dirpath)
        xmlroot = Element('results')
        sysdesc = SubElement(xmlroot, 'sysdesc')
        sysdesc.text = self.desc
        for qid in qids:
            xmlroot.append(self.results[qid].to_xml())
        with open(filepath, 'w') as f:
            f.write(self._ugly_prettify(xmlroot))
        return filepath

    def _ugly_prettify(self, xml):
        '''
        Return a pretty-printed XML string for the Element.
        '''
        rough_string = tostring(xml, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
