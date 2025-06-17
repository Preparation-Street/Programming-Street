import math

number=16
def is_perfect(number):
    if number<0:
        return False
    root=math.isqrt(number)
    return root*root==number
print(is_perfect(number))