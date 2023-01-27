class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say(self,something):
        return '{} 说 {}'.format(self.name,something)

    def eat(self,food):
        return '{} 吃 {}'.format(self.name,food)

handsomeb = Person("小帅b",18)
print (handsomeb.name)
print (handsomeb.age)
print (handsomeb.say('哈哈哈哈'))

zhangsan = Person("张三",23)
print (zhangsan.name)
print (zhangsan.age)
