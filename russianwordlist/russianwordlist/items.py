# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RussianWordListItem(scrapy.Item):
    rank = scrapy.Field()
    word = scrapy.Field()
    english_translation = scrapy.Field()
    part_of_speech = scrapy.Field()
    
