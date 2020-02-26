#创建Person类
class Person:
    def __init__(self,name,age):# 创建__init__方法 self 是实列本身 name age 是 属性
        #实列化对象并赋予值
        self.name = name
        self.age = age
    def eat(self,food): #创建吃的方法
        print(self.name,"调用Person方法.正在吃{}".format(food))



#如果son 的父类都有相同的方法 我们可以跟据__mro__顺序，使用super()调用你想使用的方法。


class Yellow(Person):#Yellow子类继承Person父类
    def eat(self,food):
        print("调用Yellow方法.正在吃{}".format(food))

class White(Person):
    def eat(self,food):
        print("调用White方法.正在吃{}".format(food))

class son(Yellow,White):
    def eat(self,food):
        super(White,self).eat(food)
        #super().eat(food)
        #print("调用son方法.正在吃{}".format(food))


rush_B = son("rush_B",20)
rush_B.eat("麻辣烫")
print(son.__mro__)#调用mro方法并打印出来 
