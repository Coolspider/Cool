from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    #words_to_filter = ['', 'religion']

    def process_item(self, item, spider):
        for url in unicode(item['urls']):
           raise DropItem("Contains forbidden word: %s\n" %url)
        else:
            return item
