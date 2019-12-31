import panda
def a ():
    print("hello world")
    x=20
    y=30
    z=x+y
    return z
a()


def b(x,y):
    sum=x+y
    return sum
add(2,3)

def c(x,y=10):
    sum=x+y
    return sum
b(20)
b(20,30)

def dyn(*x):
    print(x)
    print(type(x))
    add=0
    for i in x:
        add=add+i

    return add











