# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes.items import QuotesItem


class QuotesSpiderSpider(Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesItem(), response=response)
        h1_tag = response.xpath("//h1/a/text()").extract_first(),
        tags = response.xpath("//*[@class = 'tag-item']/a/text()").extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()