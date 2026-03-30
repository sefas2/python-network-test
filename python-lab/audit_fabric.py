from netmiko import ConnectHandler
import yaml
import json

def audit_router(device_dict):
    router_name = device_dict.pop('name')
    print(f"\n=== Auditing {router_name} ===")

    try:
        net_connect = ConnectHandler(**device_dict)
        output = net_connect.send_command('show ip bgp summary json')
        bgp_dict = json.loads(output)
        bgp_peers = bgp_dict['ipv4Unicast']['peers']
        bgp_peers = bgp_dict['ipv4Unicast']['peers']
        for peer_ip, peer_info in bgp_peers.items():
            current_state = peer_info['state']
            if current_state == "Established":
                print(f'PASS: Neighbor {peer_ip} is UP state:{current_state}')
            else:
                print(f'CRITICAL: Neighbor {peer_ip} is DOWN state: {current_state}')
            print("========================")
        net_connect.disconnect()
    except Exception as e:
        print(f"CRITICAL: Could not connect to {router_name}. Error: {e}")


if __name__ == "__main__":
    
    with open('router_info.yaml', 'r') as f:
        datacenter_routers = yaml.safe_load(f)
    print("Initiating Datacenter BGP Audit...")
    for target_router in datacenter_routers:
        audit_router(target_router)
        
    print("\nAudit Complete!")