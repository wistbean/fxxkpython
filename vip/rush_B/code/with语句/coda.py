#读取文件
#path='路径'
#with open(path) as file:
#   data = file.read()

#创建的对象能被 with 使用，那么你这个对象必须要有 __enter__ () 和 __exit__() 这两个方法

class rush_B: #创建rush_B对象
    def __enter__(self):
        print('进入 enter 方法')
        return 'rush_B'
       #rerurn self

    def __exit__(self,type,value,trace):
        print('进去 exit 方法')

def get_rush_B(): #创建get_rush_B方法
    return rush_B() #返回 rush_B

with get_rush_B() as A: #使用wiht调用 as后面变量是enter返回的值  也可以是对象
    print('get...:',A)

#with 异常处理没有看懂 后面补回来

        
