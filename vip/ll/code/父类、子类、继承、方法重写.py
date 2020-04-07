class Person():
    father_variable=99
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    def say(self,something):
        return ("{}说：{} ".format(self.name,something))
    def eat(self,somefood):
        return ("{}吃了{} ".format(self.name,somefood))
    def play(self,something):
        return ("{}正在玩：{} ".format(self.name,something))
class YellowPerson(Person):
    def sing(self,somemusic):
        return ("{}正在唱：{} ".format(self.name,somemusic))
    def eat(self,somefood):
        return ("{}正在狼吞虎咽的吃{}".format(self.name,somefood))
    def print_some(self):
        return super().father_variable
little_boy=YellowPerson("jack_MA",18)
print(little_boy.play("lol"),little_boy.sing("夜色"),little_boy.eat("鸡腿"),little_boy.print_some())