
import psutil

print psutil.cpu_times().user
print psutil.cpu_times().nice
print psutil.cpu_times().system
print psutil.cpu_times().idle
print psutil.cpu_times().iowait
print psutil.cpu_times().irq
print psutil.cpu_times().softirq
print psutil.cpu_times().steal
print psutil.cpu_times().guest
print psutil.cpu_times().nice

for i in  psutil.cpu_times_percent(interval=1, percpu=True):
	print i

print "cpu numbers: ", psutil.cpu_count(logical=True)


