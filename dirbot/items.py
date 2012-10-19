from scrapy.item import Item, Field


class DirbotItem(Item):

    articl_url = Field()
    page_url = Field()
    content_url = Field()
    #description = Field()


class Website(DirbotItem):

    #url = Field()

    def __str__(self):
        #con_url = {}
        #con_url = self.get('urls')
        #print '____________________________Website'
        print 'the articl url: %s\n'%(self.get('articl_url'))
        print 'the page url: %s\n'%(self.get('page_url'))
        print 'the content url: %s\n'%(self.get('content_url'))
        return 'sucess'
