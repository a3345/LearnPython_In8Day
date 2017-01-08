#2017-1-7 16:30:43
#findTest,字符串的查找;

str1 = "Hello, i am the Hello kitty!"

#字符串的查找;
#从左边开始查找;
int1 = str1.find("He",0,len(str1))
#从右边开始查找;
int2 = str1.rfind("He",0,len(str1))

int6 = str1.find("Heoo")

print(int1)
print(int2)
print(int6) #str.find找不到东西,那么 结果是 -1

#字符串的查找2,index

int3 = str1.index("He")

int4 = str1.rindex("He")

#int5 = str1.index("Heoo")

print(int1, int2)

#pirnt(int5)
