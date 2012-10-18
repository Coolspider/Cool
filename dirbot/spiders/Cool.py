from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from dirbot.items import Website
import string


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
        #global page_url
        #print 'sites %s \nlen:%d\n' %(sites, len(sites))
        #for site in sites:
        item = Website()
        #divs = site.select('//div[contains(@class,"post")]')
        item['urls'] = sites.select('//a[contains(@class,"title")]/@href').extract()
        #item['description'] = site.select('text()').extract()
        #print "prase the url: %s\n" %(item['urls'])
        items.append(item)

        page_div = sites.select('//div[contains(@id, "pagenavi")]')
        page_num_info = page_div.select('//span[contains(@class, "pages")]/text()').extract()
        #print 'len; %d\ntype: %s\npage info: %s\n' %(len(page_num_info),type(page_num_info),page_num_info)
        page_num = page_num_info[0].split()
        page_urls = page_div.select('//a[contains(@class, "page")]/@href').extract()
        page_nums = page_div.select('//a[contains(@class, "page")]/text()').extract()
        #print 'page_nums %s \nurls %s\n len %d\n' %(page_nums, page_urls, len(page_urls))
        for n_count in range(len(page_nums)):
            #print 'n_count %d   %d page_num %s\n' %(n_count, len(page_num), page_num)
            if string.atoi(page_num[1]) + 1 > string.atoi(page_num[3]):
                print 'reach the blogs end\n'
                #return items
                break
            if string.atoi(page_num[1])+1 == string.atoi(page_nums[n_count]):
                page_url = page_urls[n_count]
                print 'n_count %d\npage_url %s\n' %(n_count, page_url)
                return Request(page_url, callback=self.parse)
            #return Request(page_url, callback=self.parse)
        return items

