import os 
while  True:
    print('Select a number')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Divide ')
    print('5. Exits')
    ch = input('Enter your choice: ')
    if ch == '1':
        a =int(input('Enter the first number: '))
        b =int(input('Enter the Second number: '))
        print(f'{a} + {b} is {a+b}')
    elif ch == '2':
        a =int(input('Enter the first number: '))
        b =int(input('Enter the Second number: '))
        print(f'{a} - {b} is {a-b}')
    elif ch == '3':
        a =int(input('Enter the first number: '))
        b =int(input('Enter the Second number: '))
        print(f'{a} * {b} is {a*b}')
    elif ch == '4':
        a =int(input('Enter the first number: '))
        b =int(input('Enter the Second number: '))
        print(f'{a} / {b} is {a/b}')
    elif ch == '5':
        print('exiting..')
        break
    else:
        print('Invalid choice')
    input('print enter to continue ...')
    os.system('cls')