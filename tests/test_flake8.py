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

        flake8style = engine.get_style_guide(
            ignore=['E501'], 
            max_complexity=6
        )

        directory = 'flask_rollbar'
        self.assertEqual(os.path.isdir(directory), True,
                         "Invalid test directory '%s'. You need to update test_flake8.py" % directory)

        # Get all the files to check
        files = []
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in [f for f in filenames if f.endswith(".py")]:
                files +=  [os.path.join(dirpath, filename)]
                
        result = flake8style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Code found to be too complex or failing PEP8")

if __name__ == '__main__':
    unittest.main()
