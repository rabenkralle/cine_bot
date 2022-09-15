# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
import hashlib
import os
from scrapy.utils.python import to_bytes

class CineparcerPipeline:
    
    def __init__(self):
        client = MongoClient('192.168.20.51', 27017)
        self.mongo_base = client.cinedb

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
        
class CinepacerPhotoPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photo']:
            try:
                yield scrapy.Request(item['photo'], meta={'item': item}) #Для создания папок по имени фильма, собираем meta
            except Exception as e:
                print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photo'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None): #Создаем папки
        item = request.meta['item']         #Используя meta, вытаскиваем данные item
        name = item['movie_title']
        url = request.url
        media_guid = hashlib.sha1(to_bytes(url)).hexdigest()       #Формируем название файла фотографии
        media_ext = os.path.splitext(url)[1]
        return f'full/{name}/%s%s' % (media_guid, media_ext)