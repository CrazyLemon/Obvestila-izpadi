 # -*- coding:UTF-8  -*-
import scrapy
import logging

class ElektroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    fromHour = scrapy.Field()
    toHour = scrapy.Field()
    #location = scrapy.Field()
    city = scrapy.Field()
    street = scrapy.Field()

class ElektroprimorskaSpider(scrapy.Spider):
    name = "elektroprimorska"
    allowed_domains = ["elektro-primorska.si"]
    start_urls = [
        "http://www.elektro-primorska.si/omrezje/obvestila-o-izklopih/"]

    def parse(self, response):
        #LOCATION_SELECTOR = 'h2 ::text'

        for locationEl in response.css('.blackout-wrapper'):
            item = ElektroItem()
            #location = locationEl.css(LOCATION_SELECTOR).extract_first(),
            date = locationEl.css('p > strong ::text').extract_first(),
            fromHour = locationEl.css('p > strong:nth-child(2) ::text').extract_first(),
            toHour = locationEl.css('p > strong:nth-child(3) ::text').extract_first(),

            #item['location'] = location[0].strip().split(': ')[1]
            item['date'] = date[0].strip().split(', ')[1]
            item['fromHour'] = fromHour[0].strip().split(',')[0]
            item['toHour'] = toHour[0].strip().split(',')[0]
            
            for cities in locationEl.css('.field-item'):
                city = cities.css('h3 ::text').extract()
                streets = cities.css('li ::text').extract()

                for i, element in enumerate(city):
                    item['city'] = city[i]
                    item['street'] = streets
                    yield item
