# Functions

## Functions (Built-in)
print(), input(), type(), range(),len(),int(),float(),string(),list(),etc. are examples of built-in functions.

## Functions (User-defined)
Function is a group of statements that performs a task.

Function is a block of code which only runs when it is called. In Python, we use the `def` keyword to create a function.

syntax:
```
#1
def function_name(parameters):
    fstatement(s)

#2
def function_name(parameter1,parameter2,...):
    fstatement(s)
    return [expression]  
```
example:
```
def greet(name):   #Function definition
    print("Hello " + name)
    print("Welcome to the world of Python")

greet("John")  #Function Call


#add two numbers
def add(a,b):
    c=a+b
    return c  #return statement is used to exit a function and return a value and go to the place where the function was called.

result=add(10,20)
print(result)

```
## Variable Scope and Lifetime
local variables:
1. variables defined inside a function are called local variables.
2. local variables are only accessible inside the function.
3. local variables are deleted once the function has finished executing.

global variables:
1. variables defined outside a function are called global variables.
2. global variables are accessible anywhere in the program.
3. global variables are deleted once the program has finished executing.
```
def my_func():
    x = 10  # x is local variable
    y = 20  # y is local variable
    print("value inside function : ", x, y)

x = 20  # x is global variable
my_func()
print("value outside function : ", x)
print(y) # y is not accessible outside the function

```

## Function arguments
Function arguments are the values passed to a function when it is called.

Three types of function arguments:
### Default arguments
Default arguments are arguments that are given a default value when the function is called.
```
def my_func(a,b=5):
    print(a,b)

my_func(3)
```

### Keyword arguments
Python allows you to call a function using keyword arguments.
```
def my_func(a,b):
    print(a,b)

my_func(a=3,b=5)
```
### Arbitrary arguments
#### *args  -  allows you to pass an arbitrary number of arguments to a function. args is a tuple.

```
def my_func(*args):
    print(args)
    print(type(args))

my_func(3,5,6,7)
```
#### **kwargs - allows you to pass an arbitrary number of keyword arguments to a function. kwargs is a dictionary.
```
def my_func(**kwargs):
    print(kwargs)
    print(type(kwargs))

my_func(a=3,b=5,c=6,d=7)
```

## Anonymous Functions / Lambda Functions
Anonymous functions are functions that are defined without a name.
Anonymous functions are also called Lambda functions.
Lambda functions are commonly used with map, filter, reduce  built-in functions.

syntax:
```
lambda arguments: expression
```

example:
```
def sum(a,b):
    return a+b

result=sum(3,5)
print(result)

sum = lambda a,b: a+b
print(sum(3,5))

```
