# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import logging

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE

class DouyuImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 发送每个图片的请求，响应数据自动保存在 settings.py 的 IMAGES_STORE字段对应的路径里
        yield scrapy.Request(item['image_src'])


    def item_completed(self, results, item, info):
        # print("---" * 30)
        # print(results)


        old_name = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]
        new_name = IMAGES_STORE + item['nick_name'] + ".jpg"

        try:
            os.rename(old_name, new_name)
        except Exception as e:
            logging.error(e)


        return item




class DouyuPipeline(object):
    def process_item(self, item, spider):
        #spider.logger.info("xxxx")
        return item
