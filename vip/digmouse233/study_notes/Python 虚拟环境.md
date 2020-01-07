## Python 虚拟环境

通过 Python3 的 venv 模块（Python2 的 virtualenv 模块）在指定的位置创建指定的 Python 版本环境，这样就可以在同一个系统中运行需要不同 Python 版本的文件了，每一个虚拟环境之间互不干扰。

#### 创建 Python2 的虚拟环境

首先安装 Python2 的 virtualenv 模块:

> python2 -m pip install -user virtualenv

在所在目录下创建 Python2 的虚拟环境 venr（如无此目录会自动创建）:

> python2 -m virtualenv venr

激活 venr 虚拟环境:

> source bin/activate

#### 创建 Python3 的虚拟环境

在 xxx/xxx/xxx/xxx 目录下创建 Python3.8 的虚拟环境 venr:

> python3.8 -m venv /xxx/xxx/xxx/xxx

激活 venr 虚拟环境:

> source bin/activate

#### 取消和删除虚拟环境

取消当前虚拟环境:

> deactivate

删除 venr 虚拟环境:

> rm -r xxx/		# 虚拟环境目录