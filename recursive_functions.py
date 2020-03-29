# Factorial using a while loop

def get_factorial(num):
    if num < 0:
        return "Can't find factorial of a number"
    if num == 0 or num == 1:
        return 1
    factorial = 1
    while num > 0:
        print(num, 'x', factorial, '=', num * factorial)
        factorial *= num
        num -= 1

def get_factorial(num):
    if num < 0:
        return "Can't find factorial of a number"
    elif num == 0 or num == 1:
        return 1
    else:
        return num*get_factorial(num-1)

# Factorial using a auxiliary function

def get_factorial(num):
    print_loading = False
    if num > 100:
        print_loading = True
    return get_factorial_aux(num, print_loading)

def get_factorial_aux(num, print_loading):
    if print_loading:
        print('loading...')
    if num < 0:
        return "Can't find factorial of a number"
    elif num == 0 or num == 1:
        return 1
    else:
        return num*get_factorial_aux(num-1, print_loading)
