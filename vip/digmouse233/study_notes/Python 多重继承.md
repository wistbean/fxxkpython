## Python 多重继承

多继承是指一个子类拥有且同时继承多个父类，其将**同时拥有所有父类的属性与方法:**

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 单继承 Person
class YellowPeopleFather(Person):
  pass

# 单继承 Person
class WhitePeopleMother(Person):
  pass

# 多继承 YellowPeopleFather 与 WhitePeopleMother
class Son(YellowPeopleFather, WhitePeopleMother):
  pass
```

若多个父类拥有同一个方法，则子类在使用 super() 方法调用时遵循 MRO 顺序。

**使用 super(class_N, self) 方法时，总是调用 Class_N 类 MRO 顺序的的下一个类。**

> 可以通过调用子类 xxx 的 MRO 方法查看 MRO 顺序:
>
> ```python
> print(xxx.__mro__)
> ```
>
> 

可以通过向 super(class_N, self) 方法传入参数的方式指定调用对象，

若 MRO 的顺序为：Son ----> Mother ----> Father ----> Person ----> Object，

1. 子类 Son 调用父类 Mother 方法 xxx：

```python
class Son(Mother, Father):
  def xxx(self, something):
    # 此时 class_N 为 Son 类，其 MRO 顺序的下一个为 Mother 类
    super(Son, self).xxx(something)	
```

2. 子类 Son 调用父类 Person 方法 xxx：

```python
class Son(Mother, Father):
  def xxx(self, something):
    # 此时 class_N 为 Father 类，其 MRO 顺序的下一个为 Person 类
    super(Father, self).xxx(something)	
```

