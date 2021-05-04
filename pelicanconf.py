#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ryan Travis'
SITENAME = 'Blessed Hammer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Used to convert jupyter notebooks to markdown
MARKUP = ('md', 'ipynb')
from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]
IGNORE_FILES = [".ipynb_checkpoints"]
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()#(('Pelican', 'https://getpelican.com/'),
        #  ('Python.org', 'https://www.python.org/'),
        #  ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
        #  ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/rtravis89'),
          ('linkedin', 'https://www.linkedin.com/in/rtravis89/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True