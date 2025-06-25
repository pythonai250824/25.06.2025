from abc import ABC, abstractmethod
from typing import override


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

def sum_args(x, y, *args):
    result = x + y
    for i in args:
        result += i
    return result

print()
print(sum_args(1, 2))
print(sum_args(1, 2, 5, 6, 8, 9, 2 , 2))

# unpack
l1 = [(1, 2), (3, 4)]
for x, y in l1:
    print (x, y)

def get_numebrs(x, y, z):
    print(x, y, z)

nums = [1, 2, 3]
get_numebrs(*nums)
x, y, z = nums
print(x, y, z)

print('==================')
def run_fun(func_name, *args):
    func_name(*args)

def func1(x):
    print(x)

def func2(x, y):
    print(x + y)

def func3(x, y, z):
    print(x + y + z)

def func4(dic1):
    print(dic1['name'])

run_fun(func1, 10)
run_fun(func2, 2, 5)
run_fun(func3, 2, 5, 7)
run_fun(func4, {'name': 'danny'})

class EventPrinter(ABC):
    @abstractmethod
    def print_event(self, message, *args):
        pass

class ConsoleEventPrinter(EventPrinter):
    @override
    def print_event(self, message, *args):
        print(message)

class FileEventPrinter(EventPrinter):
    @override
    def print_event(self, message, *file_name):
        '''

        :param message:
        :param args: args[0] == file_name
        :return:
        '''
        print(message, file_name[0])

c = ConsoleEventPrinter()
c.print_event('program started')
f = FileEventPrinter()
f.print_event('program started', 'log.txt')

num1 = [1,2,3]
num2 = [num1, 4, 5]  # [ [1, 2, 3], 4, 5]
num3 = [*num1, 4, 5] # [ 1, 2, 3, 4, 5]
print(num3)



