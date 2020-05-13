# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
import sys
# import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

import mysql.connector

from datetime import date, datetime, timedelta


class CoreyMSItem(scrapy.Item):
    link = scrapy.Field()
    summary = scrapy.Field()


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    last_upd_time = scrapy.Field()

class TechCrunchItem(scrapy.Item):
    title = scrapy.Field()
    pubDate = scrapy.Field()
    link = scrapy.Field()



class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()


class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
