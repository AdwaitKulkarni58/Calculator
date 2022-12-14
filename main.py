def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for operation in operations:
    print(operation)

user_choice = input("Choose an operation from the above options: ")

function_chosen = operations[user_choice]
result = function_chosen(num1, num2)

print(f"{num1} {user_choice} {num2} = {result}")