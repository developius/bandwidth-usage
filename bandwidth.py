import os
from subprocess import Popen,PIPE,STDOUT,call

proc=Popen('cat /proc/net/dev', shell=True, stdout=PIPE, )
output=proc.communicate()[0]

print("eth0 (R):")
print("		Bytes: %i Packets: %i" % (int(output[455:464]), int(output[465:472])))
print("eth0 (T):")
print("		Bytes: %i Packets: %i" % (int(output[517:526]), int(output[527:534])))
