# if 5 > 3:  # Syntax Error
#     print("Hello")

# a = 5
# print(b)  # Name Error

#print(5/0)  # ZeroDivisionError
#print(math.pi) # ImportError

# try:
#     a = int(input("Enter a number: "))
#     print(5/a)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except NameError:
#     print("You used a variable that doesn't exist!")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("You got it right!")
finally:
    print("This is always executed!")

print("This is always executed!")
