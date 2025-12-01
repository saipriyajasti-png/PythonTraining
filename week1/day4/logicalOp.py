a=int(input("enter a number: "))
b=int(input("enter another number: "))
if(a>0 and b>0):
    print("both numbers are positive")
elif(a>0 or b>0):
    print("either of the numbers are positive")
else:
    print("neither of them are positive")