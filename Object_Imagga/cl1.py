import requests
import json

# Define the URL for the Imagga API endpoint for fetching tags

url = "https://api.imagga.com/v2/tags"

# Set the query parameters for the API request, including the image URL

querystring = {#enter the image link address you would like to recognize
    "image_url": "https://hips.hearstapps.com/hmg-prod/images/headshot-of-giraffe-sabi-sands-game-reserve-royalty-free-image-1573571300.jpg?crop=1.00xw:0.334xh;0,0.101xh&resize=1200:*"
}

# Define the headers for the API request, including the authorization header with encoded API credentials

headers = {
    "accept": "application/json",
    "authorization": "enter your imagga authorization key here"
}
# Make a GET request to the Imagga API
response = requests.get(url, headers=headers, params=querystring)
data = json.loads(response.text)

# Check if the response contains the expected structure
if "result" in data and "tags" in data["result"]:
    for tag_info in data["result"]["tags"]:
        confidence = tag_info.get("confidence", 0)
        if confidence > 80:
            tag = tag_info["tag"]["en"]
            print(f"Tag: {tag}, Confidence: {confidence}")
else:
    print("Unable to fetch tags.")
