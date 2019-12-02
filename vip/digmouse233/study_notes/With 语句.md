## With 语句

Python 读取文件:

```python
with open(path) as file:		# 变量 file 得到 __enter__(self) 方法的返回值
  data = file.read()
```

用 with 调用的对象中需要用到以下两个方法:

```python
def __enter__(self):		 # 首先调用，负责初始化
# statement

def __exit__(self, type, value, trace):		# 最后调用，负责擦屁股
# statement
```

