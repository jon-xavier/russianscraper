import scrapy
from russianwordlist.items import RussianWordListItem

class MasterRussianSpider(scrapy.Spider):
    name = "master_russian"
    allowed_domains = ["http://http://masterrussian.com/vocabulary"]
    start_urls = ["http://http://masterrussian.com/vocabulary/most_common_words.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_2.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_3.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_4.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_5.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_6.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_7.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_8.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_9.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_10.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_11.htm",
    "http://http://masterrussian.com/vocabulary/most_common_words_12.htm",
    ]
    
    def parse(self, response):
        
        for sel in response.xpath('//*[@id="wrapper"]/div[2]/div/div/div[1]/div/table[2]/tbody'):
            item = RussianWordListItem()
            item['rank'] = sel.xpath('//*[@id="wrapper"]/div[2]/div/div/div[1]/div/table[2]/tbody/tr/td[1]/text()').extract
            item['word'] = sel.xpath('//*[@id="wrapper"]/div[2]/div/div/div[1]/div/table[2]/tbody/tr/td[3]/a/text()').extract
            item['english_translation'] = sel.xpath('//*[@id="wrapper"]/div[2]/div/div/div[1]/div/table[2]/tbody/tr/td[4]/text()').extract
            item['part_of_speech'] = sel.xpath('//*[@id="wrapper"]/div[2]/div/div/div[1]/div/table[2]/tbody/tr/td[5]/text()').extract
            yield item