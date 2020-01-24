age=18
def my_func():
    name="小帅比"
    print(name)
    global  age
    print(age)
my_func()
def my_func_1():
    age=66
    def my_inner_func():
        nonlocal age
        print(age)
    my_inner_func()
my_func_1()
