def sum_odd_range(n):
    ans = 0 
    for i in range(n[0],n[1]+1):
        if i%2!=0:
            ans= ans + i
        else :
            pass
    return ans

print(sum_odd_range([1,10]))