## Python List / Tumple

list 与 tumple 内均可存放不同数据类型的元素：

```python
my_list = ['1', 'a', '1.0']
my_tumple = ('1', 'a', '1.0')
```

tumple 一旦定义所占用内存不再改变，list 占用内存随着其中元素的增多而增大。

**list 用来存储比较“灵活”的元素，tumple 用来存储比较“死”的元素。**

list 与 tumple 相互转换时仅需将原变量放入新类型函数中即可:

```python
my_tumple = tumple(my_list)		# converse list to tumple
my_list = list(my_tuple)			# converse tumple to list
```

