# -*- coding: utf-8 -*-
import scrapy
import json


class BiliUserInfoSpider(scrapy.Spider):
    name = 'bili_user_info'
    allowed_domains = ['https://www.bilibili.com/']
    start_urls = ['http://https://www.bilibili.com//']

    def start_requests(self):
        for i in range(1, 1300):
            yield scrapy.Request(
                f'https://api.bilibili.com/x/web-interface/newlist?rid=33&type=0&pn={i}&ps=20&jsonp=jsonp&_=1522238225577',
                callback=self.parse,
                encoding='utf-8')

    def parse(self, response):
        # data = json.loads(response.text)['data']['archives']
        # print(data)

        for eve_data in json.loads(response.body.decode())["data"]["archives"]:
            print(eve_data)
            yield eve_data
