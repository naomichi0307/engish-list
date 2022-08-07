import scrapy
import logging
# from elscrapy.items import ElscrapyItem
class WordSpider(scrapy.Spider):
    name = 'word'
    allowed_domains = ['ejje.weblio.jp']
    # start_urls = ['http://ejje.weblio.jp/content/']
  

    def __init__(self, query='', *args, **kwargs):
        super(WordSpider, self).__init__(*args, **kwargs)
        self.user_agent = 'custom-user-agent'
        self.start_urls = ['https://ejje.weblio.jp/content/' + query]



    def parse(self, response):
       
        # item=ElscrapyItem()
        # item['word']=response.xpath('//*[@id="summary"]/div[2]/p/span[2]/text()').get().replace('\n', '').strip()
        # yield item
        word=response.xpath('//*[@id="summary"]/div[2]/p/span[2]/text()').get().replace('\n', '').strip()
        yield{
            'word':word
        }