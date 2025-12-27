import random
def random_matrx(rows, columns):
    total_matrix = rows*columns
    
    for i in range(0, rows):
        for j in range(0,columns):
            num = random.randint(1,9)
            print(num, end=" ")
        print()
random_matrx(3,4)