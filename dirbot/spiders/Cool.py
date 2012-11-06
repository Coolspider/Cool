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
        items = []
        global page_request, articl_request
        item = Website()
        item['articl_url'] = self.parse_articl_url(response)
        page_url = self.parse_page_url(response)
        item['page_url'] = []
        if page_url != 0:
            item['page_url'].append(page_url)
        item['content'] = []
        item['articl_name'] = []
        #print "articl url:%s\nlen:%d\n" %(item['articl_url'],len(item['articl_url']))
        for t_count in range(len(item['articl_url'])):
            articl_url = item['articl_url'][t_count]
            print "##################requse url = %s\n" %(articl_url)
            articl_request = Request(articl_url, callback=self.parse_articl_content)
            articl_request.meta['item'] = item
            yield articl_request
            if t_count == len(item['articl_url']) - 1:
                if item['page_url']:
                    print '$$$$$$$$$$$$$$$$$$$$$$$$page url %s\n' %(item['page_url'][0])
                    page_request = Request(item['page_url'][0], callback=self.parse)
                    #yield page_request
    def parse_articl_url(self, response):
        hxs = HtmlXPathSelector(response)
        url = hxs.select('//a[contains(@class,"title")]/@href').extract()
        print 'artcil url: %s' %(url)
        return url
    def parse_articl_content(self, response):
        item = response.meta['item']
        hxs = HtmlXPathSelector(response)
        name_div = hxs.select('//div[@class="post"]')
        item['articl_name'] = name_div.select('//h2/text()').extract()
        item['content'] = hxs.select('//body').extract()
        #print item['content']
        return item
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
