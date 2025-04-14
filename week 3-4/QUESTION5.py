#making different functions for different arithmetic operations
def add(a,b):
    #returns the addition of a and b
    return a+b

def subtract(a,b):
    #returns the subtraction of b from a
    return a-b

def multiply(a,b):
    #returns the multiplication of a and b
    return a*b

def divide(a,b):
    #returns the division of a by b; raises error if b is zero
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a/b

def truncated_division(a,b):
    #returns the truncated (integer) division of a by b; raises error if b is zero
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a//b

def modulus(a,b):
    #returns the modulus (remainder) of a divided by b; raises error if b is zero
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a%b

def exponentiation(a,b):
    #returns a raised to the power of b.
    return a**b


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))
    print("Truncated Division:", truncated_division(a, b))
    print("Modulus:", modulus(a, b))
    print("Exponentiation:", exponentiation(a, b))
except ValueError as e:
    print("Error:", e)