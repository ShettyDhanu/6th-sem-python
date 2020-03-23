#to generate first n fibonacci number and factorial of n using function

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    def fib(n):
        a=0
        b=1
        if(n<0):
            print("it should be >0")
        elif(n==0):
            return a
        elif(n==1):
            return b
        else:
            for i in range(2,n):
                c=a+b
                a=b
                b=c
                return b
n=int(input("enter the number"))
f=fact(n)
print("{}!={}.format(n,f)")
print("fibonacci number")
print(fib(n))
