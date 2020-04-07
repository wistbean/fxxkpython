age = 18 #全局变量

def my_func():
    name = 'rush_B' #局部变量
    print(name)

    global age #获取全局变量age
    age +=1 #age+1=age
    print(age)
my_func()
