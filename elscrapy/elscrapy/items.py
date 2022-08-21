# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join

class ElscrapyItem(scrapy.Item):
    word = scrapy.Field(
        input_processor = MapCompose(str.lstrip),#入力する文字列（取得したデータ）の空白部分を削除
        output_processor = Join(' ')#input_processorはリスト型なので、こちらで連結する
    )