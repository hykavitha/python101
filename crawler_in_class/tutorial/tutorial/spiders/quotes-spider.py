import scrapy
from scrapy.loader import ItemLoader

# from ..pipelines import MySQLStorePipeline
from ..pipelines import MysqlPipeline
from ..items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        for quote in response.css("div.quote"):
            item = QuotesItem()

            item['text'] = quote.css("span.text::text").get()
            item['author'] = quote.css("small.author::text").get()
            item['tags'] = quote.css("div.tags a.tag::text").getall()
            item['last_upd_time'] = '2020-05-12 19:54:00'
            print(item)
            yield item

    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         item = {} #MySQLStorePipeline()
    #         # l = ItemLoader(item=MySQLStorePipeline(), selector=quote)
    #         # l.add_css('text', "span.text::text")
    #         # print("After parsing -->", l)
    #          item ['text'] = quote.css("span.text::text").get()
    #          item['author'] = quote.css("small.author::text").get()
    #          item['tags'] = quote.css("div.tags a.tag::text").getall()
    #         yield item
    #
    #     #return items
