#to count the no of charecters in a given strings and hence to display the charecters of string in reverse order

def rev(n):
    str=""
    for i in n:
        str=i+str
        return str
n="welcome to SDMIT"
count=0
for i in n:
    count=count+1
    print(count)
    print("original string is",end="")
    print(n)
    print("reversed string is",end="")
print(rev(n))
