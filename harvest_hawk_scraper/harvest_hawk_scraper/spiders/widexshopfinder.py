import json
import scrapy


class WidexshopfinderSpider(scrapy.Spider):
    name = "widexshopfinder"
    allowed_domains = ["widex.com"]
    start_urls = ['https://www.widex.com/api/shop-finder/GetShopsByProximity?latlng=-2.4431722633004624,78.45883144232754&country=IN&filterOnPreferred=false&isInitialMapLoad=true&shopFinderDatasourceId={ECBC1A3C-7745-4635-AC7D-21621D0379F1}']

    def parse(self, response):
        data = json.loads(response.body)
        for shop in data:
            yield {
                'title': shop.get('title', ''),
                'address': shop.get('addressLine1', ''),
                'state': shop.get('state', ''),
                'country': shop.get('country', ''),
                'postalCode': shop.get('postalCode', ''),
                'contactPhone': shop.get('contactPhone', '')
                }
