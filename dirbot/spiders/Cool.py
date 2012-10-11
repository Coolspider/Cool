from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import Website


class CoolSpider(BaseSpider):
    name = "Cool"
    allowed_domains = ["coolshell.cn"]
    start_urls = [
        "http://coolshell.cn/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//li')
        items = []

        for site in sites:
            item = Website()
            item['urls'] = site.select('//a/@href').extract()
            #item['url'] = site.select('a/@href').extract()
            #item['description'] = site.select('text()').extract()
            items.append(item)

        return items
