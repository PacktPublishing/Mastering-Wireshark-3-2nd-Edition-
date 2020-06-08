import pyshark
c = pyshark.LiveCapture(interface="Wi-Fi")
"""
c.sniff(packet_count=20)
Represents a live capture on a network interface.
"""

for packet in c.sniff_continuously(packet_count=5):
    print("Just Arrived: ", packet.eth.addr)
    """
    print("IP in packet: ", 'IP' in packet)
    """
    if ('IP' in packet) == True:
        print("->IP Source:      ", packet.ip.addr)
        print("->IP Destination: ", packet.ip.dst)
    else:
        print("NO IP ADDRESS IN PACKET")

    
fo = open("outputtest.txt", "w")
print("Name of file: " , fo.name)
fo.write("Python is awesome!")
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
print("Python is great!","Isn't it?")
fo.close()
