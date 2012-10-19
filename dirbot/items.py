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
        print 'the url: %s\n'%(self.get('articl_url'))
        print 'the url: %s\n'%(self.get('page_url'))
        print 'the url: %s\n'%(self.get('urls'))
        return 'sucess'
