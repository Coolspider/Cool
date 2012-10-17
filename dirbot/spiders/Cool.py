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
        sites = hxs.select('//body')
        items = []
        #print 'sites %s \nlen:%d\n' %(sites, len(sites))
        #for site in sites:
        item = Website()
        #divs = site.select('//div[contains(@class,"post")]')
        item['urls'] = sites.select('//a[contains(@class,"title")]/@href').extract()
        #item['description'] = site.select('text()').extract()
        #print "prase the url: %s\n" %(item['urls'])
        items.append(item)

        return items
