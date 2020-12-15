import scrapy
import re
import chompjs

from .base_spider import BaseSpider
from vehicle2.helpers.repair_json import repair_json
from vehicle2.items import Vehicle2Item


class ConvertusSpider(BaseSpider):
    name = 'convertus'

    def parse(self, response):
        vehicles = response.css('div.list-view > div.vehicle-card a.url')
        for a_tag in vehicles:
            # Parse each vehicle
            yield scrapy.Request(self.base_url + a_tag.attrib['href'], callback=self.parse_vehicle2)
        # Get query string for next page
        # next_page_extension = response.css(
        #     'ul.pagination a[rel="next"]::attr(href)').get()
        # if next_page_extension:
        #     # Recursively pull vehilce urls if extension is found
        #     yield scrapy.Request(self.base_url + '/all-inventory/index.htm' + next_page_extension, callback=self.parse)

    def parse_vehicle(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        # Yield result
        yield Vehicle2Item(
        #     'title'= extract_with_css('title'),
        #     'make' = extract_with_css('div.data-vehicle-make::text'),
        #     'model'= extract_with_css('div.data-vehicle-model::text'),
        #     'year' = extract_with_css('div.data-vehicle-year::text'),
        #     'condition'= extract_with_css('div.data-vehicle-condition::text'),
        #     'id': extract_with_css('div.data-vehicle-id::text'),
        #     'body-style'= extract_with_css('div.data-vehicle-body-style::text'),
        #     'odometer'= extract_with_css('div.data-vehicle-odo::text'),
        #     'stock-number'= extract_with_css('div.data-vehicle-stock::text'),
        #     'vin'= extract_with_css('div.data-vehicle-vin::text'),
        #     'colour'= extract_with_css('div.data-vehicle-colour::text'),
        #     'mrsp'= extract_with_css('div.data-vehicle-mrsp::text'),
        #     'price'= extract_with_css('div.data-vehicle-internet-price::text'),
        #     'trim'= extract_with_css('div.data-vehicle-trim::text'),
        #     'transmision'= extract_with_css('div.data-vehicle-transmission::text'),
        #     'make'= extract_with_css('div.data-vehicle-make::text'),
        #     'make'= extract_with_css('div.data-vehicle-make::text'),
        #     photos=[image.get('uri') for image in details.get(
        #         'images') if image.get('uri')]
        # )
            
            price=details.get('internetPrice'),
            vin=details.get('vin'),
            stock_number=details.get('stockNumber'),

            status=details.get('newOrUsed'),
            kilometers=details.get('odometer'),
            make=details.get('make'),
            model=details.get('model'),
            trim=details.get('trim'),
            year=details.get('modelYear'),

            body_type=details.get('bodyStyle'),
            engine_size=details.get('engineSize'),
            doors=details.get('doors'),
            fuel_type=details.get('fuelType'),
            transmission=details.get('transmission'),

            exterior_color=details.get('exteriorColor'),
            interior_color=details.get('interiorColor'),

            photos=[image.get('uri') for image in details.get(
                'images') if image.get('uri')]
        )
