n=int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            break
    else:
        print("Prime number")
else:
    print("not a prime number")
