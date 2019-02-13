# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import json
from jingdong.items import ZYZBItem
import csv
import time

class GunxqzyzbSpider(Spider):
    name = 'gunxqzyzb'
    #allowed_domains = ['stock.xueqiu.com/v5/stock/finance/cn/indicator.json']
    #start_urls = ['http://stock.xueqiu.com/v5/stock/finance/cn/indicator.json/']
    def start_requests(self):
        self.itemlist = ['avg_roe', 'np_per_share', 'operate_cash_flow_ps', 'basic_eps', 'capital_reserve', 'undistri_profit_ps', 'net_interest_of_total_assets', 'net_selling_rate', 'gross_selling_rate', 'total_revenue', 'operating_income_yoy', 'net_profit_atsopc', 'net_profit_atsopc_yoy', 'net_profit_after_nrgal_atsolc', 'np_atsopc_nrgal_yoy', 'ore_dlt', 'rop', 'asset_liab_ratio', 'current_ratio', 'quick_ratio', 'equity_multiplier', 'equity_ratio', 'holder_equity', 'ncf_from_oa_to_total_liab', 'inventory_turnover_days', 'receivable_turnover_days', 'accounts_payable_turnover_days', 'cash_cycle', 'operating_cycle', 'total_capital_turnover', 'inventory_turnover', 'account_receivable_turnover', 'accounts_payable_turnover', 'current_asset_turnover_rate', 'fixed_asset_turnover_ratio']
        base_url = 'https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol=??&type=all&is_detail=true&count=100' 
        headers ={}
        headers['Host'] = 'stock.xueqiu.com'
        headers['Origin'] = 'https://xueqiu.com'
        headers['Referer'] = 'https://xueqiu.com/snowman/S/'
        cookie = 'device_id=a775585a22aecdf2ca1dda2792d46f0a; s=e711pj1dik; xq_a_token=663059f1a494115c0dfac8bc11acf01c72ca2407; xq_a_token.sig=dnGkJ3pgM6zGvDwI8aPmcRuWcjk; xq_r_token=d6cf388d8a883c161910ce23151c244332e73959; xq_r_token.sig=eqyxteFffPXoFVmB8uAIMgtmh9Q; u=561545464733363; _gat_gtag_UA_16079156_4=1; _ga=GA1.2.139151440.1544355527; _gid=GA1.2.1120827421.1545464733; Hm_lvt_1db88642e346389874251b5a1eded6e3=1544355526,1545464733; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1545479801'
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
        quote_name = result.get('data').get('quote_name')
        ZYZB = result.get('data').get('list')
        item = ZYZBItem()
        item['id'] = response.meta['gupiaoid']
        item['quote_name'] = quote_name
        for ZYZB_em in ZYZB:        
            item['report_date'] = ZYZB_em.get('report_date')
            item['report_name'] = ZYZB_em.get('report_name')
            try:
                timeArray = time.localtime(int(item['report_date'])/1000)
                item['report_date'] = time.strftime("%Y-%m-%d", timeArray)
            except:
                pass            
            
            for item_em in self.itemlist:
                try:                    
                    item[item_em] = ZYZB_em.get(item_em)
                except:
                    pass
            #self.logger.debug(item)
            yield item
        pass
