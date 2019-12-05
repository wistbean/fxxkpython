## Python lambda()

lambda() 是一个 **匿名函数**，也就意味着 lambda() 不需要定义函数名称，其用于定义只会调用一次的函数

```python
# 定义 N 个参数后执行 statement
lambda argument_1, argument_2, argument_N: statement 

# 定义不限量个参数后执行 statement
lambda *argument: statement	
```

在 lambda() 函数后加括号向其传入参数:

```python
# 向 lambda 函数中传入实参 x 与 y
(lambda argument_1,argument_2: statement)(x,y)

(lambda *argument: statment)(x,y)
```

使用 map() 函数和 filter() 函数对 lambda() 函数进行高效使用：

1. map() 函数可以传入两个参数，第一个参数为将传入的函数，第二个参数为调取参数的序列。在 map() 函数中，序列中的每个值都会被取出来执行执行传入的函数:

```python
# Example
my_list = [1, 2, 3, 4, 5]

print(list(map(lambda x: x + 5, my_list)))

================ OUTPUT ====================
[6, 7, 8, 9, 10]
```

2. filter() 函数可以传入两个参数，第一个参数为将传入的函数**（通常为判断函数）**，第二个参数为调取参数的序列。在 map() 函数中，序列中的每个值都会被取出来执行执行传入的函数:

```python
# Example
my_list = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x % 2 == 0, my_list)))

================ OUTPUT ====================
[2, 4]
```

