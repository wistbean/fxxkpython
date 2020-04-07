## Python 字符串

在 Python 中， string 是一种类似于列表的 **不可变类型**，可以通过 index 来访问 string 里面的字符。

#### 表示方法

```python
# Single quote 'xxx'
'digmouse'

# Double quotes "xxx"
"digmouse"

# Triple quotes '''xxx'''
'''digmouse'''
```

#### 转义字符

1. 单引号：\\'
2. 双引号：\\"
3. newline：\\n
4. tab：\\t
5. 回车：\\r
6. 退格：\\b

如果不想转义则在字符串前加 r:

```python
str = r"Hello\nWorld!"
print(str)

====== OUTPUT ========
Hello\nWorld!
```

#### String 拼接

1. 使用 + 拼接 string:

```python
str = str_1 + str_2
```

2. 使用 += 拼接 string (性能更好):

```python
str_1 += str_2
```

3. 使用 * 快速生成 N 个相同 string:

```python
str = str_1 * N
```

#### String 格式化

1.  使用以下两种格式化方法并在字符串最后加上 % 与对应的值：
   - %s: 字符格式化
   - %d: 整型格式化

```python
print("Hello, My name is %s, I'm %d years olf." % ('digmouse', 19))
```

2. 使用 format 格式化方法并使用 {} / {index} / {name} 进行占位后加上对应的值：

```python
# Using {}
print("Hello, my name is {}, I'm {} years old.".format('digmouse', 19))

# Using {index}
print("Hello, my name is {0}, I'm {1} years old.".format('digmouse', 19))

# Using {name}
print("Hello, my name is {name}, I'm {age} years old.".format(name='digmouse', age=19))
```

#### String 方法

1. 使用 find 方法在 string 中查找 xxx，如果有则返回在字符串中的 index，如果没有则返回 -1:

```python
str.find("xxx")
```

2. 使用 replace 方法用 xxx_2 替换 xxx_1:

```python
str.replace("xxx_1", "xxx_2")
```

3. 使用 split 方法对字符串中的特定字符 'x' 两边进行分割:

```python
str.split('x')
```

4. 使用 strip 方法将空格和换行符清除掉:

```python
str.strip()
```

5. 使用 lower 方法将 string 中的字符转换为小写:

```python
str.lower()
```

6. 使用 upper 方法将 string 中的字符转换为大写:

```python
str.upper()
```

7. 判断 string 是否以 "xxx" 开头:

```python
str.startswith('xxx')
```

8. 判断 string 是否以 "xxx" 结尾:

```python
str.endswith('xxx')
```

