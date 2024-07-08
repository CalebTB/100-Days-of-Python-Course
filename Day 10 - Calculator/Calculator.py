def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/':
        return num1 / num2


def main():
    end = False

    while not end:

        # Factory Resets for Variables
        total = 0
        continue_calculating = ""
        start_new_calc = False
        # -----------------------------

        num1 = float(input("Enter first number: "))
        operations_list = ["+", "-", "*", "/"]
        for operation_var in operations_list:
            print(operation_var)
        while not start_new_calc:

            operation = input("Enter operation: ")
            num2 = float(input("Enter second number: "))

            total = calculator(num1, num2, operation)
            print(f"{num1} {operation} {num2} = {total:.2f}")

            while continue_calculating not in ['y', 'n']:
                continue_calculating = input("Would you like to continue [y] "
                                             "or start a new calculation [n]? ").lower()

            if continue_calculating == 'y':
                num1 = total
                pass
            if continue_calculating == 'n':
                start_new_calc = True


if __name__ == '__main__':
    main()
