import scrapy
from scrapy.loader import ItemLoader

# from ..pipelines import MySQLStorePipeline
from ..pipelines import MysqlPipeline
from ..items import QuotesItem
from ..items import CoreyMSItem
from bs4 import BeautifulSoup


class QuotesSpider(scrapy.Spider):
    name = "coreyms"

    def start_requests(self):
        urls = [
            'https://coreyms.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        soup = BeautifulSoup(response.text, 'lxml')

        for article in soup.find_all('article'):
            summary = article.find('div', class_='entry-content').p.text
            try:
                vid_src = article.find('iframe', class_='youtube-player')['src']
                vid_id = vid_src.split('/')[4]
                vid_id_orig = vid_id[4].split('?')[0]
                youtube_link = f'https://www.youtube.com/watch?v={vid_id_orig}'
            except:
                youtube_link = None

            item = CoreyMSItem()
            item ['summary'] = summary
            item['link'] = youtube_link
            print(item)
            yield item


