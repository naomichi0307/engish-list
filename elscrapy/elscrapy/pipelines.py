# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ElscrapyPipeline:
    def process_item(self, item, spider):
        return item

#ここからsqlite3

class SQLitePipeline:
    def open_spider(self,spider):
        self.connection = sqlite3.connect('../elproject/db.sqlite3')
        self.c=self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE word_list(
                    word text
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
        

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO word_list (word)
            VALUES(?)
        ''', (
            item.get('word'),
        ))
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.connection.close()