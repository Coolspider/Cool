from scrapy.exceptions import DropItem
from os import path, mkdir, chdir


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""


    def process_item(self, item, spider):
        articl_path = path.expanduser('~') + '/Articl/'
        if not path.exists(articl_path):
            mkdir(articl_path)
        chdir(articl_path)
        tmp_name = u'%s' %(item['articl_name'][0])
        articl_name = articl_path + u'%s.html' %(tmp_name)
        print 'articl name :%s' %(articl_name)
        #articl_name = '/home/chen/articl/tmp.data'
        fp = open(articl_name, 'w')
        for str_tmp in item['content']:
            fp.write(str_tmp.encode('utf-8'))
        fp.close()
        return item
