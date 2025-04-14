
def calculator(a, b, op):
    if (op == '+'):
        print(f'{a} {op} {b} = {a + b}')
    elif (op == '-'):
        print(f'{a} {op} {b} = {a - b}')
    elif (op == '*'):
        print(f'{a} {op} {b} = {a * b}')
    else:
        print(f'{a} {op} {b} = {a / b}')

calculator(1, 3, '+')