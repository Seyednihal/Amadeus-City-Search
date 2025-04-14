import requests
import json
from base64 import b64encode

# Replace with your actual API credentials
client_id = '*****************'
client_secret = '************'
# Encode credentials for authentication
credentials = f"{client_id}:{client_secret}"
encoded_credentials = b64encode(credentials.encode()).decode()

# Step 1: Get access token
auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
auth_headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
auth_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)

if auth_response.status_code == 200:
    access_token = auth_response.json()['access_token']
    print("Access token generated successfully.")

    # Step 2: Use City Search API
    city_search_url = "https://test.api.amadeus.com/v1/reference-data/locations"
    city = "Paris"  # You can change the city name

    search_headers = {
        "Authorization": f"Bearer {access_token}"
    }

    search_params = {
        "keyword": city,
        "subType": "CITY,AIRPORT"
    }

    search_response = requests.get(city_search_url, headers=search_headers, params=search_params)

    if search_response.status_code == 200:
        results = search_response.json()
        print("\nCity Search Results:")
        print(json.dumps(results, indent=4))
    else:
        print(f"City search failed: {search_response.status_code}")
        print(search_response.text)
else:
    print(f"Failed to get access token: {auth_response.status_code}")
    print(auth_response.text)
