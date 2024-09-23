def sum_of_digits(n):
    s= 0
    while n> 0:
        digit = n%10
        s+= digit
        n//= 10
    return s

num=int(input("Enter a number: "))
result=sum_of_digits(num)
print(result)

        
