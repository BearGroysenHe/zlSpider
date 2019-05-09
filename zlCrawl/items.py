# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class ZlcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    degree_requirement = scrapy.Field()
    work_experence_requirement = scrapy.Field()
    welfare = scrapy.Field()
