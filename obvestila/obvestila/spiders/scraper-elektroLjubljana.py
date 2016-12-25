import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class ElektroItem(scrapy.Item):
    fromDate = scrapy.Field()
    toDate = scrapy.Field()
    fromHour = scrapy.Field()
    toHour = scrapy.Field()
    city = scrapy.Field()
    street = scrapy.Field()

class ljubljanaCenter(scrapy.Spider):
    name = "ljubljanaCenter"
    start_urls = ["http://www.elektro-ljubljana.si/DesktopModules/DNNArticle/DNNArticleRSS.aspx?moduleid=555&tabid=741&categoryid=160"]
    def parse(self, response):
        item = ElektroItem()
        if response.xpath("//channel/item"):
            for items in response.xpath("//channel/item"):
                city = items.xpath(".//title/text()").extract_first(),
                street = items.xpath(".//description/text()").extract_first(),

                item['city'] = city[0].split(" od ")[0].replace("Izklop: ","")
                item['fromDate'] = city[0].split(" od ")[1].split(" ob ")[0]
                item['toDate'] =   city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[1]
                item['fromHour'] = city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[0]
                item['toHour'] = city[0].split(" od ")[1].split(" do ")[1].split(" ob ")[1]
                item['street'] = street[0].split(" energije na: ")[1].split(".")[0]
                yield item

class trbovlje(scrapy.Spider):
    name = "trbovlje"
    start_urls = ["http://www.elektro-ljubljana.si/DesktopModules/DNNArticle/DNNArticleRSS.aspx?moduleid=555&tabid=741&categoryid=163"]
    def parse(self, response):
        item = ElektroItem()
        if response.xpath("//channel/item"):
            for items in response.xpath("//channel/item"):
                city = items.xpath(".//title/text()").extract_first(),
                street = items.xpath(".//description/text()").extract_first(),

                item['city'] = city[0].split(" od ")[0].replace("Izklop: ","")
                item['fromDate'] = city[0].split(" od ")[1].split(" ob ")[0]
                item['toDate'] =   city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[1]
                item['fromHour'] = city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[0]
                item['toHour'] = city[0].split(" od ")[1].split(" do ")[1].split(" ob ")[1]
                item['street'] = street[0].split(" oskrbovani iz")[1].split(".")[0].split(",")
                yield item

class novoMesto(scrapy.Spider):
    name = "novoMesto"
    start_urls = ["http://www.elektro-ljubljana.si/DesktopModules/DNNArticle/DNNArticleRSS.aspx?moduleid=555&tabid=741&categoryid=161"]
    def parse(self, response):
        item = ElektroItem()
        if response.xpath("//channel/item"):
            for items in response.xpath("//channel/item"):
                city = items.xpath(".//title/text()").extract_first(),
                street = items.xpath(".//description/text()").extract_first(),

                item['city'] = city[0].split(" od ")[0].replace("Izklop: ","")
                item['fromDate'] = city[0].split(" od ")[1].split(" ob ")[0]
                item['toDate'] =   city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[1]
                item['fromHour'] = city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[0]
                item['toHour'] = city[0].split(" od ")[1].split(" do ")[1].split(" ob ")[1]
                item['street'] = street[0].split(" oskrbovani iz")[1].split(".")[0].split(",")
                yield item

class ljubljanaOkolica(scrapy.Spider):
    name = "ljubljanaOkolica"
    start_urls = ["http://www.elektro-ljubljana.si/DesktopModules/DNNArticle/DNNArticleRSS.aspx?moduleid=555&tabid=741&categoryid=162"]
    def parse(self, response):
        item = ElektroItem()
        if response.xpath("//channel/item"):
            for items in response.xpath("//channel/item"):
                city = items.xpath(".//title/text()").extract_first(),
                street = items.xpath(".//description/text()").extract_first(),

                item['city'] = city[0].split(" od ")[0].replace("Izklop: ","")
                item['fromDate'] = city[0].split(" od ")[1].split(" ob ")[0]
                item['toDate'] =   city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[1]
                item['fromHour'] = city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[0]
                item['toHour'] = city[0].split(" od ")[1].split(" do ")[1].split(" ob ")[1]
                item['street'] = street[0].split(" oskrbovani iz")[1].split(".")[0].split(",")
                yield item

class kocevje(scrapy.Spider):
    name = "kocevje"
    start_urls = ["http://www.elektro-ljubljana.si/DesktopModules/DNNArticle/DNNArticleRSS.aspx?moduleid=555&tabid=741&categoryid=31"]
    def parse(self, response):
        item = ElektroItem()
        if response.xpath("//channel/item"):
            for items in response.xpath("//channel/item"):
                city = items.xpath(".//title/text()").extract_first(),
                street = items.xpath(".//description/text()").extract_first(),

                item['city'] = city[0].split(" od ")[0].replace("Izklop: ","")
                item['fromDate'] = city[0].split(" od ")[1].split(" ob ")[0]
                item['toDate'] =   city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[1]
                item['fromHour'] = city[0].split(" od ")[1].split(" ob ")[1].split(" do ")[0]
                item['toHour'] = city[0].split(" od ")[1].split(" do ")[1].split(" ob ")[1]
                item['street'] = street[0].split(" oskrbovani iz")[1].split(".")[0].split(",")
                yield item

configure_logging()
runner = CrawlerRunner()
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(ljubljanaCenter)
    yield runner.crawl(trbovlje)
    yield runner.crawl(novoMesto)
    yield runner.crawl(ljubljanaOkolica)
    yield runner.crawl(kocevje)
    reactor.stop()

crawl()
reactor.run() 
