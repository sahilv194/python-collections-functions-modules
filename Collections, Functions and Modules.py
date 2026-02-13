# 1️ COLLECTIONS


print("----- LIST Example -----")
numbers = [1, 2, 3, 4]
numbers.append(5)
print("List:", numbers)


print("\n----- TUPLE Example -----")
data = (10, 20, 30)
print("Tuple:", data)


print("\n----- SET Example -----")
unique_numbers = {1, 2, 3, 3}
unique_numbers.add(4)
print("Set:", unique_numbers)


print("\n----- DICTIONARY Example -----")
student = {
    "name": "Sahil",
    "age": 21,
    "course": "Python"
}
print("Dictionary:", student)
print("Student Name:", student["name"])


# 2️ FUNCTIONS


print("\n----- FUNCTION Example -----")

# User-defined function
def greet(name):
    return "Hello " + name

print(greet("Sahil"))


# Function with default argument
def add(a, b=5):
    return a + b

print("Addition:", add(10))


# Lambda function
print("\n----- LAMBDA Function Example -----")
square = lambda x: x * x
print("Square of 6:", square(6))


# Recursion Example
print("\n----- RECURSION Example -----")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))


#3 MODULES


print("\n----- BUILT-IN MODULE Example -----")

import math
print("Square Root of 16:", math.sqrt(16))


import random
print("Random Number:", random.randint(1, 10))


print("\nProgram Finished Successfully ✅")
