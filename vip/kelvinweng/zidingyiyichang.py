class MyError(Exception):
    def __init__(self,value):
        super().__init__(self)
        self.value =value
    def __str__(self):
        return self.value

try:
    raise MyError("自定义异常")
except MyError as err:
    print (err)
