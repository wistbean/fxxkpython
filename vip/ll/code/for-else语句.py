    #筛选0-19的奇数
for i in range(20):
    for x in range(i,i+1):
        if x %2==0:
            break
    else:
        print(x)