try:
    f = open("C:/Users/10500957/Desktop/python test/xiaohuangwen.txt","a",encoding="UTF-8")
    f.write("\n 我要看苍老师!")
    print (f.read())

finally:
    if f:
        f.close()

