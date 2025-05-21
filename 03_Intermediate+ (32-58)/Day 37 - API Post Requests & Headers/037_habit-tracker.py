import requests
from datetime import datetime

# Get today's date in YYYYMMDD format
today = datetime.now().strftime("%Y%m%d")

# User credentials and API endpoints
USERNAME = "your-username"
TOKEN = "your-password"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
READING_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/programming"
PIXEL_ENDPOINT = f"{READING_GRAPH_ENDPOINT}/{today}"

# User account setup
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

# Graph configuration
graph_config = {
    "id": "programming",
    "name": "Coding Graph",
    "unit": "h",
    "type": "float",
    "color": "ajisai" # Purple
}

# Data to create a pixel (log 2 hours today)
pixel_params = {
    "date": today,
    "quantity": 2
}

# Data to update pixel (change to 60 hours)
update_pixel = {
    "quantity": "60"
}

# Header with auth token
headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment the desired action:

# Create a new user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create a new graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, nutritionix_headers=nutritionix_headers)
# print(response.text)

# Add a new pixel (data entry)
# response = requests.post(url=READING_GRAPH_ENDPOINT, json=pixel_params, nutritionix_headers=nutritionix_headers)
# print(response.text)

# Update an existing pixel
# response = requests.put(url=PIXEL_ENDPOINT, json=update_pixel, nutritionix_headers=nutritionix_headers)
# print(response.text)

# Delete a pixel (today’s entry)
# response = requests.delete(url=PIXEL_ENDPOINT, nutritionix_headers=nutritionix_headers)
# print(response.text)
