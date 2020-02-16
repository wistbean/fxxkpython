class Person: #创建Person类
    attr ="xxx"#共有变量
    def __init__(self,name,age): #定义__init__函数a方法用来初始化 self表示实例化本身
        self.name = name #声明每个实例化对象的属性值
        self.age = age #和上面同一个意思
handsomeb =Person("handsomeb",18)
print(handsomeb.name)
print(handsomeb.age)
rush_B =Person("rush_B",20)#通过Person("rush_B",20)实例化一个对象
print(rush_B.name)
print(rush_B.age)
print(rush_B.attr)
print(handsomeb.attr)

