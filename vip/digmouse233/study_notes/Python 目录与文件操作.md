## Python 目录与文件操作

使用 Python os 库来调用操作方法:

```python
import os
```

**目录操作：**

```python
# 创建一个新目录 xxx
os.mkdir('xxx')

# 重命名目录 xxx_1 为 xxx_2
os.rename('xxx_1', 'xxx_2')

# 获取现在所处的目录路径
os.getcwd()

# 切换到目录路径 xxx
os.chdir('xxx')

# 读取 xxx 目录路径下所有文件
os.listdir('xxx')

# 删除目录路径 xxx
os.rmdir('xxx')
```

**文件操作：**

1. 打开文件:

```python
# 打开文件 xxx 并设定文件模式 x
open('xxx', mode='x')
```

> 常见文件格式（可以组合使用）：
>
> 'r'			只读模式
>
> ‘w'			写入模式（替换文件内的所有内容）
>
> 'x'			创建一个新的可写文件
>
> ‘a’			追加内容
>
> ‘b’			字节模式
>
> ‘t’			文本模式
>
> ‘+’			打开磁盘文件进行读写

2. 读取文件:

```python
# 读取文件 xxx
xxx.read()

# 逐行读取文件 xxx
xxx.readline()
```

3. 关闭文件：

```python
# 关闭文件 xxx
xxx.close()
```

4. 重命名文件:

```python
# 重命名文件 xxx_1 为 xxx_2
os.rename('xxx_1', 'xxx_2')
```

5. 删除文件:

```python
# 删除文件 xxx
os.remove('xxx')
```





## Python 代码注释格式

1. **单行注释在 # 后加空格，与代码对齐**
2. **行内注释（不常用）主要对不熟悉的代码语句进行注释**
3. **多行注释有两种写法，与代码块之间留一个空行:**

```python
# comment_1
# comment_2
# comment_3
```

```python
"""
comment_1
comment_2
comment_3
"""
```

