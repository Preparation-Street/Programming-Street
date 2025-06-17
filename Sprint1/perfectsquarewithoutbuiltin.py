number=16
def is_perfect(number):
    if number<0:
        return False
    i=1
    while i*i<=number:
        if i*i==number:
            return True
        i+=1
    return False
print(is_perfect(number))