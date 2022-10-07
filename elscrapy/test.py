# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings

# process = CrawlerProcess(get_project_settings())

# # 'followall' is the name of one of the spiders of the project.
# process.crawl('word', query='relative')
# process.start() # the script will block here until the crawling is finished

import scrapy
from scrapy.crawler import CrawlerProcess

from elscrapy.spiders.word import WordSpider

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
        #loader = ItemLoader(item = ElscrapyItem(), response=response)
        #loader.add_xpath('word', '//*[@id="summary"]/div[2]/p/span[2]/text()')
        #yield loader.load_item()
        yield{
            'word':word
        }
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(WordSpider, query='relative')
process.start() # the script will block here until the crawling is finished