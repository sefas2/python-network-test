import requests
import json

def test_local_api():
    print("Sending API GET request to Local Docker API...")

    url = "http://localhost:8080/get"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\n Success! Connected to the local REST API.\n")
            
            api_data = response.json()
            print(json.dumps(api_data, indent=4))
            
        else:
            print(f" API Call Failed. Status Code: {response.status_code}")

    except Exception as e:
        print(f"Critical Failure: {e}")
test_local_api()
