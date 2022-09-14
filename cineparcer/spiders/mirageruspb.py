import scrapy
from scrapy.http import HtmlResponse
from cineparcer.items import CineparcerItem



class MirageruspbSpider(scrapy.Spider):
    name = 'mirageruspb'
    allowed_domains = ['mirage.ru']


    def __init__(self, city):
        self.start_urls = [f'http://mirage.ru/{city}/films/']

    def parse(self, response: HtmlResponse):
        
        movie_links = response.xpath('//a[contains(@class, "preview")]/@href').extract()
        movie_titles = response.xpath('//a[contains(@class, "title")]/text()').extract()
        movie_photos = response.xpath('//a[contains(@class, "preview")]/img/@src').extract()
        for i in range(len(movie_links)):
            yield CineparcerItem(link = response.urljoin(movie_links[i]), movie_title = movie_titles[i], photo = movie_photos[i])
            