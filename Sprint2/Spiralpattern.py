
def spiral_matrix(n):
    matrix=[[0]*n for i in range(n)]
    left,right,top,bottom=0,n-1,0,n-1
    num=1
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            matrix[top][i]=num
            num+=1
        top+=1
        for i in range(top,bottom+1):
            matrix[i][right]=num
            num+=1
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
    return matrix

n=3
spiral=spiral_matrix(n)
for row in spiral:
    print(' '.join(str(x) for x in row))

