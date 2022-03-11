a = 1
b = 2.8
sum = a + b #int a is automatically converted to float and then added to float b
print(sum)  #output: 3.8


a = 1
print(type(a)) #output: <class 'int'>
b = 1.1
print(type(b)) #output: <class 'float'>
c = 'Hello, world!'
print(type(c)) #output: <class 'str'>

a = 1
b = float(a)
print(b) #output: 1.0

print(type(b)) #output: <class 'float'>

c = '100'
print(c) #output: 100
print(type(c)) #output: <class 'str'>

d = int(c)
print(d) #output: 100
print(type(d)) #output: <class 'int'>

a = '100'
b = int(a)
print(b) #output: 100

f = '3.14'
g = float(f)
print(g) #output: 3.14

c = 'string'
d = int(c)
print(d) #output: Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: invalid literal for int() with base 10: 'string'

t = '11.1'
u = int(t)
print(u) #output: ValueError: invalid literal for int() with base 10: '11.1'
