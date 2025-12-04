x = "Global"

def outer():
    y = "Enclosing" 
    x= "Hi" 
    def inner():
        z = "Local"  
        print(z)
        print(y)
        print(x)
    print(x)
    inner()

outer()
print(x)

