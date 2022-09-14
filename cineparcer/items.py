# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from turtle import title
import scrapy


class CineparcerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    movie_title = scrapy.Field()
    photo = scrapy.Field()
    link = scrapy.Field()

    pass
