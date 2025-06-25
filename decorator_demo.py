from abc import abstractmethod


# @override
# @abstractmethod
# @property


def get_func():
    return print

f = get_func()
# f = print
f('hi')

def before_after(func_name):
    def wrapper():
        print('Before')
        func_name()
        print('After')
    return wrapper

@before_after
def say_hello():
    print('hello there ...')

say_hello()


def safe_run(func_name):
    def wrapper(*args):
        try:
            return func_name(*args)
        except Exception as e:
            print(e)
    return wrapper

@safe_run
def do_div(a, b):
    return a / b

result = do_div(3, 1)
if result:
    print('result=', result)

result = do_div(3, 0)
if result:  # if result != None:
    print('result=', result)



###################################################

# @repeat(3) -- next lesson

import time

def time_measure(func):
    def wrapper(*args, **kwargs):
        # 1 start timer
        start = time.time()
        # 2 run funciton
        result = func(*args, **kwargs)
        # 3 calc time
        duration = time.time() - start
        # 4 print time
        print(f'the function {func} took {duration:.2f} seconds')

        return result
    return wrapper

@time_measure
def time1(message):
    time.sleep(2)  # simulate long operation
    print(message)

@time_measure
def time2(message):
    time.sleep(1.5)  # simulate long operation
    print(message)

time1('hello')
time2('hello')
