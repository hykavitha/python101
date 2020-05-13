import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'


    def start_requests(self):
        yield scrapy.Request('http://www.example.com/categories/%s' % self.category)