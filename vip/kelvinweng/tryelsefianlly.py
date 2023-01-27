try:
    with open('handsomeb.txt') as f:
        f.read()

except FileNotFoundError as err:
    print ('文件不存在:',err)

else:
    print('打开文件没毛病，可以进一步操作')

finally:
    print('最后一定会干的事情')
