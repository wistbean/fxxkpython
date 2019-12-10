class Person():
    father_variable=99
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    def eat(self,something):
        return ("调用的是Person {}吃：{} ".format(self.name,something))
class Yellow_people_father(Person):
    def eat(self, something):
       return ("调用的是Yellow_people_father {}吃：{} ".format(self.name, something))
class Yellow_people_mother(Person):
    def eat(self, something):
        return  ("调用的是Yellow_people_mother {}吃：{} ".format(self.name, something))
class son(Yellow_people_father,Yellow_people_mother):
    def eat(self, something):
        return  super(Yellow_people_father,self).eat(something)
        # return ("调用的是son {}吃：{} ".format(self.name, something))
boy=son("jack",18)


print(boy.eat("milk"))
print(son.__mro__)