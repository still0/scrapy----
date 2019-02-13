# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
#from urllib.parse import quote
from jingdong.items import JingdongItem



class JingdongSpider(Spider):
    name = 'jd'
    
    #allowed_domains = ['search.jd.com/s_new.php']
    #start_urls = ['http://search.jd.com/s_new.php/']
    
    
    def start_requests(self):
        data = {'enc': 'utf-8', 'psort': '3'}
        self.keyword = self.settings.get('KEYWORD') #settings.attributes[name]
        
        #self.logger.debug(self.keyword)
        
        data['keyword'] = self.keyword
        data['wq'] = self.keyword
        base_url = 'https://search.jd.com/s_new.php?'
        
        
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['page'] = page
            params = urlencode(data)
            url = base_url + params
            request = Request(url,self.parse)
            request.meta['keyword'] = self.keyword
            yield request
            
        pass

    def parse(self, response):
        goods = response.css('ul li.gl-item')
        #self.logger.debug(goods.extract())
        item = JingdongItem()
        for good in goods:
            item['keyword'] = response.meta['keyword']
            item['id'] = good.xpath('@data-sku').extract_first()
            item['price'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-price"]/strong/i/text()').extract_first()
            item['title'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-name p-name-type-2"]/a/em/text()').extract_first()
            item['promo_words'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-name p-name-type-2"]/a/i/text()').extract_first()
            item['href'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-img"]/a/@href').extract_first()
            item['comment_num'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-commit"]/strong/a/text()').extract_first()
            item['shop'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-shop"]/span/a/text()').extract_first()
            item['img'] = good.xpath('div[@class = "gl-i-wrap"]/div[@class = "p-img"]/a/img/@source-data-lazy-img').extract_first()
            yield item
            
    
        
        
        pass
