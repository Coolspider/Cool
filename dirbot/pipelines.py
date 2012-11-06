from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""


    def process_item(self, item, spider):
        articl_name = '~/articl/%s' %(item['articl_name'][0])
        fp = open(articl_name, 'w')
        fp.write(item['content'][0])
        fp.close()
        return item
