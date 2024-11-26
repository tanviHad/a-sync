# Reverse of given number 6542

revNum = 0
num = 6542

while(num > 0):
    rem = num % 10
    revNum = (revNum * 10) + rem
    num = num // 10

print("Reverse of given number 6542 is :", revNum)