ll={"handsomeb":"boy","sex":"男","age":"18"}
for count,value in enumerate(ll,3):
    print(count,value)
def enumerate_1(sequence,start=0):
    n=start
    for elem in sequence:
        yield  n,elem
        n+=1
for i in enumerate_1(ll):
    print(i)
url_1 = ["https://www.doutula.com/article/list/?page=" + str(i) for i in range(0,640)]
print(url_1)