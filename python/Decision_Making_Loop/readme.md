

Decision Making And Loop
Boolean Expression
Boolean expressions are used to evaluate conditions. It is used to determine if a condition is true or false. example:

a = 5
b = 10
c = a > b #Boolean expression which evaluates to False



Comparison Operators
There are six comparison operators in Python. They are used to compare two values.

== : equal to
!= : not equal to
< : less than
'>' : greater than
<= : less than or equal to
'>=' : greater than or equal to
example:

x = 5
y = 10

print(x == y) # False
print(x != y) # True
print(x < y) # True
print(x > y) # False
print(x <= y) # True
print(x >= y) # False
Logical Operators
Logical operators are used to combine conditional statements and evaluate conditions.



Operator	Description
and	If both the operands are true then condition becomes true.
or	If any of the two operands are true then condition becomes true.
not	used to reverse the result.
example:

#and operator
x = 5
y = 10
z = 10

print(x == y and x == z) # False
print(x == y and x != z) # False
print(x == y and x < z) # True

#or operator

print(x == y or x == z) # True
print(x == y or x != z)  # True
print(x == y or x < z) # True

#not operator
print(not(x == y)) # False
print(not(x == z)) # True



If..else statement
if..else statement is used to execute a block of code if a condition is true, otherwise it will execute a different block of code.

if
syntax:

if condition:
    statement(s)
example:

x = 5
y = -1

if x > 0:
    print('x is positive')

print('This is always executed')

if y > 0:
    print('x is positive')

print('This is always executed')



if...else
syntax:

if boolean_expression:
    statement(s)
else:
    statement(s)
example:

x = -1

if x >= 0:
    print('x is positive or zero')

else:
    print('x is negative')

print('This is always executed')



if...elif...else
syntax:

if boolean_expression:
    statement(s)
elif boolean_expression:
    statement(s)
else:
    statement(s)
example:

x = -1

if x > 0:
    print('x is positive')
elif x == 0:
    print('x is zero')
else:
    print('x is negative')

print('This is always executed')




Nesting if...else
if...else statement inside another if...else statement is called as nested if...else statement. syntax:

if boolean_expression:
    if boolean_expression:
        statement(s)
    else:
        statement(s)
else:
    statement(s)
example:

num  = float(input('Enter a number: '))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')



While loop
while loop is used to execute a block of code as long as the condition is true. syntax:

while boolean_expression:
    statement(s)
example:

n = 3
i = 1
while i <= n:
    print(i)
    i = i + 1

#infinite loop
while i <= n:
    print(i)


For loop
for loop is used to iterate over a sequence (e.g., string, tuple, list) and execute a block of code for each element.
syntax:

for element in sequence:
    statement(s)
Sequence
String => It is a sequence of characters.
Lists => It is a sequence of items.
range() => It is used to create sequence of integers.
example:


#string
a = "Python"
for letter in a:
    print('Current Letter:', letter)

#lists
a = [1, 2, 3]
b = ['Python', 'JavaScript', 'C++']

for ele in a:
    print('Current Element:', ele)

for language in b:
    print('Current language:', language)

#range()

numbers = list(range(1, 10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for num in numbers:
    sum = sum + num

print('Sum :', sum)



Break and continue statement
break statement is used to terminate the loop.

syntax:

break
example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        break
    print(num)



continue statement is used to skip the remaining statements of the loop.

syntax:

continue
example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 5:
        continue
    print(num)



    
Pass statement
pass statement is used when a statement is required syntactically but you do not want any command or code to execute.

syntax:

pass
example:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    pass
