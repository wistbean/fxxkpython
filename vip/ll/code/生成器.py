import time
def main_func(func):
    start_time=time.perf_counter()
    my_func=func()
    end_time=time.perf_counter()
    print('{}方法消耗了{}ms'.format(func.__name__,(end_time-start_time)*1000))
    return my_func
@main_func
def func_1():
    ll=[i for i in range(9999999)]

@main_func
def func_2():
    ll=(i for i in range(9999999))

def foo():
    yield 1
    yield "2"
    yield 3
for i in foo():
    print(i)