# -*- coding: utf8 -*-
from __future__ import unicode_literals
import unittest

import os
import sys

import pep8

if sys.version_info[0] == 3:
    unicode = str

if sys.version_info[:2] == (2, 6):
    # Monkeypatch to make tests work on 2.6
    def assert_less(first, second, msg=None):
        assert first > second
    unittest.TestCase.assertLess = assert_less


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):

        pep8style = pep8.StyleGuide(quiet=True)
        pep8style.options.ignore = pep8style.options.ignore + tuple(['E501'])

        directory = 'flask_rollbar'
        self.assertEqual(os.path.isdir(directory), True,
                         "Invalid test directory '%s'. You need to update test_pep8.py" % directory)

        pep8style.input_dir(directory)
        result = pep8style.check_files()

        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
