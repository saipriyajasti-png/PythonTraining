marks=int(input("enter your marks: "))
if(marks>=0 and marks<=100):
    if(marks>=75):
        print("distinction")
    elif(marks>=60 and marks<75):
        print("first class")
    elif(marks>=50 and marks<60):
        print("second class")
    elif(marks>=35 and marks<50):
        print("pass")
    else:
        print("fail")
else:
    print("Invalid input")