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

def calculate():
    num1 = int(input("Enter the first number: "))
    want_to_continue = True

    while want_to_continue:
        for operation in operations:
            print(operation)

        user_choice = input("Choose an operation from these options: ")

        num2 = int(input("Enter the second number: "))

        function_chosen = operations[user_choice]
        result = function_chosen(num1, num2)

        print(f"{num1} {user_choice} {num2} = {result}")

        calculate_again = input(f"Enter y to continue with {result}, or 'n' to stop calculation: ")
        if (calculate_again == "y"):
            num1 = result
        else:
            want_to_continue = False
calculate()
