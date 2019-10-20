x = int(input("Enter number whose cube root is to be determined:"))
ans = 0
elipson = 0.001
while ans ** 3 - x<elipson:
    ans += elipson 
if ans ** 3 - x >=elipson:
    print(str(ans) + "is the cube root of" + " ", x)
else:
    print(str(x) + "is not cube root")
