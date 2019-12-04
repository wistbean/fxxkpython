## Python Set

set 中的元素都是 **唯一的，无序的，不可重复的**，并且只能使用 **不可变** 类型。

Initialize directly:

```python
xxx = {1, 2, 0.3, 4, 'five'}
```

Initialize by type conversion:

```python
xxx = set((1, 2, 0.3, 4, 'five'))
```

为了确保唯一性，set 中的元素是不能重复的。在 set 中定义了重复的数据时，set 会 **去重** 将其视为一个数据。

#### Find

因为 set 是无序的，所以 **set 不支持索引操作！**

我们可以使用关键词 in 查询某个元素是否在 set 中:

```python
element in xxx		# return Ture / False
```

#### Add

1. 调用 set 的 add 方法向 set 集合中添加元素（只能作为一个元素）:

```python
xxx.add(new_element)			# only as one element
```

2. 调用 set 的 update 方法向 set 集合中添加元素（被拆分为多个元素）:

```python
xxx.update(new_elements)	  # seperate as many elements
```

#### Delete

1. 调用 set 的 remove 方法删除 set 集合中的特定元素:

```python
xxx.remove(element)
```

2. 调用 set 的 discard 方法删除 set 集合中的特定元素（如果不存在也不会报错）:

```python
xxx.discard(element)
```

3. 清空 set 集合:

```python
xxx.clear()
```

#### Extra

1. 得到两个集合的并集:

```python
set_1.union(set_2)
```

2. 得到两个集合的交集:

```python
set_1.intersection(set_2)
```

3. 判断 set_1 集合是否为 set_2 集合的子集:

```python
set_1.issubset(set_2)
```

4. 判断 set_1 集合是否为 set_2 集合的父集:

```python
set_1.issuperset(set_2)
```

