def my_func():
    age=12 #局部变量
    def my_inner_func():
        nonlocal age #调用被嵌入的局部变量
        age +=1
        print(age)
    my_inner_func()

my_func()
