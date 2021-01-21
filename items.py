# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy

class FindMeGFItem(scrapy.Item):
    page_url = scrapy.Field()
    name = scrapy.Field()
    avg_rating = scrapy.Field()
    num_ratings = scrapy.Field()
    num_reviews = scrapy.Field()
    how_expensive = scrapy.Field()
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
 