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
            item = ShiyanlouItem()
            item['name'] = lab.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
            item['update_time'] = lab.xpath('.//relative-time/@datetime').extract_first()
            repo_url = response.urljoin(lab.xpath('.//a/@href').extract_first())
            request = scrapy.Request(repo_url, callback = self.parse_repo)
            request.meta['item'] = item          
            yield request

    def parse_repo(self, response):
        item = response.meta['item']
        for number in response.css('ul.numbers-summary li'):
            name_text = number.xpath('.//a/text()').re_first('\n\s*(.*)\n')
            number_text = number.xpath('.//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)\n')
            if name_text and number_text:
                number_text = number_text.replace(',','')
                if name_text in ('commit', 'commits'):
                    item['commits'] = int(number_text)
                elif name_text in ('branch', 'branches'):
                    item['branches'] = int(number_text)
                elif name_text in ('release', 'releases'):
                    item['releases'] = int(number_text)
            yield item
