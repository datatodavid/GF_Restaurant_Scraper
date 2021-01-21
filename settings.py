# -*- coding: utf-8 -*-

# Scrapy settings for findmegf_long project

BOT_NAME = 'findmegf_long'

SPIDER_MODULES = ['findmegf_long.spiders']
NEWSPIDER_MODULE = 'findmegf_long.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2

# Configure item pipelines
ITEM_PIPELINES = {
   'findmegf_long.pipelines.WriteItemPipeline': 300,
}
