class sombody():
    def __enter__(self):
        print("进入了__enter__方法")
        return self
    def __exit__(self,type,value,trace):
        print("进入__exit__方法")
        print("value",value)
        print("trace",trace)
        print("type",type)
        return True
    def cal(self):
        return 100/0
def get_sombody():
    return sombody()
with get_sombody() as h:
    h.cal()
    # print("返回值:{}".format(h))