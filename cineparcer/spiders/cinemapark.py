import scrapy
from scrapy.http import HtmlResponse
from cineparcer.items import CineparcerItem

class CinemaparkSpider(scrapy.Spider):
    name = 'cinemapark'
    allowed_domains = ['kinoteatr.ru']
    

    def __init__(self, city):
        self.start_urls = [f'https://kinoteatr.ru/kinoafisha/{city}/']

    def parse(self, response: HtmlResponse):

        movie_links = response.xpath('//a[contains(@class, "movie_card")]/@href').extract()
        movie_titles = response.xpath('//div[contains(@class, "movie_card")]/@data-gtm-list-item-filmname').extract()
        movie_photos = response.xpath('//img[contains(@class, "movie_card")]/@src').extract()
        for i in range(len(movie_links)):
            yield CineparcerItem(link = movie_links[i], movie_title = movie_titles[i], photo = movie_photos[i])
