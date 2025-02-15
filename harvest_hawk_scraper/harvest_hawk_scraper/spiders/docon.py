import json
import scrapy
from pandas import read_csv


class DoconSpider(scrapy.Spider):
    name = "docon"

    # def start_requests(self):
    #     url = "https://www.nmc.org.in/MCIRest/open/getPaginatedData?service=getPaginatedDoctor&draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=1&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=2&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=3&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=4&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=5&columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=6&columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&start=0&length=99999&search%5Bvalue%5D=&search%5Bregex%5D=false&year=2004&_="
    #     yield scrapy.Request(url, self.parse_doctornames)
            
    # def parse_doctornames(self, response):
    def start_requests(self):
        # data = json.loads(response.body)
        # for doctor in data["data"]:
        #     if doctor[4]:
        #         yield {"doctorName": doctor[4].strip().lower()}

        # doctor_names = [doctor_name[4].lower().split()[0] for doctor_name in data["data"]]
        # for doctor_name in doctor_names:
        #     if doctor_name.isalpha():
        #         url = f"https://docon.co.in/api/v1/doctor/search?locality=&name={doctor_name}"
        #         yield scrapy.Request(url, self.parse_doctorids)

        df = read_csv("output/doctors_Ids.csv")
        df = df.iloc[2015:3015]
        for _, row in df.iterrows():
            # url = f"https://docon.co.in/api/v1/doctor/search?locality=&name={row.doctorName}"
            # yield scrapy.Request(url, self.parse_doctorids)
            url = f"https://docon.co.in/api/v1/doctor/clinic-details?doctorID={row.doctorId}"
            yield scrapy.Request(url, self.parse_doctordetail, meta={"firstName": row.firstName, "lastName": row.lastName})

    def parse_doctorids(self, response):
        data = json.loads(response.body)
        for doctor in data.get("data", []):
            doctor_id = doctor.get("_source", {}).get("docID", "")
            first_name = doctor.get("_source", {}).get("firstName", "")
            last_name = doctor.get("_source", {}).get("lastName", "")
            yield {
                "doctorId": doctor_id,
                "firstName": first_name,
                "lastName": last_name,
            }
            # if doctor_id.isalnum():
            #     url = f"https://docon.co.in/api/v1/doctor/clinic-details?doctorID={doctor_id}"
            #     yield scrapy.Request(url, self.parse_doctordetail, meta={"firstName": first_name, "lastName": last_name})

    def parse_doctordetail(self, response):
        data = json.loads(response.body)
        first_name = response.meta.get("firstName", "")
        last_name = response.meta.get("lastName", "")
        for doctor in data:
            yield {
                "doctorName": f"{first_name} {last_name}",
                "clinicName": doctor.get("displayName", ""),
                "address": doctor.get("address", {}).get("line1", ""),
                "city": doctor.get("address", {}).get("city", ""),
                "state": doctor.get("address", {}).get("state", ""),
                "country": "India",
                "postalCode": doctor.get("address", {}).get("pincode", ""),
                "contactPhone": doctor.get("number", "")
                }
