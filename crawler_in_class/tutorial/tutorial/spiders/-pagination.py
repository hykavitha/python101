# import scrapy
# from ..items import MyItem
#
#
# class MySpider(scrapy.Spider):
#     name = 'example'
#     allowed_domains = ['example.com']
#
#     def start_requests(self):
#         yield scrapy.Request('http://www.example.com/1.html', self.parse_item)
#         yield scrapy.Request('http://www.example.com/2.html', self.parse_item)
#         yield scrapy.Request('http://www.example.com/3.html', self.parse_item)
#
#     def parse_item(self, response):
#         self.logger.info('Hi, this is an item page! %s', response.url)
#         item = scrapy.Item()
#         item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
#         item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
#         item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
#         item['link_text'] = response.meta['link_text']
#         return item
#
#
#     # def parse(self, response):
#     #     for h3 in response.xpath('//h3').getall():
#     #         yield MyItem(title=h3)
#     #
#     #     for href in response.xpath('//a/@href').getall():
#     #         yield scrapy.Request(response.urljoin(href), self.parse)