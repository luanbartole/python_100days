import requests

# Parameters for the API request: 23 True/False questions
params = {
    "amount": 23,
    "type": "boolean"
}

# Send GET request to Open Trivia DB API
response = requests.get(url="https://opentdb.com/api.php?", params=params)
response.raise_for_status()  # Raise an error if the request fails

# Extract the list of questions from the API response
new_question_data = response.json()["results"]
