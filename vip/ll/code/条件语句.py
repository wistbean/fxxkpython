class sentence():
    def __init__(self):
        self.if_number=17
        self.while_number=10
    def _if(self):

        if int(self.if_number)<18:
            print("太小了")
        elif int(self.if_number)==18:
            print("刚刚好")
        else :
            print("太大了")
    def _while(self):
        while self.while_number<18:
            print("太小了，疯狂长大")
            self.while_number+=1
            print(self.while_number)
        print("大小刚刚好\n{}cm!".format(self.while_number))
    def _for(self):
        for i in range (10):
            if i%2==0:
                continue
            print(i)
if __name__=="__main__":
    dw=sentence()
    dw._if()
    dw._while()
    dw._for()