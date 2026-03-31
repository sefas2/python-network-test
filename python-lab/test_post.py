import requests

def test_local_post():
    url = 'http://localhost:8080/post'
    new_bgp_neighbor = {
        'neighbor_ip' : '10.0.0.99',
        'remote_as' : '65099',
        'description': 'new neighbor'
    }

    headers = {
        'Authorization' : 'Bearer super_secret_token_123'
    }

    try:
        response = requests.post(url, json=new_bgp_neighbor, headers=headers)
        if response.status_code == 200:
            print(response.json())
        else:
            print('Failed! - status code: {response.status_code}')
    except Exception as e:
        print('Critical Fail: {e}')

test_local_post()