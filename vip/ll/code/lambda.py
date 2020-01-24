my_list=[i for i in range(10)]
print(list(map(lambda x:x+2,my_list)))
print(tuple(filter(lambda x:x%2==0,my_list)))