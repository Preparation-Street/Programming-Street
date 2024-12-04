def longpal(string):
    res = ""
    
    for i in range (len(string)):
        temp = check(string,i,i )
        if len(temp)> len(res):
            res = temp
        temp = check(string,i,i+1 )
        if len(temp)> len(res):
            res = temp   
                 
    return res            

def check(string, l, r):
    while l>0 and r<len(string) and string[l] == string [r]:
        l -=1
        r +=1
    return string[l+1:r]    

string = "ababadcmadam"
print(longpal(string))