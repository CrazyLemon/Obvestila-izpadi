 # -*- coding:UTF-8  -*-
import scrapy

class IncidentItem(scrapy.Item):
    date = scrapy.Field()
    time = scrapy.Field()
    location = scrapy.Field()
    incidentType = scrapy.Field()
    incidentDescription = scrapy.Field()


class sos112Spider(scrapy.Spider):
    name = "sos112"
    allowed_domains = ["sos112.si"]
    start_urls = ["http://spin.sos112.si/SPIN2/Javno/Dogodki/"]

    def parse(self, response):

        for incidents in response.css(" ul > li"):
            item = IncidentItem()
            location = incidents.css('b ::text').extract_first(),
            incidentType = incidents.css('h2 ').extract_first(),
            incidentDescription = incidents.extract(),

            dateAndTime = incidentType[0].strip().split('<br>')[1].replace("\r\n                    ","").replace(" </h2>","")
            item['location'] = location
            item['incidentType'] = incidentType[0].strip().split('<br>')[0].replace("<h2>","")
            item['date'] = dateAndTime.split(" ")[0]
            item['time'] =  dateAndTime.split(" ")[1]
            item['incidentDescription'] = incidentDescription[0].strip().split('<br>')[2].replace("\r\n                ","").replace("\r\n            </li>","")
            yield item
