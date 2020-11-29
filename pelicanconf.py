#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pelican_jupyter import markup as nb_markup
import yaml


AUTHOR = 'Nick Hamlin'
SITENAME = "Nick Hamlin"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# No need to set categories manually
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'random'

# Use "garden" instead of the default "categories" 
CATEGORY_URL = 'garden/{slug}'
CATEGORIES_SAVE_AS = 'garden.html'
CATEGORY_SAVE_AS = 'garden/{slug}.html'
DIRECT_TEMPLATES = ['categories','index','archives']

# It's just me writing stuff, no need for author page
AUTHOR_SAVE_AS = ''

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./theme"

MARKUP = ('md','ipynb')

PLUGINS = [nb_markup]
IPYNB_MARKUP_USE_FIRST_CELL = True
IGNORE_FILES = ['.ipynb_checkpoints']

# Load custom YAML content for various pages
# with open('./content/projects.yml','r') as project_yml:
#     PROJECTS = yaml.load(project_yml, Loader=yaml.FullLoader)

with open('./content/testimonials.yml','r') as testimonial_yml:
    TESTIMONIALS = yaml.load(testimonial_yml, Loader=yaml.FullLoader)
