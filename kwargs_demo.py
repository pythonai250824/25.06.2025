from abc import ABC, abstractmethod
from typing import override


def foo(x, y , *args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    if 'name' in kwargs.keys():
        print('your name is', kwargs['name'])

foo(1, 2, name='danny', age=30)

def haham(x, y, *args, dict1 = {}):
    pass

haham(1, 2, {'name':'danny', 'age':30})

dict1 = {'name': 'danny', 'x': 1}
key1, key2 = dict1
print(key1, key2)

(key1, value1), (key2, value2) = dict1.items()
print(key1, value1, key2, value2)

def greet(name, age):
    print(f'hello {name}, you are {age} years old.')


greet('danny', 30)
greet(name='danny', age=30)
data = {'name': 'danny', 'age': 30}
greet(**data)


class EventPrinter(ABC):
    @abstractmethod
    def print_event(self, message, *args, **kwargs):
        pass

class ConsoleEventPrinter(EventPrinter):
    @override
    def print_event(self, message, *args, **kwargs):
        print(message)

class FileEventPrinter(EventPrinter):
    @override
    def print_event(self, message, *args, **kwargs):
        # * [1,2,3] =>  1, 2 , 3
        # * 1, 2, 3 => [1, 2 ,3]
        # *args

        # ** {'name': 'danny', 'age': 30} => name='danny', age=30
        # ** name='danny', age=30         => {'name': 'danny', 'age': 30}
        # **kwargs
        '''

        :param message:
        :param args: args[0] == file_name
        :return:
        '''
        print(message, kwargs['file_name'])

c = ConsoleEventPrinter()
c.print_event('program started')
f = FileEventPrinter()
f.print_event('program started', file_name='log.txt')
f.print_event('program started', 2, file_name='log.txt')

dict1 = {'a': 10, 'b': 20}
# dict2 = {dict1, 'c': 4, 'd': 5}  # [ [1, 2, 3], 4, 5]
dict2 = {**dict1, 'c': 4, 'd': 5}  # {'a': 10, 'b': 20, 'c': 4, 'd': 5}
print(dict2)

def print_info(fname, lname, address, *args, **kwargs):
    # if inside kwargs key 'hide': True ==> print only first name, otherwise print all fields in one line
    # if inside kwargs key 'upper': True ==> print everything in upper case
    hide = kwargs.get('hide', False)
    upper = kwargs.get('upper', False)

    output = f"{fname}"
    if not hide:
        output += f" {lname} {address}"
    if upper:
        output = output.upper()

    print(output)

print_info('danny', 'shovevani', 'narniya 12')
print_info('danny', 'shovevani', 'narniya 12', hide=True)
print_info('danny', 'shovevani', 'narniya 12', hide=True, upper=True)
print_info('danny', 'shovevani', 'narniya 12', upper=True)

def a1():
    a2()

# a1()  # Error

def a2():
    pass

a1()

print('==================')
def run_fun(func_name, *args, **kwargs):
    func_name(*args, **kwargs)

def func1(x):
    print(x)

def func2(x, y):
    print(x + y)

def func3(x, y, z):
    print(x + y + z)

def func4(dic1):
    print(dic1['name'])

def func5(x, y, *args, **kwargs):
    print(x + y)
    print(args)
    print(kwargs)


run_fun(func1, 10)
run_fun(func2, 2, 5)
run_fun(func3, 2, 5, 7)
run_fun(func4, {'name': 'danny'})
run_fun(func5, 2, 5, 4, 4, 4, upper=True)



