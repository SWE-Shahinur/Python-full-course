x=lambda a,b: a*b+b*4
print(x(2,3))


def subcribe(n):
    return lambda a:a+n
x=subcribe(2)
y=subcribe(3)
print(x(2))
print(y(2))
