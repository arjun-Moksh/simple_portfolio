# Introduction

## Hello World Program

1. Create a new Python file and name it hello_world.py.
2. In the file, write a program that prints the string "Hello World!" to the screen.

```
print("Hello, world!")
```

3. Run the program by entering the following command in a terminal window:

```
python hello_world.py
```

## Variables and Literals

### Variables

A Variable is a named location in memory that can hold data of any type.
In simple terms, a variable is a named container for storing data.

#### Rules for Naming a Variable

1. A variable name must begin with a letter or the underscore character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ ).
4. Variable names are case-sensitive (age, Age and AGE are three different variables).

### Literals

A literal is raw data for representing fixed value.

#### Numeric Literals

1. Integers are whole numbers, such as 42 and -23.
   Data type: int
2. Floats are numbers with a decimal point, such as 3.14 and -273.15.
   Data type: float

3. Complex numbers are written with a + or - in front of the number, such as 3+2i and -4.5+7i.
   Data type: complex

example:

```
a = 1
b = 2.8
c = 1 + 2j
```

#### String Literals

Strings are a sequence of characters surrounded by quotation marks.We can user single or double or triple quotation marks.
example:

```
a = "Hello, world!"
b = 'Hello, world!'
name = "John"

#multiline string
c = """
This is a multiline string.
It can span multiple lines.
"""
```

#### Boolean Literals

Boolean literals are either True or False.
example:

```
a = True
b = False
```

### Comments in Python

Comments are lines of text that are ignored by the Python interpreter. <br>
Comments are useful for documenting code and for making code easier to read.
In Python a line that is a comment is denoted by the hash (#) symbol.
example:

```
# This is a comment, and will be ignored by Python
```

## Input and Output

### Output

1. The print() function is used to display text on the screen.
2. The print() function returns None.
3. The print() function can be used to display text on the screen.
   example:

```
print("Hello, world!")
```

#### Input

1. The input() function is used to prompt the user for input.
2. The input() function returns a string value.
3. The input() function can be used to prompt the user for input and store the user's response in a variable.
   example:

```
name = input("What is your name? ")
print("Hello, " + name + "!")
```

## Type Conversion

Type conversion is the process of converting one type of data to another type of data.

1. Implicit type conversion
2. Explicit type conversion

### Implicit type conversion

Implicit type conversion occurs when the variable is assigned a value of a different type.
example:

```
a = 1
b = 2.8
sum = a + b #int a is automatically converted to float and then added to float b
print(sum)  #output: 3.8
```

#### type() function

The type() function returns the type of data that a variable contains.
example:

```
a = 1
print(type(a)) #output: <class 'int'>
b = 1.1
print(type(b)) #output: <class 'float'>
c = 'Hello, world!'
print(type(c)) #output: <class 'str'>
```

### Explicit type conversion

In explicit type conversion,we use predefined functions to convert the value of one type to another type.

1. int() => converts a value to an integer
2. float() => converts a value to a floating point number
3. str() => converts a value to a string

example:

```
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
```

#### Explict type conversion rules

1. string to int and float and vice versa only works if the string can be converted to the target type. example :

```
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
```

2. int to float and vice versa

## Operators

Operators are used to perform operations on variables and values.

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators

### Arithmetic Operators

1. Addition (+)
2. Subtraction (-)
3. Multiplication (\*)
4. Division (/)
5. Modulus (%)
6. Floor Division (//)
7. Exponentiation (\*\*)

example:

```
#number operations
a = 1
b = 2.8

sum_ab = a + b
print(sum_ab) #output: 3.8

sub_ab = a - b
print(sub_ab) #output: -1.8

mult_ab = a * b
print(mult_ab) #output: 2.8

div_ab = a / b
print(div_ab) #output: 0.5

mod_ab = a % b
print(mod_ab) #output: 1

floor_div_ab = a // b
print(floor_div_ab) #output: 0

exp_ab = a ** b
print(exp_ab) #output: 1

#string operations
#concatenation
a = 'Hello, '
b = 'world!'
c = a + b
print(c) #output: Hello, world!

#multiplication
d = 'Hello, '
e = 'world!'
s = d + e
print(s * 3) #output: Hello, world!Hello, world!Hello, world!


```

### Assignment Operators

1. Assign (=)
2. Add and assign (+=)
3. Subtract and assign (-=)
4. Multiply and assign (\*=)
5. Divide and assign (/=)
6. Modulus and assign (%=)
7. Floor Division and assign (//=)
8. Exponentiation and assign (\*\*=)

example:

```
a = 1
a += 2  #a = a + 2
print(a) #output: 3

b = 1
b -= 2  #b = b - 2
print(b) #output: -1
```

### Operator Precedence

Operator precedence determines the order of operations.
Operator precedence List:

1. ()
2. \*\*
3. \*, /, //, %
4. +, -
5. > , <, >=, <=, ==, !=
6. and
7. or

example:

```
a = 1 + 2 * 3 ** 2
print(a) #output: 19

```

### Operator Associativity

Operator associativity determines the order in which operators are evaluated.
Operators with higher precedence are evaluated before operators with lower precedence.
example:

```
a = 1 + 2 * 3 ** 2
print(a) #output: 19
```
