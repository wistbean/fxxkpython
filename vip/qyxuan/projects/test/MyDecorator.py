def user_check(func):
    def wrapper(username, password):
        if(username != 'root'):
            raise  Exception('permission denied')
        elif(password != '1234'):
            raise  Exception('password incorrect')
        else:
            try:
                # return func(username, password)
                return func #此处为什么一定要带参数
            except Exception as err:
                print("程序发生异常，错误信息, {}".format(err))
    return wrapper

@user_check
def login_user(username, password):
    print('login success')

# login_user('qyxuan', '1234')
# login_user('root', '1111')
login_user('root', '1234')
#
# def func_1(func):
#     def func_inner(*args, **kwargs):
#         print("func_1")
#         func(*args, **kwargs)
#     return func_inner   #此处不能加（）
# #
# def func_2(func):
#     def func_inner(something):
#         print("func_2")
#         func(something)
#     return func_inner
#
# @func_1
# @func_2
# def say(something):
#     print(something)
#
# say("qyxuan python")
