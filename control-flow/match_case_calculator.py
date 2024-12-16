num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

operand = input('Choose the operation (+, -, *, /): ')

match operand:
    case '+':
        result = num1 + num2
        print(f'The result is {result}')
    case '-':
        result = num1 - num2
        print(f'The result is {result}')
    case '*':
        result = num1 * num2
        print(f'The result is {result}')
    case '/':
        if num2 == '0':
            print('Cannot divide by zero.')
        else:
            result = num1 / num2
            print(f'The result is {result}')
