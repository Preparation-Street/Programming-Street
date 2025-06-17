number=5
def fibonacci(number):
    if number<0:
        return ""
    if number==0:
        return 0
    if number==1:
        return 1

    return fibonacci(number-1)+fibonacci(number-2)
for i in range(number):
    print(fibonacci(i),end=" , ")
