# -*- coding: utf-8 -*-
import scrapy


class LoichuaSpider(scrapy.Spider):
    name = 'loichua'
    allowed_domains = ['loichua']
    start_urls = ['http://loichua/']

    def parse(self, response):
        pass
