import scrapy
from scrapy.http import HtmlResponse
from cineparcer.items import CineparcerItem

class VelikanparkSpider(scrapy.Spider):
    name = 'velikanpark'
    allowed_domains = ['velikan-park.ru']
    start_urls = ['http://velikan-park.ru/afisha/']

    def parse(self, response: HtmlResponse):
        movie_links = response.xpath('//div[contains(@class, "today")]/a/@href').extract()
        movie_titles = response.xpath('//div[contains(@class, "today")]//img/@alt').extract()
        movie_photos = response.xpath('//div[contains(@class, "today")]//img/@src').extract()
        for i in range(len(movie_links)):
            yield CineparcerItem(link = response.urljoin(movie_links[i]), movie_title = movie_titles[i], \
             photo = response.urljoin(movie_photos[i]))

