list = []
odd_list=[]
for i in range(1, 5):
    number = int(input('Enter integer' + str(i) +':'))
    list.append(number)
for i in range(len(list)):
    if(list[i]%2!= 0):
        odd_list.append(list[i])
if(len(odd_list) == 0):
	print('No odd number entered")
else:
	print('The maximum odd number is',max(odd_list))