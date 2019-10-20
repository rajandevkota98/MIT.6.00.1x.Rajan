num = int(input("Enter Decimal Number:")
i =0
x = num
if num > 0:
	num = num
elif num < 0:
	num = abs(num)
result = 0
while num > 0:
	q = num/2
	r = mum//2
	num = q
	result+ = r*i
	i*= 10
print("The binary of decimal" + str(x) + " is " + str(result))