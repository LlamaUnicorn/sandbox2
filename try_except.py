def boilerplate():
    try:
        # Block of code that might raise an exception
        num = int(input("Enter a number: "))
        result = 10 / num

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")

    except ValueError:
        print("Error: Please enter a valid integer")

    else:
        print("Result:", result)

    finally:
        print("This will always be executed")


def my_func():
    try:
        user_input = int(input('Enter a digit: '))
        result = 10 / user_input
        return print('Result: ', result)
    except Exception as e:
        print(f'Error: {e}')


my_func()
