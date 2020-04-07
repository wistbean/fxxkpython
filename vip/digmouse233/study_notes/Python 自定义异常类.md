## Python 自定义异常类

如果不想处理异常，则在自定义异常类中继承父类的 raise 方法进行输出:

```python
class MyException(Exception):
  pass

raise MyException('xxx')	# output 'xxx'
```

可以在自定义异常类中自定义方法：

```python
# 例子：定义返回错误信息的方法
class MyException(Exception):
  def __init__(self, value):
    super().__init__(self)
    self.value = value
  
  def __str__(self):
    return self.value
```

