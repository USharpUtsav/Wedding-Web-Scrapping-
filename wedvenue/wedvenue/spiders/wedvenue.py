import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import re

class VenueSpider(scrapy.Spider):
    name = "venue_spider"
    start_urls = [
        "https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1"
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.unique_urls = set()

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(3)

        order = 0  # Track order of venues

        for _ in range(6):
            venue_links = self.driver.find_elements(By.CSS_SELECTOR, "div.srp-venues-container a")

            for link in venue_links:
                url = link.get_attribute("href")
                if url not in self.unique_urls:
                    self.unique_urls.add(url)
                    order += 1
                    yield scrapy.Request(url, callback=self.parse_venue_details,meta={"order": order})

            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next Page']")
                next_button.click()
                time.sleep(3)  # Wait for new page to load
            except Exception as e:
                self.logger.error(f"Next Page button not found: {e}")
                break  # Stop if there's no next page

    def parse_venue_details(self, response):
        url = response.url
        venue_name = response.css('h1::text').get()

        venue_highlights = []
        # Search for the JSON that contains "venue_highlights"
        match = re.search(r'("venue_highlights":\[[^\]]+\])', response.text)
        if match:
            venue_highlights_json = match.group(1)
            # Convert the matched JSON string to a Python list
            try:
                venue_highlights_data = json.loads('{' + venue_highlights_json + '}')["venue_highlights"]
                # Extract the 'label' from each highlight
                venue_highlights = [highlight.get("label") for highlight in venue_highlights_data]
            except json.JSONDecodeError:
                self.logger.error("Error decoding JSON for venue highlights.")

        script_content = response.css('script[type="application/ld+json"]::text').get()
        telephone_number = None
        if script_content:
            json_data = json.loads(script_content)
            telephone_number = json_data.get("telephone")

        # Extract the address
        address_data = json_data.get("address", {})
        street_address = address_data.get("streetAddress", "")
        postal_code = address_data.get("postalCode", "")
        locality = address_data.get("addressLocality", "")
        region = address_data.get("addressRegion", "")


        full_address = f"{street_address}, {locality}, {region} {postal_code}"

        text = response.css('p::text').getall()
        guest_capacity = None
        for t in text:
            match = re.search(r'\d+', t)
            if match:
                guest_capacity = match.group()
                break  # Exit the loop once the first numeric value is found

        order = response.meta["order"]  # Retrieve the order

        yield {
            "Order": order,
            "A - URL": url,
            "B - Venue Name": venue_name,
            "C - Phone": telephone_number,
            "D - Venue Highlights": venue_highlights,
            "E - Guest Capacity": guest_capacity,
            "F - Address": full_address,
        }

    def closed(self, reason):
        self.driver.quit()
