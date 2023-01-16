class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person 的信息是 name:{self.name},age:{self.age}"


print (Person("handsomeb",18))
    
