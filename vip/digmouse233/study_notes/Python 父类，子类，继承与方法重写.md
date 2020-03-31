## 父类，子类，继承与方法重写

父类可以衍生出子类，同时父类拥有的属性和方法（功能），子类们也会继承下来。

**父类衍生子类，子类继承父类。**

> ![img](https://vip.fxxkpython.com/wp-content/uploads/2019/09/Untitled-Diagram8.png)
>
> 人类作为父类衍生出“黄种人”、“黑种人”、“白种人”、“棕种人”四种子类。而人类所拥有的属性和方法（功能），继承的子类们也会相应的拥有，不需要额外的操作。

#### 如何继承

定义一个父类:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def eat(self, food):
    print("{} eats {}".format(self.name, food))
  
  def play(self, game):
    print("{} plays {}".format(self.name, game))
```

**在子类的 () 中写上父类名称，则子类继承父类:**

```python
class Yellow_people(Person):
  pass
```

可以为创建出来的子类定义特有的方法和属性:

```python
class Yello_people(Person):
  # 子类不需要 __init__() 函数，其属性默认继承父类（也可重写）
  def sing(self, song):
    print("{} sings {}".format(self.name, song))
```

**OOP 中最大的父类是 object，也就是说 Person 类继承了 object 类。**Python 默认继承最大的父类，所以我们不需要写:

```python
class Person(object)
```

#### 如何重写方法

适用于父类子类定义同一个方法但想要的效果不同:

```python
# 父类
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
   
  def eat(self, food):
    print("{} eats {}".format(self.name, food))
    
# 子类
class Yellow_people(Person):
  # 子类默认继承父类 __init__() 方法所以不需要重写 
  def eat(self, food):
    print("{} eats {} quickly".format(self.name, food))
```

当 **单继承** 子类定义类与父类相同的属性或方法时，使用父类名称或 super() 调用父类属性或方法

```python
# 父类
class Person:
  attr = '666'		# 父类中定义的属性
  
# 子类  
class Yellow_prople(Person):
  attr = '999'
  def print_sone(self):
    print("子类变量：", attr)
    # 子类使用父类名称调用父类属性
    print("子类调用了父类的变量: ", Person.attr)		
    print("子类调用了父类的变量:", super().attr)
======================= OUTPUT ============================
子类变量：999
子类调用了父类的变量: 666
子类调用了父类的变量: 666
```

