def recurPower(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*recurPower(base,exponent-1)
print("The recor power of" +str(recurPower(2,3)))
	