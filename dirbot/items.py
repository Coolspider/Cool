from scrapy.item import Item, Field


class DirbotItem(Item):

    urls = Field()
    #description = Field()


class Website(DirbotItem):

    #url = Field()

    def __str__(self):
        con_url = self.get('urls')
        return con_url
