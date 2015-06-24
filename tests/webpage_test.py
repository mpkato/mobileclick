# -*- coding:utf-8 -*-
import unittest
import nose

class PageTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_page(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    nose.main(argv=['nose', '-v'])
