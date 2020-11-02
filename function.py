def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
   return x/y

x = int(input('Enter x value: '))
y = int(input('Enter y value: '))
f = input('Enter function: ')
if f == 'add':
    print(add(x,y))
elif f == 'sub':
    print(sub(x,y))
elif f == 'mul':
    print(mul(x,y))
elif f == 'div':
    print(div(x,y))
