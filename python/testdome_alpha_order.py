def AlphabetSoup(str): 

    # code goes here
    
    L = [s for s in str]
    print (L)
    for i in xrange(len(L)-1):
        print (i)
        for j in xrange(len(L)-1):
            if L[j] > L[j+1]:
                tmp = L[j]
                L[j] = L[j+1]
                L[j+1] = tmp
    
    
    return ''.join(L)
    
# keep this function call here  
print AlphabetSoup("cbtdoga")