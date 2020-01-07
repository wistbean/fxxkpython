## Python Tumple

Initialize a tumple:

```python
xxx = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth')
```

#### Find

1. Find what is the first element in the tumple:

```python
xxx[0]		# number begin from 0 in python
```

2. Find what is the Nth element in the tumple:

```python
xxx[N-1]
```

3. Find what are the elements between Ath and Bth in the tumple:

```python
xxx[A, B+1]
```

4. Find what is the last element in the tumple:

```python
xxx[-1]
```

5. Find what are the elements form the second element to the last one in the tumple:

```python
xxx[2:]
```

#### Modify (forbidden)

tumple 类型是 **不可变** 类型，一旦定义其中元素则不可修改。

#### Delete (forbidden)

tumple 类型是 **不可变** 类型，一旦定义其中元素则不可删除。

但是可以删除整个 tumple：

```python
del xxx			# delete the whole tumple
```

#### Add

tumple 类型是 **不可变** 类型，一旦定义其中元素则不可增加。

但是可以新创建 tumple 并合并进原 tumple：

```python
('new_element_1', 'new_element_2') + xxx
```

