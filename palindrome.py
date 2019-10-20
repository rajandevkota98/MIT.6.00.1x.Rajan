def pal(num):
	x = num
	sum = 0
	while num> 0:
		rem = n % 2
		num = num/10
		sum += sum*10 + rem
	return sum
x = pal(22522)