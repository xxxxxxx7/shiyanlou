#!/usr/bin/env python3

import sys

#arg = sys.argv[1]

try:
	if (len(sys.argv)) < 1:
            raise ValueError

	for arg in sys.argv[1:]:
		a = arg.split(':')
		b = float(a[1]) * 0.165

		if int(a[1]) - b < 3500:
			d = int(a[1]) - b
		elif int(a[1]) - 3500  <= 1500:
			c = (int(a[1]) - 3500 - b) * 0.03
			d = int(a[1]) - b - c
		elif int(a[1]) - 3500 >= 1500 and int(a[1]) - 3500 <= 4500:
			c = (int(a[1]) - 3500 -b) * 0.1 - 105
			d = int(a[1]) - b - c
#			print(format(a,".2f"))
		elif (int(a[1]) - 3500) >= 4500 and (int(a[1]) - 3500) <= 9000:
			c = (int(a[1]) - 3500 -b) * 0.2 - 555
			d = int(a[1]) - b - c
#			print(format(a,".2f"))
		elif int(a[1]) - 3500 >= 9000 and int(a[1]) - 3500 <= 35000:
			c = (int(a[1]) - 3500 -b) * 0.25 - 1005
			d = int(a[1]) - b - c
#			print(format(a,".2f"))
		elif int(a[1]) - 3500 >= 35000 and int(a[1]) - 3500 <= 55000:
			c = (int(a[1]) - 3500 -b) * 0.3 - 2755
			d = int(a[1]) - b - c
#			print(format(a,".2f"))
		elif int(a[1]) - 3500 >= 55000 and int(a[1]) - 3500 <= 80000:
			c = (int(a[1]) - 3500 -b) * 0.35 - 5505
			d = int(a[1]) - b - c
#			print(format(a,".2f"))
		elif int(a[1]) - 3500 >= 80000:
			c = (int(a[1]) - 3500 -b) * 0.45 - 13505
			d = int(a[1]) - b - c
		
		print(a[0]+":"+format(d,".2f"))












except:
	print("Parameter Error")
