#2017-1-7 19:31:56
#列表元素的  增加 删除 查

#新建一个测试列表

fruit = ["apple","pearr","banana"]
fruit2 = ["aa","bb"]

fruit.append("xxx")

print(fruit)
#c插入到索引0的前面;
fruit.insert(0,"xxx")

print(fruit.extend(fruit2))
for i in fruit:
    print(i)
print(fruit2.extend(fruit))

print(fruit)
