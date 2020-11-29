#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False


CATEGORY_URL = 'garden-category/{slug}'
CATEGORIES_SAVE_AS = 'garden'
ARCHIVES_SAVE_AS = "archives"
INDEX_SAVE_AS = "index"
ARTICLE_SAVE_AS = "{category}/{slug}"
CATEGORY_SAVE_AS = 'garden-category/{slug}'
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{category}/{slug}"


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
