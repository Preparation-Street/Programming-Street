array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum=array[0]
current_sum=array[0]
for num in array[1:]:
    current_sum=max(num,current_sum+num)
    max_sum=max(max_sum,current_sum)
print(max_sum)