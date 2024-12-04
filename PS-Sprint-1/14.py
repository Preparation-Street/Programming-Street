array = [4, 7, 1, 8, 5]
larger = [array[0]]
smaller = [array[0]]
for i in array:
    if i>larger[0]:
        larger[0] = i
    if i<smaller[0]:
        smaller[0] = i
print(larger[0])
print(smaller[0])            