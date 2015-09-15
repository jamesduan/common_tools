
print [x * x for x in range(1, 11) if x % 2 ==0 ]
print [ m + n for m in 'ABC' for n in 'XYZ']

for m in 'ABC':
	for n in 'XYZ':
		print m+n

############################

import os

print [ d for d in os.listdir('.')]
d = {'x': 1, 'y':2, 'z':3}
print [ key + '=' + str(val) for key,val in d.items()]


