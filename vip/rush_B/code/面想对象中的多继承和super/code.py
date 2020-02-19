#创建Person类
class Person:
    def __init__(self,name,age):# 创建__init__方法 self 是实列本身 name age 是 属性
        #实列化对象并赋予值
        self.name = name
        self.age = age
    def eat(self,food): #创建吃的方法
        print(self.name,"正在吃{}".format(food))

class subclass(Person):#subclass子类继承Person父类
    def __init__(self,name,age,weight):#初始化 
        #super调用父类__init__初始化name，age
        #super().__init__(name,age)
        #也是可以使用super父类名称来调用 注意调用方法的属性要一致
        Person.__init__(self,name,age)
        self.weight=weight 

    def print_some(self): #创建print_some方法 
        print(self.name,"今年{}岁，体重{}斤".format(self.age,self.weight))

rush_B = subclass("rush_B",20,180)
rush_B.print_some()
