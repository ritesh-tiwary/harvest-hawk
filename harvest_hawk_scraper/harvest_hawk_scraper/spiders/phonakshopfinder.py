import json
import scrapy


class PhonakshopfinderSpider(scrapy.Spider):
    name = "phonakshopfinder"
    locations = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Maharashtra", "Madhya Pradesh", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Telangana", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman Nicobar", "Chandigarh", "Dadra Nagar Haveli and Daman Diu", "Delhi", "Jammu Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]


    def start_requests(self):
        for location in self.locations:
            url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
            yield scrapy.Request(url, self.parse_coordinates, meta={"location": location})

    def coordinates_by_location(self, location_name, locations):
        for location in locations:
            if location.get("name") == location_name and "India" in location.get("display_name", ""):
                return location.get("lat"), location.get("lon")  
    
    def parse_coordinates(self, response):        
        locations = json.loads(response.body)
        location_name = response.meta.get("location", "Unknown")
        lat, lon = self.coordinates_by_location(location_name, locations)
        self.logger.info(f"Coordinates for {location_name}: {lat}, {lon}")

        if lat and lon:
            url = f"https://www.phonak.com/content/phonak/in/en/find-a-provider/jcr:content/root/container/findaprovider_copy_c.find.json?lat={lat}&lng={lon}"
            yield scrapy.Request(url, self.parse_shops, meta={"location": location_name})

    def parse_shops(self, response):
        data = json.loads(response.body)
        state = response.meta.get("location", "Unknown")
        for shop in data.get("dealers", []):
            yield {
                'name': shop.get('name', ''),
                'address': f"{shop.get('address', '')}, {shop.get('city', '')}",
                'state': state,
                'country': shop.get('country', ''),
                'postalCode': shop.get('zipcode', ''),
                'contactPhone': shop.get('phone', '')
                }
