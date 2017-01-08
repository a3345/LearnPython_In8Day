#2017-1-8 15:42:04
#list tuple dic 列表,元组,字典;

nameList1 = ["mark", "lily", "lucy"]
nameTuple = ("mark", "lily", "lucy")
nameDic = {"name1":"mark", "name2":"lily", "name3":"lucy"}

#输出
print(nameList1)
print(nameTuple)
print(nameDic)

#修改nameTuple的值
'''
    当尝试修改元组的内容时候会error;
'''
#nameTuple[0] = "park"

#输出某个字典元素;
print(nameDic["name2"])
