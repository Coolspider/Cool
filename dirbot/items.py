from scrapy.item import Item, Field


class DirbotItem(Item):

    urls = Field()
    #description = Field()


class Website(DirbotItem):

    #url = Field()

    def __str__(self):
        #con_url = {}
        #con_url = self.get('urls')
        #print '____________________________Website'
        print 'the url: %s\n'%(self.get('urls'))
        return 'sucess'
