import math
sequence = [1, 2,3, 4,5,6,8]
n = len(sequence)+1
expected_sum = n*(n+1)//2
actual_sum = sum(sequence)

missing_no = expected_sum - actual_sum
print(missing_no)