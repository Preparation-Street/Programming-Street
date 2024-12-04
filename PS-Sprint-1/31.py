def NcR(n,r):
    res =1
    for i in range (r):
        res =res* (n-i)
        res = res//(i+1)
    return res

n=10
r=3    
print(NcR(10,3))