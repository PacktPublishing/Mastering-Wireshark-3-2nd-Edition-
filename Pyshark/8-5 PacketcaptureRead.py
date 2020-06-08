import pyshark
c = pyshark.FileCapture('testexport.pcapng',display_filter="udp")

for packet in c:
    print ('>>>>>>>>>>>>>>>>>>>>>Just Read:', packet)




