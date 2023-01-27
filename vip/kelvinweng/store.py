import pickle as p

#我们要存储内容的文件名

girlfriendsfile = 'girlfriend.data'

girlfriends = ['波多野结衣','苍井空','小泽玛利亚']

#把我们的女朋友写到文件里，然后存储器存储

with open(girlfriendsfile,'wb+') as f:
    p.dump(girlfriends,f)
    f.close()

del girlfriends #删掉我们的女朋友

#把我们的女朋友读回来

with open(girlfriendsfile,'rb+') as f:
    list = p.load(f)
    print (list)
