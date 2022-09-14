from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from cineparcer import settings
from cineparcer.spiders.mirageruspb import MirageruspbSpider

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(MirageruspbSpider, city = "spb")
    process.start()