# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
#from jingdong.items import TmailItem
#from jingdong.items import GSJJItem

class JingdongPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db
        
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
             mongo_url = crawler.settings.get('MONGO_URL'),
             mongo_db = crawler.settings.get('MONGO_DB')
        )
    
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]
        
    def process_item(self,item,spider):
        #name = item.__class__.__name__
        if item['id']:
            name = item['id']
        else:
            name = item.__class__.__name__
        
        #if isinstance(item,TmailItem):
        """
            if item['sale_num'] :
                try:
                    item['sale_num'] = eval(item['sale_num'].replace('万笔','*10000'))
                except:
                    pass
        """
        #self.db[name].update({'id':item.get('id')},{'$set':item},True)
        self.db[name].update({'report_name':item.get('report_name')},{'$set':item},True)   
        
        return item
    
    def close_spider(self,spider):
        self.client.close()

