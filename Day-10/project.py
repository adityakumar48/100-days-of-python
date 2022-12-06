from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
is_true = True

while is_true:
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))

    def OperationFunction(num1, num2, operation_symbol):
        function = operations[operation_symbol]
        answer = function(num1, num2)
        return f"{num1} {operation_symbol} {num2} = {answer}"

    print(OperationFunction(num1, num2, operation_symbol))

    another_continue = input("You wanna do more calculations? yes or no\n")
    if(another_continue == "no"):
        is_true = False
        print("Goodbye")
    elif another_continue == "yes":
        is_true = True
