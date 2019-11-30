## Python 赋值

Python 是动态类型机制（在运行时自动决定类型），不需要我们对变量指定数据类型。**Python 中的变量名称，和具体的对象是没有关联的。**

Python 只关心对象本身，所以更为贴切的来讲，

​        Origin					Better

变量 (variable)          名称 (name)

​         赋值                       贴标签

在下面的例子中，数字 1 与 a，b 指向同一个对象内存地址：

```python
>>> a = 1
>>> b = 1
>>> id(1)
xxxxxxx
>>> id(a)
xxxxxxx
>>> id(b)
xxxxxxx
```

**Python 所谓赋值，相当于“变量名称”这个标签贴在了“对象”身上。**