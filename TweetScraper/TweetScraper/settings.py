# -*- coding: utf-8 -*-

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'TweetScraper'
USER_AGENT = 'https://github.com/hykavitha'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'
DOWNLOAD_HANDLERS = {'s3': None,} # from http://stackoverflow.com/a/31233576/2297751, TODO

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'

ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToFilePipeline':100,
    #'TweetScraper.pipelines.SavetoMySQLPipeline':100, # replace `SaveToFilePipeline` with this to use MySQL
}

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'

#settings for mysql
MYSQL_SERVER = "127.0.0.1"
MYSQL_DB     = "web_scraping"
MYSQL_TABLE  = "twitter_scraper" # the table will be created automatically
MYSQL_USER   = "kavitha"        # MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_PWD    = "root123"        # MySQL user's password
