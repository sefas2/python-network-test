from netmiko import ConnectHandler
import yaml

with open ('router_info.yaml', 'r') as f:
    devices = yaml.safe_load(f)
for device in devices:
    router_name = device.pop('name')
    loopback_ip = device.pop('loopback_ip')

    cmd = ['configure terminal', 'interface lo', f'ip address {loopback_ip}/32']
    net_connect = ConnectHandler(**device)
    print(f'Configuring device = {router_name}')
    send_command = net_connect.send_config_set(cmd)
    print(send_command)
    net_connect.disconnect()
    

        