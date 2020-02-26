class Person: #创建Person类

    attr="xxxxx"
    def __init__(self,name,age): #__inti__初始化 self是实列本身 name，age 是属性
        #实例化变量赋予值
        self.name=name
        self.age=age   

    def eat(self,food):#创建吃方法
        print(self.name,"正在吃{}".format(food))

    def play(self,game):
        print(self.name,"正在玩{}".format(game))

class subclass(Person): #子类subclass继承Person父类
    #也是创建自己独有的方法和属性
    def sing(self,song):
        print(self.name,"正在唱{}".format(song))
     #也可以重写方法
    def play(self,game):
        print(self.name,"正在疯狂的玩{}".format(game))
    
     #super()可以得到父类变量直接引用
    def print_some(self):
        print("子集使用父类的变量:",super().attr)





rush_B=Person("rush_B",18)
rush_B.play("地平线4")
rush_A=subclass("rush_A",18)
rush_A.play("地平线4")
rush_A.sing("生日快乐")
rush_A.play("英雄联盟")
rush_A.print_some()
