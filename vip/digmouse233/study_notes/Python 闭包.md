## Python 闭包

闭包可以让使用者访问到函数内部的数据，也就是可以拿到在闭包内所提供的隐藏数据。如果某个功能只需要一个函数，可以使用闭包而不需另创建一个类。

```python
# Example
def outer_func(x):
  def inner_func(y):
    return x + y
  return inner_func

adder5 = outer_func(5)	# x = 5 in outer_func
adder5(10)	# y = 10 in inner_func
================== OUTPUT =====================
15
```

第一次将参数传入并 **保留** 在外函数，第二次将参数传入内函数。

```python
# 在闭包内隐藏数据
def outer_func():
  x = 5		# 隐藏数据 5
  def inner_func(y):
    return x + y
  return inner_func

outer = outer_func()
outer(1)
========== OUTPUT ==============
6
```



