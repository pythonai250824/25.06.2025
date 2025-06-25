
def print_numbers(*args: int):
    print(type(args))
    for number in args:
        print(number)

print_numbers(1)
print_numbers(1, 2, 3)
print_numbers(1, 'hello', [1,2,3])
print_numbers()

def print_numbers2(a):
    pass

def print_numbers3(a, b):
    pass

def print_numbers4(arg_list: tuple[int] = tuple()):
    for number in arg_list:
        print(number)

print_numbers4()
print_numbers4((1, 2, 3))
print_numbers4(())

# illegal
#def foo(*args, x):
#    print(x)

def foo(x, *args):
    print(x)

foo(5, 1, 2, 3, 4)

# write func which gets x, y, and args and returns x + y + args...
# sum_args
# sum_args(1, 2) ==> 3
# sum_args(1, 2, 3) ==> 6
