def iterPower(base, exp):
	result= 1
	while exp>0:
		result *= base
		exp-=1
	return result
x = input("Enter the number")
y= int(input("Enter the number"))
print("The iterpower is"  + str(iterPower(x,y)))