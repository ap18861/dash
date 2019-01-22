from __future__ import print_function
from collections import OrderedDict
import psutil, platform, subprocess, pprint

#Show platform 
print(platform.uname())
print(platform.linux_distribution())

#show cpu family

output = subprocess.check_output("cat /proc/cpuinfo", shell=True)
# cpu_output = Ordereddict()
# print(cpu_output)
#show cpu temp
cpu_temp = psutil.sensors_temperatures()
core1 = cpu_temp['coretemp'][1]
core2 = cpu_temp['coretemp'][2]

print("{}:          {}".format(core1[0],core1[1]))
print("{}:          {}".format(core2[0],core2[1]))

#show cpu count
cpu_count = psutil.cpu_count()
print("CPU Count:       {}".format(cpu_count))

#show memory
mem = list(psutil.virtual_memory())
total_memory = psutil.virtual_memory().total / (1024**2) * .001 # Putting it in Human readable format and thenmoving the decimal point 3 spaces.

print("Memory Percent:  {}%".format(mem[2])) # print percent of memory used
print("Memory Used:     {} GB".format(mem[3]/ (1024**2) * .001))
print("Memory Free:     {} GB".format(mem[4]/ (1024**2) * .001))
print("Total Memory:    {} GB".format(total_memory)) # print total memory

#show disk
disk_percent = psutil.disk_usage('/')[3]
hdd_disk = list(psutil.disk_usage('/'))
print("Disk Percent:    {}%".format(disk_percent)) # print disk usage percentage
print("Disk Used:       {} GB".format(hdd_disk[1] / (1024**2) * .001))
print("Disk Free:       {} GB".format(hdd_disk[2] / (1024**2) * .001))
print("Total Disk:      {} GB".format(hdd_disk[0] / (1024**2) * .001))
# print(psutil.cpu_count())
