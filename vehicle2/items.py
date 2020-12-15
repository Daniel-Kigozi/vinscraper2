# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Vehicle2Item(scrapy.Item):
    price = scrapy.Field()
    stock_number = scrapy.Field()
    vin = scrapy.Field()
    status = scrapy.Field()

    year = scrapy.Field()
    kilometers = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    trim = scrapy.Field()
      
    exterior_color = scrapy.Field()
    interior_color = scrapy.Field()
    fuel_type = scrapy.Field()
    drive = scrapy.Field()

    engine_size = scrapy.Field()
    cylinder = scrapy.Field()
    transmission = scrapy.Field()
    fuel_type= scrapy.Field()

    doors = scrapy.Field()
    body_type = scrapy.Field()
    photos = scrapy.Field()

    