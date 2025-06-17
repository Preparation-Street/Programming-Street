string = "abab"
n=len(string)
for i in range(1,n//2+1):
    if n%i==0:
        substring=string[:i]
        if substring*(n//i)==string:
            print("T")
else:
    print("False")