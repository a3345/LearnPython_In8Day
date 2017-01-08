#2017-1-7 10:12:41
# 剪刀:0 石头:1 布:2

#random 随机数的包;
import random

#print(random.int(0,2))

#定义两个玩家;
while(1):
    play = int(input("请输入一个数字:")) # 这里注意要强制类型转换;转换成整形;
    print("你输入的是:%d"%play)
    pc = random.randint(0,2)
    print("电脑输入的是:%d"%pc)

    if (play == 0 and pc == 2) or (play == 1 and pc == 0) or (play == 2 and pc == 1): # 注意&& ||不能使用;
        print("你赢了")
    elif play == pc :
        print("平局")
    else :
        print("你输了")
