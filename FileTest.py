#2017-1-7 18:23:16
#提取出文件的后缀名;

fileName = ["1.py", "2.py", "3.txt", "4.jpg"]
str3 = "Hello"
#用于测试len()的用法;
print(len(str3))

for i in range(0,len(fileName)):
#可以直接遍历列表;
#for i in fileName:
    str1 = fileName[i]
    #找到最后一个小数点的索引值;
    int2 = str1.rfind(".")
    #取出最后一个小数点索引值后面的字符;

    #取出小数点之后的所有字符;
    houZui= str1[ int2+1 : :1]
    #i += 1



    #输出文件的后缀名

    print(houZui)
