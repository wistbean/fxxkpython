## for 循环语句 & else 语句

Python 中 for 循环语句可以同 else 语句一起使用，其作用是 **过滤**。

**如果 for 循环中有 else 语句，其会在 for 循环结束后运行**

**如果 for 循环中有 break 语句，for 循环会直接结束，不会执行 else 语句。**

下图在 2 - 9 的列表中寻找质数（除了被 1 和它本身整除之外，不能被其余数整除）

```python
for i in range(2, 10):			# initialize a list from 2 to 9
  for x in range(2, i):
    if i % x == 0:
      break
  else:
    print(i, " ")
```

