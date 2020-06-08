import os
import pyshark
c = pyshark.LiveCapture(interface="Wi-Fi")
fo = open("packetcapture.txt", "w")

for packet in c.sniff_continuously(packet_count=50):
    #print("Just Arrived: ", packet.eth.addr)
    fo.write("MAC: ")
    fo.write(packet.eth.addr)
    fo.write(" SRC IP: ")
    fo.write(packet.ip.addr)
    fo.write(" DST IP: ")
    fo.write(packet.ip.dst)
    #textstuff = packet.pretty_print()
    #fo.write(textstuff)
    fo.write("\n")

textstuff = 'Python is a great language.'
"""
fo.write(textstuff)
"""
print("File Just Created: ", fo.name)

# Close opend file
fo.close()
