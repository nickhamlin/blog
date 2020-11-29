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

# Strip HTML extensions because S3...
ARCHIVES_SAVE_AS = "archives"
INDEX_SAVE_AS = "index"

# Garden-category must be separate since /garden is now a file, not a directory
CATEGORY_URL = 'garden-category/{slug}'
CATEGORY_SAVE_AS = 'garden-category/{slug}'
CATEGORIES_SAVE_AS = 'garden'

ARTICLE_SAVE_AS = "{slug}"
ARTICLE_URL = "{slug}"


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
