list=[1,2,3,4,5,6,7,8]
print(list[::-1])#倒序输出
print(list[-5:-3])
print(list[3:5])
del list[2]#指定序列删除元素
print("#删除元素",list)
list.insert(2,7)#指定序列添加元素
print("#指定序列添加元素",list)
list.append(7)#末尾添加元素
print("#指定序列添加元素",list)
list.reverse()
print("倒序输出",list)
list.pop()#删除最后一个元素
list.clear()#清空列表