# name, age= input("Enter Name and Age").split()
# print("Name:", name)
# print("Age:", age)

# Prompt the user for input
user_input = input("Enter your name and age separated by space: ")

# Split the input into two parts
name, age = user_input.split()

# (Optional) Convert age to integer
age = int(age)

# Display result
print(f"Hello {name}! You are {age} years old.")