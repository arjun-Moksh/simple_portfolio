# OOP
## Class and Objects
1. Class is a collection of attributes (variables)and methods (functions).
2. Class can be created using the keyword 'class'.
3. Attributes are variables that belong to the class.
4. Methods are functions that belong to the class.
5. Object is an instance of a class and the process of creating an object is called instantiation.

### Defining a Class
syntax:
```
class ClassName:
    #attributes
    #methods

```

example:
```
class MyClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World")
```
### Creating an Object
syntax:
```
object_name = ClassName()
```
example:
```
class MyClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World")

a = MyClass()

print(a.x)
print(a.y)
a.my_method()

```
### Creating Multiple Objects
```
class MyClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World")

a = MyClass()

print(a.x)
print(a.y)
a.my_method()

b  = MyClass()
print(b.x)
print(b.y)
b.my_method()

a.x = 50
b.x = 100

print(a.x)
print(b.x)

```
### Class Objects
When we create an object, Python automatically creates a class object that is associated with the object.
```
class MyClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World")

print(MyClass.a)
print(MyClass.b)

```
### self Parameter
Whenever we create an object from a class, Python creates a special parameter called self.

This parameter is a reference to the current instance of the class.

When we call a method, Python passes the self parameter automatically.

self parameter in a method is a reference to the current instance of the class.

example:
```
class MyClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World")

    def my_method_2(self, num):
        print(num)

    def add_numbers(self, a, b):
        return a + b


obj = MyClass()
obj2 = MyClass()

print(obj.my_method())  #=> MyClass.my_method(obj)

obj2.my_method_2(100)  #=> MyClass.my_method_2(obj2, 100)

sum1 = obj.add_numbers(10, 20)
print(sum1)

```
## Constructors
Constructors are special methods that are automatically called when we create an object from a class.

example:
```
class MyClass:
    x = 5  # class variable
    y = 10 # class variable

    def __init__(self, a, b):
        self.a = a  #instance variable
        self.b = b  #instance variable

    def my_method(self):
        print("Hello World")

    def my_method_2(self, num):
        print(num)

    def add_numbers(self, a, b):
        return a + b

    def print_vars(self):
        print(self.a)
        print(self.b)

obj1 = MyClass(10, 20) #=> MyClass.__init__(obj1, 10, 20)
print(obj1.a)
print(obj1.b)

obj1.print_vars()
```

## Inheritance
1. Inheritance is the capability of one class to derive or inherit the properties(attributes and methods) from another class.
2. Base class => Parent class or Super class
3. Derived class => Child class or Sub class

syntax:
```
class BaseClass:
    #attributes of BaseClass
    #methods of BaseClass

class DerivedClass(BaseClass):
    #attributes of DerivedClass
    #methods of DerivedClass
```

example:
```
class BaseClass:
    x = 5
    y = 10
    def my_method(self):
        print("Hello World from BaseClass")

    def my_method_2(self, num):
        print(num)

class DerivedClass(BaseClass):
    z = 15
    def my_method_3(self):
        print("Hello World from DerivedClass")

obj1 = BaseClass()
obj1.my_method()
obj1.my_method_2(100)

obj2 = DerivedClass()
obj2.my_method()
obj2.my_method_2(700)
```
```
class quadriLateral:
    def __init__(self, a, b, c, d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)


class rectangle(quadriLateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        #quadriLateral.__init__(self,a,b,c,d)

    def area(self):
        a=self.side1 * self.side2
        print("area=",a)

class square(quadriLateral):
    def __init__(self, a):
        super().__init__(a, a, a, a)
        #rectangle.__init__(self,a,a,a,a)

    def area(self):
        a=self.side1 ** 2
        print("area=",a)

r1=rectangle(10, 20)
r1.perimeter()
r1.area()

s1=square(10)
s1.perimeter()
s1.area()

```


## Namespaces
Name (also called identifier) is a name given to an object.

Everything in Python is an object.

Name is a way to access an object.

```
a = 2
print('id(2) = ',id(2))
print('id(a) = ',id(a))

b = 2
print('id(2) = ',id(2))
print('id(b) = ',id(b))


a = [1,2,3]
print('id(a) = ',id(a))

b = [1,2,3]
print('id(b) = ',id(b))

c = a
print('id(a) = ',id(a))
print('id(c) = ',id(c))

s = 'Hello'
print('id(s) = ',id(s))
w = 'Hello'
print('id(w) = ',id(w))

#Functions are also objects

def print_hello():
    print('Hello')

a = print_hello

a() #=> Hello

```
