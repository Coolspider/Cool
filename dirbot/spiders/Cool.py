from scrapy.spider import BaseSpider
#from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from dirbot.items import Website
#from scrapy.item import Item, Field
import string


class CoolSpider(BaseSpider):
    name = "Cool"
    allowed_domains = ["coolshell.cn"]
    start_urls = [
        "http://coolshell.cn/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #sites = hxs.select('//body')
        items = []
        #global page_url
        #print 'sites %s \nlen:%d\n' %(sites, len(sites))
        #for site in sites:
        item = Website()
        item['articl_url'] = hxs.select('//a[contains(@class,"title")]/@href').extract()
        item['page_url'] = []
        item['page_url'].append(tm_page_url)
        item['content_url'] = []
        return items
    def parse_articl_url(self, response):
        hxs = HtmlXPathSelector(response)
        url = hxs.select('//a[contains(@class,"title")]/@href').extract()
        print 'artcil url: %s' %(url)
        return url
    def parse_articl_content(self, response):
        hxs = HtmlXPathSelector(response)
        return hxs.select('//body').extract()
    def parse_page_url(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//body')
        page_div = sites.select('//div[contains(@id, "pagenavi")]')
        page_num_info = page_div.select('//span[contains(@class, "pages")]/text()').extract()
        #print 'len; %d\ntype: %s\npage info: %s\n' %(len(page_num_info),type(page_num_info),page_num_info)
        page_num = page_num_info[0].split()
        page_urls = page_div.select('//a[contains(@class, "page")]/@href').extract()
        page_nums = page_div.select('//a[contains(@class, "page")]/text()').extract()
        for n_count in range(len(page_nums)):
            #print 'n_count %d   %d page_num %s\n' %(n_count, len(page_num), page_num)
            if string.atoi(page_num[1]) + 1 > string.atoi(page_num[3]):
                print 'reach the blogs end\n'
                return 0
            if string.atoi(page_num[1])+1 == string.atoi(page_nums[n_count]):
                Page_url = page_urls[n_count]
                print 'n_count %d\npage_url %s\n' %(n_count, Page_url)
                return Page_url
