## With 语句

Python 读取文件

```python
with open(path) as file:		# 变量 file 得到 __enter__(self) 方法的返回值
  data = file.read()
```

在 with 调用后得到的对象里需要用到

```python
__enter__(self)		 # 首先调用，负责初始化
```

和

```python
___exit__(self, type, value, trace)		# 最后调用，负责擦屁股
```

两个方法