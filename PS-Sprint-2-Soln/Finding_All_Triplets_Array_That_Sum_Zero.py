def sum_zero_array(arr):
    
    result = []
    for i in range(0,len(arr)):
        tagret = -arr[i]
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[j] + arr[k] == tagret:
                    triplet = sorted([arr[i], arr[j], arr[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

print(sum_zero_array([-1, 0, 1, 2, -1, -4]))