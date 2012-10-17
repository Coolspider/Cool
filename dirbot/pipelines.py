from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""


    def process_item(self, item, spider):
        #print '______________process_item'
        #for url in unicode(item['urls']):
        #   raise DropItem("Contains forbidden word: %s\n" %url)
        #else:
        #print 'item list longth:%d\n item_list:%s' %(len(item['urls']), item['urls'])
        for item_l in item['urls']:
            print 'url: %s\n' %(item_l)
        return item
