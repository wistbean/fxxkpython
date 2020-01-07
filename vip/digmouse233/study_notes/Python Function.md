## Python Function

Python 已经提供给我们能供直接使用的函数叫做 **内置函数。**

创建自定义函数的好处是可以让代码简洁和模块化，可供重复使用，大大提高使用效率。

定义自定义函数的方法如下：

> def function_name (parameter_name):
>
> ​           return XXX

一般来说，定义在函数里面的变量被称为 **局部变量**，而定义在函数之外的变量被称为 **全局变量。**

**函数里不可以直接使用函数外的全局变量！**

1. 函数内部调用最外层的全局变量 var，需要声明 **global** var
2. 函数内部调用上层的局部变量 var，需要声明 **nonlocal** var

```python
var = 1

def my_func():
  var = 2
  def my_inner_func():
    global var		# var = 1
    nonlocal var  # var = 2
    var + 1
  my_inner_func()
  
my_func()
```

#### Parameter

1. 定义的函数的参数个数应与实际传入的参数个数相等
2. 可以直接指定参数值，而后直接调用:

```python
def print_some(length, age):
  print('Age: ', age)
  print('Length: ', length)
  
print_some(age = 28, length = 18)			# 直接传入参数
```

3. 定义函数的参数事设定默认值:

```python
def print_some(length, age = 66):		# 设置参数 age 的默认值为 66
  print('Age: ', age)
  print('Length: ', length)
  
print_some(length = 18)			# 若不传入参数 age 的值，则使用默认值
```

4. 使用 * 定义函数的可变参数（可以接受多个参数，最后都转化为 **tumple**）:

```python
def print_some(length, *age):		# 设置 age 为可变参数
  print('Age: ', age)
  print('Length: ', length)
  
print_some(18, 1, 2, 3, 4, 5)		# 传入 5 个 age 值

================== OUTPUT =======================
('Age: ', (1, 2, 3, 4, 5))
('Length: ', 18)
```

5. 使用 ** 定义函数的可变参数（可以接受多个参数，最后都转化为 **dictionary**）:

```python
def print_some(length, **age):		# 设置 age 为可变参数
  print('Age: ', age)
  print('Length: ', length)

# 传入 dictionary 需使用 key-value 形式 
print_some(length = 18, age_1 = 1, age_2 = 2, age_3 = 3, age_4 = 4, age_5 = 5)		

================== OUTPUT =======================
('Age: ', {'age_1': 1, 'age_3': 3, 'age_2': 2, 'age_5': 5, 'age_4': 4})
('Length: ', 18)
```

