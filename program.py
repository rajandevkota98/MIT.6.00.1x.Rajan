print('pokhara')
x = int(input("Enter the number"))
ans= 0
while ans**4<x:
 ans+=1
 
if ans**4==x:
 print(str(x)+ ' '+ 'is' + ' ' +'Perfect fourth root' + ' ' + str(ans))
else:
    print(str(x)+ ' '+ 'is not a' + ' ' +'Perfect fourth root')