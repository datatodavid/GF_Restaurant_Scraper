# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindMeGFItem(scrapy.Item):
    # define the fields for your item here like:
    page_url = scrapy.Field()
    name = scrapy.Field()
    avg_rating = scrapy.Field()
    num_ratings = scrapy.Field()
    num_reviews = scrapy.Field()
    how_expensive = scrapy.Field()
    # perc_celiac_friendly = scrapy.Field()
    total_celiac_friendly = scrapy.Field()
    total_not_celiac_friendly = scrapy.Field()
    total_reviewers_celiac = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zipcode = scrapy.Field()
    phone = scrapy.Field()
    business_url = scrapy.Field()
    gf_features = scrapy.Field()
    dedicated_gf = scrapy.Field()
    dedicated_fryer = scrapy.Field()
    gf_menu = scrapy.Field()
    categories = scrapy.Field()
    reviewer_name = scrapy.Field()
    review_rating = scrapy.Field()
    review_text = scrapy.Field()
 