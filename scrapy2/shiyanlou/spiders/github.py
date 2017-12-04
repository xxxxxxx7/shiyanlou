# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem


class GithubSpider(scrapy.Spider):

    name = 'github'
    allowed_domains = ['github.com']

    @property

    def start_urls(self):

        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):

        for lab in response.css('li.public'):


            item = ShiyanlouItem({
                'name': lab.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time': lab.xpath('.//relative-time/@datetime').extract_first()

            })
            yield item



