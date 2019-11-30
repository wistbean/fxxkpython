## Python 基础语句

#### if 语句

1. **if:** 如果满足什么条件就执行
2. **elif:** 否则如果满足什么条件就执行
3. **else:** 以上条件均不满足则执行

```python
number = int(input("Enter a number: "))

if number < 18:
  print("Too small")
elif number == 18:
  print("Not bad")
else:
  print("Great")
```

#### pass 语句

满足某些条件但并未想好执行什么指令时使用（跳过）

```python
number = int(input("Enter a number: "))

if number < 18:
  print("Too small")
elif number == 18:
  print("Not bad")
else:
  pass
```

#### while 语句

只要满足特定条件就重复执行命令

```python
number = int(input("Enter a number: "))

while (number < 19):
  print("Too small, but grow quickly")
  number += 1
  
print("It's OK.")
```

#### for 语句

对于一些序列中的元素进行循环操作

```python
length = [12, 14, 16, 18, 20]		
for i in length:		
  if i < 18:
    print("Too small: ", i)
  else:
    print("Not bad: ", i)
```

#### break 语句

终止循环

```python
length = [12. 14. 16. 18. 20]
for i in length:
  if i > 16:
    print("It's OK: ", i)
    break
  else:
    print("Too small, ", i)
```

#### continue 语句

跳出 **本次** 循环

```python
length = [12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in length:
  if i % 2 == 0:
    print("Pass, the length is even!")
    continue
  print("The odd length: ", i)
```

