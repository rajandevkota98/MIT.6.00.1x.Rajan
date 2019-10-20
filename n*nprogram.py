/*Program for n^2*/
num = input("Enter the number:")
interleft = num
ans = 0
while(interleft!=0):
	ans = num + ans
	interleft = interleft - 1
print("The square of number is " + str(ans))