## Python 装饰器

如果函数 xxx_1 作为参数传入 xxx_2 函数并被其使用，且在最后改变了 xxx_2 函数的返回结果，我们便称函数 xxx_2 为装饰器:

```python
def xxx_2(func):
  def inner_func():
    # statement
    func()
  return inner_func

@xxx_2
def xxx_1():
  # statement
```

装饰器可以将逻辑代码与业务分离开来，降低代码的耦合度，提高代码的使用率:

```python
# 用户登陆验证案例
def user_check(func):
  def wrapper(username, password):
    if(username != 'root'):
      raise Exception('Permission Denied')
    elif(password != '1234'):
      raise Excepetion('Password Incorrect')
    else:
      return func(username, password)
  return wrapper

@user_check
def login_user(username, password):
  print('Login Success')
```

