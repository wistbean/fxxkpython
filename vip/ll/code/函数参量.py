list=[1,2,3,4]
def my_list(list):
    list.append(5)
    print(list)
my_list(list)
def my_list_1(age,high,sex="男",*args,**arge):#指定传参,*args转换为元组,**arge转为字典
    print("年龄:{} 身高:{} 性别：{} ".format(age,high,sex))
    print(args)
    print(arge)
my_list_1(18,175,"男",1234556,age1=23,age2=32)