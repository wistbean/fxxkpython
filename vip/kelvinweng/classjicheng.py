class Person:
    attr = "666"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self,food):
        return print (self.name,"正在吃{}".format(food))

    def play(self,game):
        return print (self.name,"正在玩{}".format(game))

class Yellowpeople(Person):
    def __init__(self,name,age,weight):
        super().__init__(name,age)
        self.weight = weight

    def sing(self,song):
        print (self.name,"正在唱{}".format(song))

    def eat(self,food):
        print (self.name,"正在狼吞虎咽的吃{}".format(food))

    def print(self):
        print (self.name,'今年{}岁,体重{}斤'.format(self.age,self.weight))

class Whitpeople(Person):
    pass

class Son(Yellowpeople,Whitepeople):
    pass

kelvin = Yellowpeople("kelvin",23,78)
kelvin.sing("浮夸")
kelvin.eat('蛋糕')
kelvin.play('war game')
kelvin.print()


