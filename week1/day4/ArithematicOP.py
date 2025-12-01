a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
op=int(input("select an option number\n1.add 2.sub 3.multiply 4.divide : "))
match(op):
    case 1:
        print("sum is",(a+b))
    case 2:
        print("difference is",(a-b))
    case 3:
        print("product is",(a*b))
    case 4:
        print("division is",(a/b))
    case _:
        print("Invalid option")