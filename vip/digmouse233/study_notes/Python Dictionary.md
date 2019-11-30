## Python Dictionary

Initialize a dictionary:

```python
xxx = {'key_1': 'value_1', 'key_2': 'value_2'}
```

key 只能用 **不可变** 类型且在字典中 **不可以** 重复。

#### Find

Find the value corresponding to key:

```python
>>> xxx['key_1']
'value_1'
>>> xxx['key_2']
'value_2'
```

#### Modify

The way to modify dictionary is similar to list:

```python
>>> xxx['key_1'] = 'value_3'
>>> xxx['key_1']
'value_3'
```

#### Delete

1. Delete a pair of element in the dictionary:

```python
del xxx['key_1']
```

2. Clear the whole dictionary:

```python
xxx.clear()
```

3. Destory the dictionary:

```python
del xxx
```

#### Add

Add a pair of element directly by define it:

```python
xxx['key_3'] = 'value_3'
```

#### Conversion

1. Converse dictionary **values** to list:

```python
xxx.values()
```

2. Converse dictionary **keys** to list:

```python
xxx.keys()
```

3. Converse dictionary **pairs** to tumple, and then compose a list:

```python
xxx.items()
```

