## Python 类，实例化与对象

**类：**类是一个结构，**不会**给你提供具体的数据，但是它会提供给你**必要的框架信息**，这些信息是这个结构所必须的。

**实例化：**向类构建的结构加入具体数据的过程

**对象：**通过类的结构可以实例化出对象

![img](https://vip.fxxkpython.com/wp-content/uploads/2019/09/Untitled-Diagram7.png)

### 类

```python
class Person:
  
  attr = 'pp'											# 类共有的变量 attr
  
  def __init__(self, name, age):		
    self.name = name							# self 代表实例本身
    self.age = age
  
  # 定义类的方法
  def say(self, something):
    return '{} says {}'.format(self.name, something)
  
  def eat(self, food):
    return '{} eats {}'.format(self.name, food)
    
# 实例化对象 'digmouse'
digmouse = Person('digmouse', 18)
little_chicken = Person('little chicken', 19)

print(digmoue.name)
print(little_chicken.age)
print(digmouse.attr)
print(little_chicken.attr)
print(digmouse.say("Hello!"))
print(little_chicken.eat("watermelon"))
=========================== OUTPUT ===========================
digmouse
19
pp
pp
digmouse says Hello!
little chicken eats watermelon
```





