## Python 快速生成列表

快速生成列表格式:

> xxx = [表达式 循环语句 条件]

可以在循环语句中加入嵌套 for 循环:

```python
# Example
xxx_1 = [1, 2, 3, 4, 5, 6]
xxx_2 = [2, 3, 5, 7, 9, 0]

new_list = [i for i in xxx_1 for j in xxx_2 if i == j]
print(new_list)
================== OUTPUT ==================
[2, 3, 5]
```

