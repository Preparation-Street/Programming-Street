array=[3,1,2,4,5]
array.sort()
n=len(array)
mid=n//2
if n%2==1:
    median=array[mid]
else:
    median=(array[mid-1]+array[mid])/2
print("Median",median)