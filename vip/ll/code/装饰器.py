def func_1(func):
    def func_s():
        print("func")
        func()
    return func_s
@func_1
def func_2():
    print("func_2")
func_2()