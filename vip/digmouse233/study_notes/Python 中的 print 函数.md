## Python 中的 print 函数

1. print 函数会在结尾默认加入转义字符：'\n'，若要修改 print 函数打印的最后一位需传入 end 参数

```python
>>> print("xxx", end="@", flush=True) # flush 决定每次打印是否刷新
xxx@
xxx@
xxx@
xxx@
```

2. 使用 print 函数打印多个字符串时传入 sep 参数修改连接符

```python
>>> print("xxx_1", "xxx_2", sep="@")
xxx_1@xxx_2
```

3. 使用 format 和 f-string 在 string 中加入其它类型变量

```python
age = 19

# 使用 format 加入其它类型变量
print("digmouse is {} years old".format(age))

# 使用 f-string 加入其它类型变量
print(f"digmosue is {age} years old")
```

4. 使用占位符 %s 和 %d 在 string 中加入变量

```python
print("%s is %d years old" % ("digmouse", 19))	# 使用 tumple 将被调用的数据包裹起来
```

5. print 函数可以打印各种类型信息
6. 输出仅数字变化的百分数：
   - 字符串输出前加入转义字符 '\r' 可以使 flush 从最前端重新刷新
   - 使用 tqdm 或 progressbar 库

