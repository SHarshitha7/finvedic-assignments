def reverse(string):
    rev_str=" "
    for i in string:
        rev_str=i+rev_str
    print(rev_str)

string=input("Enter a string: ")
reverse(string)
