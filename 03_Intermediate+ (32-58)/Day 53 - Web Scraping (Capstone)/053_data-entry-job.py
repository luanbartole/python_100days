import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Constants
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://forms.gle/UsLgMpt2bCGuHE6L6"

# HTTP headers to mimic a real browser request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/134.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

# Send a GET request to the Zillow clone page and parse it with BeautifulSoup
response = requests.get(url=ZILLOW_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Extract rent prices using a regex pattern to filter clean dollar values
price_pattern = re.compile(r'\$\d[\d,]*')
rent_prices = soup.find_all(name="span", attrs={"data-test": "property-card-price"})
rent_prices = [
    price_pattern.search(price.get_text()).group()
    for price in rent_prices if price_pattern.search(price.get_text())
]

# Extract property links from anchor tags
rent_links = [
    link.get("href")
    for link in soup.find_all(name="a", class_="property-card-link")
]

# Extract and clean property addresses
rent_addresses = [
    re.sub(r'\s*\|\s*', ' - ', address.get_text().strip())
    for address in soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
]

# Initialize Chrome browser with option to keep window open after script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Loop through all properties and submit their data into the Google Form
for i in range(len(rent_prices)):
    driver.get(FORM_URL)
    time.sleep(5)  # Wait for the form to load

    # Locate all input fields for address, price, and link
    questions = driver.find_elements(By.CSS_SELECTOR, value="div.Qr7Oae input")
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # Fill each field with corresponding property data
    questions[0].send_keys(rent_addresses[i])
    questions[1].send_keys(rent_prices[i])
    questions[2].send_keys(rent_links[i])

    # Submit the form
    submit_button.click()

# Close the browser after all submissions
driver.quit()
