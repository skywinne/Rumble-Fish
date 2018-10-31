#coding:utf-8

import json

import scrapy
from ..items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]

    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    offset = 0

    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']

        # 判断响应数据是否为空，如果为空直接退出
        if not data_list:
            return

        for data in data_list:
            item = DouyuItem()

            item['room_link'] = u"http://www.douyu.com/" + data['room_id']
            item['image_src'] = data['vertical_src']
            item['nick_name'] = data['nickname']
            item['anchor_city'] = data['anchor_city']

            # 发送图片的链接请求，传递nick_name字符串并调用回调函数parse_page处理响应
            yield scrapy.Request(item['image_src'], meta={"name" : item['nick_name']}, callback=self.parse_image)


        self.offset += 100
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)

    # 1. 通用方式，直接获取资源文件的链接，发送请求再用open方法写入响应数据保存
    def parse_image(self, response):
        filename = response.meta['name'] + ".jpg"

        # 获取响应，按 "wb" 模式保存图片数据
        with open(filename, "wb") as f:
            f.write(response.body)












