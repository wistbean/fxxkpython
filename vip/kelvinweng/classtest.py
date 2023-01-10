class duolaameng:
    def __init__(self,name):
        self.name = name
        print ("hi, "+self.name)
    def getzhuqingting(self):
        print ("给"+ self.name+ "一个竹蜻蜓")

class duolabmeng(duolaameng):
    def getchongqiwawa(self):
        print ("给"+self.name+"一个充气娃娃")

bmeng = duolabmeng("bmeng")
bmeng.getzhuqingting()
bmeng.getchongqiwawa()

ameng = duolaameng("ameng")
ameng.getzhuqingting()
