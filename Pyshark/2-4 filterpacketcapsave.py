import pyshark
capsav = pyshark.LiveCapture(interface="Wi-Fi",bpf_filter="icmp")
capsav.sniff(packet_count=5)







print (capsav[1].sniff_time)
print ("Frame info Time: ", capsav[1].frame_info.time)
print (capsav[1].sniff_timestamp)
print (capsav[1].ip.dst)

"""
for packet in capsav.sniff_continuously(packet_count=5):
    print("Just Arrived: ", packet.eth.addr)
    
    print("IP in packet: ", 'IP' in packet)
    
    if ('ICMP' in packet) == True:
        print("->IP Source:      ", packet.ip.addr)
        print("->IP Destination: ", packet.ip.dst)
    else:
        print("NO IP ADDRESS IN PACKET")
"""
