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

while True:
    user_choice = input("Choose an operation from the above options: ")

    function_chosen = operations[user_choice]
    result = function_chosen(num1, num2)
    
    print(f"{num1} {user_choice} {num2} = {result}")

    new_operation = input("Choose another operation: ")

    num3 = int(input("Enter another number: "))

    new_operation_chosen = operations[new_operation]
    new_result = new_operation_chosen(result, num3)

    print(f"{result} {new_operation} {num3} = {new_result}")
    calculate_again = input(f"Enter y to continue with {new_result}, or 'n' to stop calculation: ")
    if (calculate_again == "n"):
        break
    else:
        continue