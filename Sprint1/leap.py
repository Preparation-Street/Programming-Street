year=int(input("Entera year"))
if year%4 ==0 and year%100!=0 or year%400==0:
    print("Leap")
else:
    print("Not leap")