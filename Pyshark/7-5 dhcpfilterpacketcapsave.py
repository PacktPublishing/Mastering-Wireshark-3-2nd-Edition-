import pyshark
capsav = pyshark.LiveCapture(interface="Wi-Fi",bpf_filter="udp port 67 or udp port 68")



print ("Begin Capture")
print ("Waiting for DHCP packets.")

for packet in capsav.sniff_continuously(packet_count=4):
    print("Just Arrived: ", packet.eth.addr)
    print("DHCP Server IP: ", packet.dhcp.get_field('option_dhcp_server_id'))
    print("DHCP Leased IP: ", packet.dhcp.get_field('ip_your'))
    print("DHCP Option: ", packet.dhcp.get_field('option_dhcp'))
    print("DHCP Option Type: ", packet.dhcp.get_field('option_type'))
    print("DHCP FQDN: ", packet.dhcp.get_field('fqdn_name'))
    print("IP in packet: ", 'IP' in packet)


