import requests

# Define OAuth credentials
client_id = "your_client_id"
client_secret = "your_client_secret"
oauth_token_url = "https://oauth.example.com/token"

# Request OAuth token
token_response = requests.post(
    oauth_token_url,
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
)

if token_response.status_code == 200:
    access_token = token_response.json()["access_token"]
    # Define API endpoint and parameters
    url = "https://www.flickr.com/services/api/flickr.photos.getPopular.html"
    params = {"param1": "value1", "param2": "value2"}

    # Make the authorized API call
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, params=params, headers=headers)

    # Validate the status code
    if response.status_code == 200:
        print("API call successful")
        # Validate JSON response structure and data here
        response_data = response.json()
        if "key" in response_data and "nested_key" in response_data["key"]:
            print("Response structure and data are as expected")
        else:
            print("Response structure or data is unexpected")
    else:
        print(f"API call failed with status code {response.status_code}")
else:
    print("OAuth token request failed")
