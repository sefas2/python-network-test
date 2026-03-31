import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_device_interface():
    print('Sending API GET request to Cisco Devnet Sandbox...')

    url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

    creds = ('admin', 'Cisco12345')

    headers = {
        'Accept': 'application/yang-data+json',
        'Content-type': 'application/yang-data+json'
    } 

    try:
        response = requests.get(url, auth=creds, headers=headers, verify=False)
        if response.status_code == 200:
            print('\n Success! Data received from router: \n')
            api_data = response.json()
            print(json.dumps(api_data, indent=4))
        else:
            print(f'API Call Failed. Status Code: {response.status_code}')
            print(response.text)
    except Exception as e:
        print(f'Critical Failure: {e}')

get_device_interface()