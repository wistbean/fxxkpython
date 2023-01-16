class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self,food):
        print (self.name,"正在吃{}".format(food))
    
class Yellowpeoplefather(Person):
    def play(self,game):
        print (self.name,"玩{}".format(game))

class Whitepeoplemother(Person):
    def say(self,language):
        print (self.name,"说{}".format(language))

class Son(Yellowpeoplefather,Whitepeoplemother):
    pass

handsomeb = Son("小帅b",18)

handsomeb.play("王者")
handsomeb.say("英文")
