'''def mul(a,b):
	result = 0
	while b>0:
		result+=a
		b-=1
	print("The multiplication is" + str(result))
    return result
x = mul(5,6)'''
def mul( a,b):
	if b==1:
		return a
	else:
		return a + mul(a,b-1)
print('The multiply of 5 and 6 is '  + str(mul(5,6)))