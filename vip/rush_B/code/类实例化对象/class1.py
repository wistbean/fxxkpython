class Person: #创建Person类  
    attr = "xxx" #创建类的共有变量

    def __init__(self,name,age): # 初始化
        self.name=name      #声明一个实例化的对象的值
        self.age=age
    def say(self,something): #创建say说方法 
        return '{0}说{1}'.format(self.name,something)
    def eat(self,food):   #创建food吃方法
        return'{0}吃{1}'.format(self.name,food)
rush_B=Person('rush_B',18)
print(rush_B.say('哈哈哈')) #调用say说方法
print(rush_B.eat('山珍海味'))#调用eat吃方法
