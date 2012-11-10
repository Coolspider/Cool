from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""


    def process_item(self, item, spider):
        tmp_name = u'%s' %(item['articl_name'][0])
        articl_name = u'/home/chen/articl/%s.html' %(tmp_name)
        print 'articl name :%s' %(articl_name)
        #articl_name = '/home/chen/articl/tmp.data'
        fp = open(articl_name, 'w')
        for str_tmp in item['content']:
            fp.write(str_tmp.encode('utf-8'))
        fp.close()
        return item
