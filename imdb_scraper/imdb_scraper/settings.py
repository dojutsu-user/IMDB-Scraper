# -*- coding: utf-8 -*-

BOT_NAME = 'imdb_scraper'

SPIDER_MODULES = ['imdb_scraper.spiders']
NEWSPIDER_MODULE = 'imdb_scraper.spiders'

# Saving the output in json format
FEED_URI = 'data/%(name)s.json'
FEED_FORMAT = 'json'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
