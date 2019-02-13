# -*- coding: utf-8 -*-
import random
# Scrapy settings for jingdong project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jingdong'
MAX_PAGE = 3
KEYWORD = '冰箱'

SPIDER_MODULES = ['jingdong.spiders']
NEWSPIDER_MODULE = 'jingdong.spiders'

MONGO_URL = 'localhost'
MONGO_DB = 'xueqiu'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = random.choice(['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2','Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'])

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3 + random.random()  #增加延时1~2s
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
"""DEFAULT_REQUEST_HEADERS = {"Accept-Language":"zh-CN,zh;q=0.8",
      "Accept-Encoding":"gzip, deflate, sdch, br",
      "Referer":"https://search.jd.com/Search",'X-Requested-With': 'XMLHttpRequest',}
"""
#DEFAULT_REQUEST_HEADERS = {"Accept-Language":"zh-CN,zh;q=0.8",
#      "Accept-Encoding":"gzip, deflate, sdch, br",
#      "Referer":"https://list.tmall.com/search_product.htm",'X-Requested-With': 'XMLHttpRequest',}
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jingdong.middlewares.ProxyMiddleware': 555}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jingdong.middlewares.ProxyMiddleware': 543,}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jingdong.pipelines.JingdongPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXY_URL = '61.178.149.237:59042'
RETRY_HTTP_CODES = [401, 403, 408, 414, 500, 502, 503, 504]
FEED_EXPORTERS = {                                                        
    'csv': 'jingdong.spiders.csv_item_exporter.MyProjectCsvItemExporter',   
} #jingdong为工程名

FIELDS_TO_EXPORT = [                                                                                                                         
    'quote_name',                                                             
    'id',
    'report_name',                                                          
    'total_revenue',                                                                
    'asset_liab_ratio',                                                              
    'net_profit_atsopc',                                                           
    'net_profit_atsopc_yoy',                                                              
    'net_profit_after_nrgal_atsolc',
    'basic_eps',
    'np_per_share',
    'np_atsopc_nrgal_yoy',
    'capital_reserve',
    'undistri_profit_ps',
    'operate_cash_flow_ps',
    'avg_roe',
    'ore_dlt',
    'net_interest_of_total_assets',
    'rop',
    'gross_selling_rate',
    'net_selling_rate',
    'operating_income_yoy',
    'current_ratio',
    'quick_ratio',
    'equity_multiplier',
    'equity_ratio',
    'holder_equity',
    'ncf_from_oa_to_total_liab',
    'inventory_turnover_days',
    'receivable_turnover_days',
    'accounts_payable_turnover_days',
    'cash_cycle',
    'operating_cycle',
    'total_capital_turnover',
    'inventory_turnover',
    'account_receivable_turnover',
    'accounts_payable_turnover',
    'current_asset_turnover_rate',
    'fixed_asset_turnover_ratio' ,
    'report_date'
                                                          
]

#不进行ssl认证
"""
DOWNLOAD_HANDLERS_BASE = {
    'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
    'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
}
DOWNLOAD_HANDLERS = {
    'https': 'zhiyi.custom.downloader.handler.https.HttpsDownloaderIgnoreCNError',
}
"""