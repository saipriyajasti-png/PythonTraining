def nthFibo(n):

    if n <= 1:
        return n

    return nthFibo(n - 1) + nthFibo(n - 2)

if __name__ == "__main__":
    n = int(input("enter a number: "))
    result = nthFibo(n)
    print(result)