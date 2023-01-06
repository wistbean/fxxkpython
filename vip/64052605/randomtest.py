import random

a = []

while True:
    num = random.randint(1,10)
    if num == 6:
        break
    a.append(num)

print (a)
