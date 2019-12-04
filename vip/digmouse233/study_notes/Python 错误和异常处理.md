## Python 错误和异常处理

**错误：**在编译过程中由控制台提示

**异常：**正常编译，在执行过程中出现问题

应当事先用 try ... except ... else ... finally 方法对可能会遇到的异常进行处理，确保程序能正常运行下去。

```python
# 若知异常类型 error_1, error_2, error_3
try:
  # statement
expect (error_1, error_2, error_3, ...) as err:		# error_N 均为 Python 的内置异常类型
  # statement
else:						# 没有发现异常，执行 else
  # statement
finally:				# 不论如何均会执行
  # statement
  
# 若不知异常类型
try:
  # statement
expect Expection as err:		# 也可以直接使用 expect:
  # statement
finally:
  # statement
  
========================== Example ==========================
try:
  with open('digmouse.txt') as file:
    file.read()
except:
  print('File is not exist.')
else:
  print('Already found the file')
finally:
  print('Done!')	# 不论如何均会执行
```

