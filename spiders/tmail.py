# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
#from urllib.parse import quote
from jingdong.items import TmailItem

class TmailSpider(Spider):
    name = 'tmail'
    #allowed_domains = ['list.tmall.com/search_product.htm']
    #start_urls = ['http://list.tmall.com/search_product.htm/']

    def start_requests(self):
        data = {'type': 'pc', 'sort': 'd','from' : 'mallfp..pc_1_searchbutton'}
        self.keyword = self.settings.get('KEYWORD') #settings.attributes[name]
        
        #self.logger.debug(self.keyword)
        
        data['q'] = self.keyword
        base_url = 'http://list.tmall.com/search_product.htm?'
        
        
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['s'] = page * 60- 60
            params = urlencode(data)
            url = base_url + params
            cookie = 'cna=tdfsEi1ekEgCAbc1rjtPAV/2; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; enc=WFArPUY9Mp%2FS4OgkMjxzOvadPOee6qSxPJbt7nPAIEI3lAOFw6UXIFnO7zhVysC5flqYM2iPQXH5fdaAX6Qu%2BQ%3D%3D; _uab_collina=154433847152725792392235; hng=CN%7Czh-CN%7CCNY%7C156; t=2d167cd8a1a6525701a48458e1a40d9b; tracknick=jd_67670a0746a95; _tb_token_=3eee7e136b33; cookie2=11b9b8b3d482cb4ad19fa22fffc83574; tt=tmall-main; res=scroll%3A1903*5940-client%3A1903*921-offset%3A1903*5940-screen%3A1920*1080; pnm_cku822=098%23E1hvWQvUvbpvjQCkvvvvvjiPR2FyljiWn2cOljnEPmPwsj1nRL5U6jtEnLqW0jGtvpvhvvvvvvGCvvLMMQvvmphvLvLwc9vjwYcEKOmAdch%2BYExr18TxO90U%2B8c6eCDzpWmQ0f06WeCpqU0HsfUpwZFIAXcBKFyK2ixr1nAK5kx%2F1n1ldChTWDKtkbmD53etvpvIvvvvvhCvvvvvvUnvphvWX9vv96CvpC29vvm2phCvhhvvvUnvphvppUyCvvOUvvVvaZmivpvUvvmv%2BM4Y1%2FgCvpvVvvpvvhCviQhvCvvv9UU%3D; cq=ccp%3D1; _m_h5_tk=09c60a13e7550acd43ebd85a62164d17_1544961536197; _m_h5_tk_enc=a785b44ae07182a7d94e54b520523edc; tk_trace=1; isg=BHFxIfgxiRbiWyNj1KoHlOTugP3L9uS5bZWaG1OGSzhXepPMk61yoELYmE65sn0I'
            cookies = {}
            for i in cookie.replace(' ','').split(";"):
                j0 = i.split("=")[0]
                j1 = i.split("=")[1]
                cookies[j0] = j1
    
            request = Request(url=url,cookies = cookies,callback = self.parse)
            request.meta['keyword'] = self.keyword
            
            yield request
            
        pass

    def parse(self, response):
        #self.logger.debug(response.body[:2000])
        goods = response.css('#content div#J_ItemList div.product')
        #self.logger.debug(goods.extract())
        item = TmailItem()
        for good in goods:
            #self.logger.debug(good.extract())
            item['keyword'] = response.meta['keyword']
            item['id'] = good.xpath('@data-id').extract_first()
            item['price'] = good.css('div.product-iWrap p.productPrice em::text').extract_first()
            #item['price'] = good.xpath('div[@class = product-iWrap]/p[@class = productPrice]/em/text()').extract_first()
            item['title'] = good.css('div.product-iWrap .productTitle a::text').extract_first()
            try:
                item['promo_words'] = good.css('div.product-iWrap a.nth-child(2)::text').extract_first()
            except :
                pass
            
            
            
            item['href'] = good.css('div.product-iWrap div.productImg-wrap a.productImg::attr(href)').extract_first()
            #self.logger.debug(item['href'])
            item['sale_num'] = good.css('div.product-iWrap p.productStatus em::text').extract_first()
            item['shop'] = good.css('div.product-iWrap a.productShop-name::text').extract_first()
            item['img'] = good.css('div.product-iWrap img::attr(src)').extract_first()
            item['img_small'] = good.css('div.product-iWrap img::attr(data-ks-lazyload)').extract()
            self.logger.debug(item)
            
            yield item
            