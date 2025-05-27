import os  # Access environment variables (email credentials)
import requests  # Make HTTP requests
from bs4 import BeautifulSoup  # Parse HTML from the product page
import smtplib  # Send email alerts
import html  # Handle special characters in product title

# ============================== ENVIRONMENT VARIABLES ==============================

# Email credentials and recipient email are stored as environment variables for security
sender_email = os.environ.get("PYTHON_EMAIL")
sender_password = os.environ.get("PYTHON_EMAIL_PASSWORD")
user_email = os.environ.get("USER_EMAIL")

# Set request headers to simulate a browser and avoid being blocked by Amazon
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/134.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

# ============================== USER INPUT & FETCH PRODUCT PAGE ==============================

print("=" * 45)
print(" " * 12 + "Amazon Price Tracker")
print("=" * 45)

# Input Product URL
url = input("Amazon Product URL:")

# Get desired price from user
desired_price = int(input("Desired Price (No decimals): R$ "))

# Request the product page and parse the HTML
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Extract product name and strip whitespace
product_name = soup.find(name="span", id="productTitle").get_text().strip()

# ============================== SCRAPE PRODUCT PRICE ==============================

# Extract the product's price (whole number only)
price = int(soup.find(name="span", class_="a-price-whole").get_text().strip(","))

# ============================== SEND EMAIL ALERT IF PRICE IS LOW ==============================

if price <= desired_price:
    # Shorten title for subject if needed
    product_title = product_name[:20] if len(product_name) > 20 else html.unescape(product_name)

    # Compose the email message
    message = (
        f"Subject: Amazon Price Alert! Low Price on '{product_title}...'\n\n"
        f"Product: {product_name}\n"
        f"Desired Minimum Price: R${desired_price: .0f},00\n"
        f"Current Price: R${price: .0f},00"
    )
    print(message)  # Debug print

    # Send the email via Gmail SMTP
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Start TLS encryption
        connection.login(sender_email, sender_password)  # Login to email server
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=user_email,
            msg=message.encode("utf-8")  # Handle special characters
        )
