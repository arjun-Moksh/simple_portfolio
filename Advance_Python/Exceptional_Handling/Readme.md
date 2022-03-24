# Exception Handling

## Exceptions
Errors are the result of something that went wrong.

Type of errors:
1. Syntax errors
2. Name errors
3. Runtime errors (exceptions)


example:
```
if 5 > 3  # Syntax Error
    print("Hello")

a = 5
print(b)  # Name Error
```
Errors that occur during runtime are called exceptions.

example:

ZeroDivisionError: division by zero

ImportError: No module named 'my_module'

example:
```
print(5/0)  # ZeroDivisionError
print(math.pi) # ImportError
```

## Exceptional Handling
### try...except
try is used to execute a block of code that might raise an exception.<br>
except is used to specify what to do if the exception occurs.
```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```
### try...except...else
try...except...else is used to execute a block of code, and if the code doesnot raises an exception, the else block is executed.
```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("You got it right!")
```
### try...except...else...finally
try...except...else...finally is used to execute a block of code, and if the code doesnot raises an exception, the else block is executed, then the finally block is always executed no matter what.
```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("You got it right!")
finally:
    print("This is always executed!")
```
