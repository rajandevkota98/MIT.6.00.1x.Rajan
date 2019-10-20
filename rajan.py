def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newtuple= ()
    for i in len(aTup):
        if i%2 == 0:
            newtuple =newtuple+ aTup[i,]
    return newTuple
x= ('a','b','c','d','e','7')
print(oddTuples(x))
