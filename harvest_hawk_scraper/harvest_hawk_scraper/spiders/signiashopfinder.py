import json
import scrapy


class SigniashopfinderSpider(scrapy.Spider):
    name = "signiashopfinder"
    allowed_domains = ["signia.net"]
    start_urls = ["https://www.signia.net/api/shop-finder/GetShopsByProximity?latlng=-2.4431722633004624,78.45883144232754&country=IN&filterOnPreferred=false&isInitialMapLoad=true&shopFinderDatasourceId={2357A5BD-F3F1-483D-9ADA-1C883EF8EE54}"]

    def parse(self, response):
        data = json.loads(response.body)
        for shop in data:
            yield {
                'name': shop.get('title', ''),
                'address': shop.get('addressLine1', ''),
                'state': shop.get('state', ''),
                'country': shop.get('country', ''),
                'postalCode': shop.get('postalCode', ''),
                'contactPhone': shop.get('contactPhone', '')
                }
