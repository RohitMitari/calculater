def add(a,b):
    return a+b
def multi(a,b):
    return a*b
def sub(a,b):
    return a-b
def division (a,b):
    return a/b

a=int(input('enter a no:'))
B=int(input('enter other no:'))
c=input('enter the operator:))
if c=='+':
    print(add(a,b))
if c=='-':
    print(sub(a,b))
if c=='*':
    print(multi(a,b))
if c=='/':
    print(division(a,b))
