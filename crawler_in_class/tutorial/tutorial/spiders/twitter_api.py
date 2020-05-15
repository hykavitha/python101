# -*- coding: utf-8 -*-
import scrapy


class TwitterApiSpider(scrapy.Spider):
    name = 'twitter-api'
    allowed_domains = ['twitter.com']
    start_urls = ['http://twitter.com/']

    def __init__(self, query='', lang='', crawl_user=False, top_tweet=False):
        self.query = query
        self.url = "https://twitter.com/i/search/timeline?l={}".format(lang)

        if not top_tweet:
            self.url = self.url + "&f=tweets"

        self.url = self.url + "&q=%s&src=typed&max_position=%s"

        self.crawl_user = crawl_user


    def parse(self, response):
        pass
