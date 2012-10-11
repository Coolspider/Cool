from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    #words_to_filter = ['', 'religion']

    def process_item(self, item, spider):
        item_list = []
        item_list = unicode(item['urls'])
        print '______________process_item'
        #for url in unicode(item['urls']):
        #   raise DropItem("Contains forbidden word: %s\n" %url)
        #else:
        print 'type:%s  longth:%d\n' %(type(item_list), len(item_list))
        
        print 'url %s\n' %item['urls'][50]
        return item
