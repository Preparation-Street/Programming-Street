def prefect_numbers(n):
  
   ans =0
   for i in range(1,n):
       if n%i==0:
         ans= ans + i
         i+=1
       else :
         i+=1
         pass 
       
   if ans==n:
     print("Perfect Numbers")
   else:
     print("Not a Perfect Number")



print(prefect_numbers(28))
print(prefect_numbers(15))