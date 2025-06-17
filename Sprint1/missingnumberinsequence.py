sequence=[1,2,4,5]
n=len(sequence)+1
missing=n*(n+1)//2
missingval=missing-sum(sequence)
print(missingval)
