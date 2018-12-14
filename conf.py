#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from misc.cyverse_sphinx_conf import *  # noqa

project = 'OSG-RMTA'
copyright = '2018, CyVerse'
author = 'CyVerse'
version = 'v 2.1'
release = 'v 2.1'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
exclude_patterns = ['README.md', 'License.md', 'Contributors_maintainers.md']
