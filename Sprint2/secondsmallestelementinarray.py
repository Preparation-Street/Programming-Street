array = [12, 13, 1, 10, 34, 1]
if len(array)<2:
    print('None')
first,second=float('inf'),float('inf')
for num in array:
    if num<first:
        second=first
        first=num
    elif first<num<second:
        second=num
if second!=float('inf'):
    print(second)