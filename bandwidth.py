import os,sys
from subprocess import Popen,PIPE,STDOUT,call

proc=Popen('cat /proc/net/dev', shell=True, stdout=PIPE, )
output=proc.communicate()[0]
output = output.split()

if (len(sys.argv) == 2):
	if (sys.argv[1] == "ethernet"):
		eth_t_bytes = output[55]
		eth_t_packets = output[56]
		eth_r_bytes = output[63]
        	eth_r_packets = output[64]
		print("eth (R):")
                print("		Bytes: %i Packets: %i" % (int(eth_r_bytes),int(eth_r_packets)))
                print("eth (T):")
                print("		Bytes: %i Packets: %i" % (int(eth_t_bytes),int(eth_t_packets)))

	if (sys.argv[1] == "wifi"):
		wlan_t_bytes = output[29]
		wlan_t_packets = output[30]
		wlan_r_bytes = output[21]
	        wlan_r_packets = output[22]
		print("wlan (R):")
		print("		Bytes: %i Packets: %i" % (int(wlan_r_bytes),int(wlan_r_packets)))
		print("wlan (T):")
                print("		Bytes: %i Packets: %i" % (int(wlan_t_bytes),int(wlan_t_packets)))

else:
	print "Usage: python %s <wifi/ethernet>" % str(sys.argv[0])
