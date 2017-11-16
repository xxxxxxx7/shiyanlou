#!/usr/bin/env python3

import sys

arg = sys.argv[1]

try:
	if int(arg) < 3500:
		print("0")
	elif int(arg) - 3500 <= 1500:
		a = (int(arg) - 3500) * 0.03
		print(format(a,".2f"))
	elif int(arg) - 3500 >= 1500 and int(arg) - 3500 <= 4500:
		a = (int(arg) - 3500) * 0.1 - 105
		print(format(a,".2f"))
	elif (int(arg) - 3500) >= 4500 and (int(arg) - 3500) <= 9000:
		a = (int(arg) - 3500) * 0.2 - 555
		print(format(a,".2f"))
	elif int(arg) - 3500 >= 9000 and int(arg) - 3500 <= 35000:
		a = (int(arg) - 3500) * 0.25 - 1005
		print(format(a,".2f"))
	elif int(arg) - 3500 >= 35000 and int(arg) - 3500 <= 55000:
		a = (int(arg) - 3500) * 0.3 - 2755
		print(format(a,".2f"))
	elif int(arg) - 3500 >= 55000 and int(arg) - 3500 <= 80000:
		a = (int(arg) - 3500) * 0.35 - 5505
		print(format(a,".2f"))
	elif int(arg) - 3500 >= 80000:
		a = (int(arg) - 3500) * 0.45 - 13505
		print(format(a,".2f"))












except:
	print("Parameter Error")