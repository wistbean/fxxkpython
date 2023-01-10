avlist = ["亚洲五码","亚洲有码","欧美原创","动漫原创"]

print ("我珍藏了",len(avlist),"个类别的av")

print ("他们分别是，")

for item in avlist:
    print (item)

print ("我又发现了一个新大陆，他叫：国产原创，我要把他添加到我的列表来")

avlist.append("国产原创")

print ("现在我的列表是这样的：", avlist)

print ("给我的列表排个序吧")

avlist.sort()

print ("排序之后我的列表是这样的：", avlist)

print ("我想删掉",avlist[0])

del avlist[0]

print ("删完之后我现在的列表是这样的：", avlist)
