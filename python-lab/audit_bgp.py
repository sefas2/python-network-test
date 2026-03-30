from netmiko import ConnectHandler
import yaml
import json

with open('router_info.yaml', 'r') as f:
    router_login = yaml.safe_load(f)

print('Connecting to switch-01')
net_connect = ConnectHandler(**router_login)
print('Pulling BGP state...')
output = net_connect.send_command('sh ip bgp summary json')
bgp_dict = json.loads(output)
bgp_peers = bgp_dict['ipv4Unicast']['peers']

for peer_ip, peer_info in bgp_peers.items():
    current_state = peer_info['state']
    if current_state == "Established":
        print(f'PASS: Neighbor {peer_ip} is UP state:{current_state}')
    else:
        print(f'CRITICAL: Neighbor {peer_ip} is DOWN state: {current_state}')
    
    print("========================")

net_connect.disconnect()