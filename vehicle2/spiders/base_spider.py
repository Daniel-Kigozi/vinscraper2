import scrapy

class BaseSpider(scrapy.Spider):
    name = 'base_spider'

    def __init__(self, base_url=False, **kwargs):
        if not base_url:
            raise ValueError('Base url must be provided')

        self.base_url = base_url
        self.start_urls = [f'{base_url}/vehicles/?']
        super().__init__(**kwargs)

    def parse(self, response):
        pass

    def parse_vehicle(self, response):
        pass
