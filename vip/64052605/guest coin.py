coin = "反面"
flag = True

while flag:
    guest = input ("请猜正反面")
    if guest == "反面":
        print ("猜对了，奖励一个吻！")
        flag = False
    elif guest == "正面":
        print ("猜错了，请继续猜！")
        
