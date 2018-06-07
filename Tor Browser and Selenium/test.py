#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/5/31 上午7:39
# @Author  : MiracleYoung
# @File    : test.py

import unittest
from time import sleep
from tbselenium.tbdriver import TorBrowserDriver


class TestSite(unittest.TestCase):
    def setUp(self):
        # Point the path to the tor-browser_en-US directory in your system
        tbpath = '/home/kdas/.local/tbb/tor-browser_en-US/'
        self.driver = TorBrowserDriver(tbpath, tbb_logfile_path='test.log')
        self.url = "https://check.torproject.org"

    def tearDown(self):
        # We want the browser to close at the end of each test.
        self.driver.close()

    def test_available(self):
        self.driver.load_url(self.url)
        # Find the element for success
        element = self.driver.find_element_by_class_name('on')
        self.assertEqual(str.strip(element.text),
                         "Congratulations. This browser is configured to use Tor.")
        sleep(2)  # So that we can see the page


if __name__ == '__main__':
    unittest.main()