#2017-1-8 15:59:47
#给8位老师随机分配在3个教室之中;


#定义两个列表,分别存储老师和教室
import random #导入随机包;
teaName = ["tea0", "tea1", "tea2", "tea3", "tea4", "tea5", "tea6", "tea7"]
roomList = [ [], [], []]

#print(teaName) #测试是否成功;
#print(roomList)

#把每个老师列表中的元素追加到roomList当中;
i = 0
j = 1
#k = 0
while j<=10:
    #初始化:先清空roomList[]列表里面的元素,为下次循环做好准备;
    for roomTemp2 in roomList:
        roomTemp2.clear() #clear() 清空里面的数据;
        #k += 1
    
    for teaTemp in teaName:
        #for roomTemp in roomList:
            i = random.randint(0, len(roomList)-1)
            roomList[i].append(teaTemp) #随机选一个房间给他装进去;

            i += 1
    j += 1

    #print(roomList)
    #遍历输出二元列表;
    print("第%d次分组"%(j-1))
    for roomTemp in roomList:
        #print("第%d个教室"%)
        print(roomTemp)
    print("===="* 20)


