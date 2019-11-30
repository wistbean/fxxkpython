## Python List

Initialize a list:

```python
xxx = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
```

#### Find

1. Find what is the first element in the list:

```python
xxx[0]		# number begin from 0 in python
```

2. Find what is the Nth element in the list:

```python
xxx[N-1]
```

3. Find what are the elements between A and B in the list:

```python
xxx[A, B+1]
```

4. Find what is the last element in the list:

```python
xxx[-1]
```

5. Find what are the elements form the second element to the last one:

```python
xxx[2:]
```

#### Modify

Change the Nth element in the list to "a":

```python
xxx[N-1] = 'a'
```

#### Delete

1. delete the Nth element in the list:

```python
del xxx[N-1]
```

2. delete one specific element (e.g.: 'first') in the list:

```python
xxx.remove('first')
```

#### Add

1. Add an element 'ADD' with index N:

```python
xxx.insert(N, 'ADD')
```

2. Add an element 'ADD' to the last:

```python
xxx.append('ADD')
```

#### Extra

1. Find the length of the list:

```python
len(xxx)
```

2. Find the index of a specific element 'A':

```python
xxx.index('A')
```

3. Reverse the whole list:

```python
xxx.reverse()
```

4. Remove and **return** the last element in the list:

```python
xxx.pop()
```

5. Clear the whole list:

```python
xxx.clear()
```

