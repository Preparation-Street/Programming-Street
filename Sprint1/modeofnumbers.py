array=[1, 2, 2, 3, 4, 4, 4]
count1={}
for num in array:
    if num in count1:
        count1[num]+=1
    else:
        count1[num]=1
maxfreq=max(count1.values())
for num,freq in count1.items():
    if freq == maxfreq:
        print(num)