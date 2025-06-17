array = [10, 20, 4, 45, 99]
unique_array=list(set(array))
unique_array.sort(reverse=True)
if len(unique_array)>=2:
    print(unique_array[1])
else:
    print("No second largest")