import pytest
from netmiko import ConnectHandler
import yaml
import json

with open('router_info.yaml', 'r') as f:
    devices = yaml.safe_load(f)

def test_bgp_mesh_is_established():

    for device in devices:
        router_name = device.pop('name')
        device.pop('loopback_ip', None)
        print(f'\nConnecting to {router_name} for BGP Validation')

        try:
            net_connect = ConnectHandler(**device)
            output = net_connect.send_command('show ip bgp summary json')
            bgp_dict = json.loads(output)
            hosts = bgp_dict['ipv4Unicast']['peers']
            for host, peers in hosts.items():
                assert peers['state'] == 'Established', f'BGP peer {host} is down on {router_name}!'
                assert peers['pfxRcd'] > 0 , f'WARNING: BGP peer {host} is {peers["state"]} but {peers["pfxRcd"]} prefixes received'
                assert peers['peerUptimeMsec'] > 60000, f'Stability Alert: BGP Peer recently flapped!'
            net_connect.disconnect()
        except Exception as e:
            pytest.fail(f'Could not connect to {router_name}: {e}')
        
