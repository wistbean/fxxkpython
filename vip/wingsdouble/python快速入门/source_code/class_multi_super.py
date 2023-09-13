class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name,' 正在吃{}'.format(food))

class YellowPeopleFather(Person):
    def eat(self,food):
        print("黄种人的eat方法")

class WhitePeopleMother(Person):
    def eat(self,food):
        print("白种人的eat方法")

class Son(YellowPeopleFather, WhitePeopleMother):
    def eat(self, food):
        super(WhitePeopleMother,self).eat(food)

he = Son('hey', 90)

he.eat("水果沙拉")
print(Son.__mro__)
