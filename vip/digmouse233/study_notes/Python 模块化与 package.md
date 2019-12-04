##Python 模块化与 package

不应该将所有的功能代码实现写到同一个文件中，而应该将代码进行模块化、归类、整理，以便日后的使用和检索，模块化在越大的项目文件中好处越大。

#### 模块

引用模块:

```python
# 直接引用模块 xxx
import xxx

# 引用模块 xxx 中的 func 方法
from xxx import xxx

# 应用模块 xxx 下的所有内容 (调用时不需声明模块)
from xxx import *
```

Python 寻找模块的顺序：

当前 Python 文件路径 ——> Python 设置的环境变量 ——> 系统的默认路径

#### package

等同于一个目录，用于区分不同不同目录下相同名称的模块

引用 package 下的模块:

```python
# 引用 package_1 目录下模块 xxx 中的 func 方法
from package_1.xxx import func

# 引用 package_1 目录下模块 xxx 中的 func_1 方法并起别名为 func_2
from package_1.xxx import func_1 as func_2
```

