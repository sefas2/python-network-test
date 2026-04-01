import pytest
import json

def test_bgp_logic_offline():
    print("\nLoading mock router data for CI/CD validation...")
    
    with open('mock_bgp_data.json', 'r') as f:
        bgp_dict = json.load(f)
        
    hosts = bgp_dict['ipv4Unicast']['peers']
    
    for host, peers in hosts.items():
        assert peers.get('state') == 'Established', f'BGP peer {host} is down!'
        assert peers.get('pfxRcd', 0) > 0, f'WARNING: BGP peer {host} sent 0 prefixes!'
        assert peers.get('peerUptimeMsec', 0) > 60000, f'STABILITY ALERT: BGP peer {host} recently flapped!'