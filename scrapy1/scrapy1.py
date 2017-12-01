#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):

	name = 'github_scrapy'

	@property

	def start_urls(self):
		
		url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

		# urls = (url_tmpl.format(i) for i in range(1, 23))

		# for url in urls:
		# 	return scrapy.Request(url=url, callback=self.parse)



		return (url_tmpl.format(i) for i in range(1, 5))



	def parse(self, response):
		for lab in response.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom public source"]'):


			yield {
				
				'name': lab.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n(.*)"),
				'update_time': lab.xpath('.//relative-time/@datetime').extract_first()


			}
