x = int(input("Enter the number:"))
elipson = 0.0001
new_guess = x
while new_guess*new_guess - x >=elipson:
	new_guess = (new_guess + x/new_guess)/2
if new_guess*new_guess - x <=elipson:
	print("Square root is" + " " + "str(new_guess))