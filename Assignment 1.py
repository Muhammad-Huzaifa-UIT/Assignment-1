print("Muhammad Huzaifa")
print("Assignment #1")


print("Question #1:-Write a Python program to print the following string in a specific format(see the output).")
print("")
print("\t\tTwinkle, twinkle, little star,\n"
"\t\t\tHow I wonder what you are!\n"
"\t\t\t\tUp above the world so high,\n"
"\t\t\t\tLike a diamond in the sky.\n"

"\t\tTwinkle, twinkle, little star,\n"
"\t\t\tHow I wonder what you are\n")

print("")
print("Question #2:-Write a Python program to get the Python version you are using")
print("")
import platform
print("You are using the following version of Python = ",platform.python_version())

print("")
print("Question #3:-Write a Python program to display the current date and time.")
print("")
from datetime import datetime
x = datetime.now()
print(x)

print("")
print("Question #4:Write a Python program which accepts the radius of a circle from the user and compute the area.")
print("")
from math import pi
c = int(input("Enter the circumference of the circle = "))
rad = c / (2*pi)
print(rad)
print("")
print("Now for the area of the circle")
area = pi*(rad**2)
print("The area of the circle is = ",area)

print("")
print("Question #5:-Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.")
print("")
fname = str(input("Enter First name: "))
lname = str(input("Enter Last name: "))
print(lname,fname)

print("")
print("Question #6:-Write a python program which takes two inputs from user and print them addition")
print("")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a+b)
