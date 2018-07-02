#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Data Science for Scientists ATL'
SITENAME = 'Data Science For Scientists ATL'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Our Github org page',
		  'https://github.com/Data-Science-for-Scientists-ATL'),
         ('Atlanta BEST program (original sponsor)',
          'http://best.emory.edu/index.html'),
         ('PyData Atlanta',
          'https://www.meetup.com/PyData-Atlanta/'),
         ('Atlanta Jupyter Users Group',
          'https://www.meetup.com/Atlanta-Jupyter-User-Group/'),
        )

# Social widget
SOCIAL = (('@DataSci4ScienceATL', 'https://twitter.com/datasci4sciATL?lang=en'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# tell pelican-bootstrap3 theme where to find our header and avatar
STATIC_PATHS = ['images']
BANNER = "images/header.jpg"
AVATAR = "images/avatar.jpg"

# below because pelican-bootstrap3 theme expects i18n plugin
PLUGIN_PATHS = ['./plugins/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# for using bootswatch themes, as explained in theme README
THEME = './themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'

# constants that add info to posts like author and date modified
SHOW_ARTICLE_AUTHOR = True