# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re

class HeightweightSpider(scrapy.Spider):
    name = "heightweight"
    allowed_domains = ["height-weight-chart.com"]
    url_base = 'http://height-weight-chart.com/'
    start_urls = (
        url_base + 'heightweight.html',
    )

    def parse(self, response):
        pages = response.css('.thumb::attr(src)').extract()
        if pages:
            for p in pages:
                m = re.match('s\/(.*)_s.jpg', p)
                if m:
                    yield Request(url=self.url_base + m.group(1) + '.html', callback=self.parse_page)

    def parse_page(self, response):
        pics = response.css('.largepic::attr(src)').extract()
        if pics:
            for p in pics:
                yield Request(url=self.url_base+p, callback=self.save_pic)

    def save_pic(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
