# -*- coding: utf8 -*-
from __future__ import unicode_literals
import unittest

import os
import sys

from flake8.api import legacy as engine

if sys.version_info[0] == 3:
    unicode = str

if sys.version_info[:2] == (2, 6):
    # Monkeypatch to make tests work on 2.6
    def assert_less(first, second, msg=None):
        assert first > second
    unittest.TestCase.assertLess = assert_less


class TestCodeComplexity(unittest.TestCase):
    def test_flake8_conformance(self):

        flake8style = engine.get_style_guide(max_complexity=6)
        flake8style.options.ignore = flake8style.options.ignore + tuple(['E501'])

        directory = 'flask_rollbar'
        self.assertEqual(os.path.isdir(directory), True,
                         "Invalid test directory '%s'. You need to update test_flake8.py" % directory)

        result = flake8style.check_files(directory)
        self.assertEqual(result.total_errors, 0,
                         "Code found to be too complex or failing PEP8")

if __name__ == '__main__':
    unittest.main()
