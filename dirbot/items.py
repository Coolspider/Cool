from scrapy.item import Item, Field


class DirbotItem(Item):

    articl_url = Field()
    page_url = Field()
    content = Field()
    articl_name = Field()
    #description = Field()


class Website(DirbotItem):

    #url = Field()

    def __str__(self):
        #con_url = {}
        #con_url = self.get('urls')
        #print '____________________________Website'
        print 'the articl url: %s\n'%(self.get('articl_url'))
        print 'the page url: %s\n'%(self.get('page_url'))
        #print 'the content: %s\n'%(self.get('content'))
        print 'articl_name : %s\n'%(self.get('articl_name'))
        return 'sucess'
