import sys


def get_int():
    while True:
        try:
            number = int(input('Enter a number: '))
            return number
        except ValueError:
            print('Not a number')
        except EOFError:
            sys.exit(0)
        finally:
            print("finally close always execute....")


try:
    first = get_int()
    second = get_int()
    print('Number after div: {}'.format(first / second))
except ZeroDivisionError:
    print('Div by zero')
else:
    print('Div performed successfully...')

