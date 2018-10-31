# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 直播间链接
    room_link = scrapy.Field()
    # 图片链接
    image_src = scrapy.Field()
    # 艺名
    nick_name = scrapy.Field()
    # 所在城市
    anchor_city = scrapy.Field()
    # 图片在磁盘中的路径
    image_path = scrapy.Field()
