# Simple Python Calculator

# Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose an operation
print("Select operation: +, -, *, /")
operation = input("Enter operation: ")

# Perform calculation using conditions
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"

# Display the result
print("Result:", result)