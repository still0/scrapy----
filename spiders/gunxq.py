# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from jingdong.items import GSJJItem
import csv

class GunxqSpider(Spider):
    name = 'gunxq'
    #allowed_domains = ['xueqiu.com/snowman/S']
    #start_urls = ['http://xueqiu.com/snowman/S/']
    def start_requests(self):
        
        base_url = 'https://stock.xueqiu.com/v5/stock/f10/cn/company.json?symbol=??' 
        headers ={}
        headers['Host'] = 'stock.xueqiu.com'
        headers['Origin'] = 'https://xueqiu.com'
        headers['Referer'] = 'https://xueqiu.com/snowman/S/'
        cookie = 'device_id=a775585a22aecdf2ca1dda2792d46f0a; s=e711pj1dik; xq_a_token=663059f1a494115c0dfac8bc11acf01c72ca2407; xq_a_token.sig=dnGkJ3pgM6zGvDwI8aPmcRuWcjk; xq_r_token=d6cf388d8a883c161910ce23151c244332e73959; xq_r_token.sig=eqyxteFffPXoFVmB8uAIMgtmh9Q; u=561545464733363; _gat_gtag_UA_16079156_4=1; Hm_lvt_1db88642e346389874251b5a1eded6e3=1544355526,1545464733; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1545465823; _ga=GA1.2.139151440.1544355527; _gid=GA1.2.1120827421.1545464733'
        cookies = {}
        for i in cookie.replace(' ','').split(";"):
            j0 = i.split("=")[0]
            j1 = i.split("=")[1]
            cookies[j0] = j1
        with open('stocklist.csv','r',newline = '') as f:
            reader = csv.reader(f)
            self.gupiaoids = [row[0] for row in reader]
            for self.gupiaoid in self.gupiaoids:
                url = base_url.replace('??',self.gupiaoid)                
                request = Request(url=url,headers = headers,cookies = cookies,callback = self.parse)
                request.meta['gupiaoid'] = self.gupiaoid
                yield request
            
        
       
        
        

    def parse(self, response):
        result = json.loads(response.text)
        GSJJ = result.get('data').get('company')
        item = GSJJItem()
        itemlist = ['org_name_cn','pre_name_cn','provincial_name',\
                        'actual_controller','classi_name','main_operation_business',\
                        'org_cn_introduction','chairman','legal_representative'\
                        ,'general_manager','secretary','established_date','reg_asset'\
                        ,'staff_num','executives_nums','listed_date','actual_issue_vol'\
                        ,'issue_price','actual_rc_net_amt','pe_after_issuing',
                        'online_success_rate_of_issue','telephone','postcode',\
                        'fax','email','org_website','reg_address_cn','office_address_cn']
        item['id'] = response.meta['gupiaoid']
        for item_em in itemlist:
            try:                    
                item[item_em] = GSJJ.get(item_em)
            except:
                pass
        self.logger.debug(item)
        yield item
        pass
