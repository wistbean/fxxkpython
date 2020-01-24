class Person():
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    def say(self,something):
        return ("{}说：{}".format(self.name,something))
    def eat(self,somefood):
        return ("{}吃了{}".format(self.name,somefood))
somebody=Person("jack",18)
print(somebody.age,somebody.name)
print(somebody.eat("面包"),somebody.say("i love you"))
