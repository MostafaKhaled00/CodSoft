# CodSoft python internship
# Mostafa Khaled Mostafa
# A5 Batch
# calculator task

# Features:
# 1. add / subtract
# 2. multiply/divide
# 3. handle zero


def add(num1, num2):
    return float(num1) + float(num2)


def subtract(num1, num2):
    return float(num1) - float(num2)


def multiply(num1, num2):
    return float(num1) * float(num2)


def divide(num1, num2):
    if float(num2) == 0:
        return "Cannot divide by zero"
    return float(num1) / float(num2)


def exit_prog():
    print("Thank you for using my application!")
    exit()


while True:
    print("\n*******************************")
    print(" Simple Calculator application")
    print("*******************************")
    print("-->> Type 'exit' to end the program\n")
    calculation = input("Enter two numbers separated by an operation to calculate (eg. 10 * 2 ): ")
    calc_sep = calculation.split()

    if calc_sep[0] == 'exit':
        exit_prog()

    if calc_sep[1] == '+':
        result = add(calc_sep[0], calc_sep[2])

    elif calc_sep[1] == '-':
        result = subtract(calc_sep[0], calc_sep[2])

    elif calc_sep[1] == '*':
        result = multiply(calc_sep[0], calc_sep[2])

    elif calc_sep[1] == '/':
        result = divide(calc_sep[0], calc_sep[2])


    print("Result = ", result)
