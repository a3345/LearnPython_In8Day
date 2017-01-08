#2017-1-7 11:33:54
# 99 乘法口诀表;

'''
    要求打印以下图形;
    *
    * *
    * * *
    * * * *
    * * * * * 
'''
'''
i = 0
while i<10:
    #print("* "*30)
    j = 0
    while j<= i:
        print("* ",end = "") # end = "" 表示不换行;
        j+=1

    print("")
    i+=1
'''

i = 1

while i<=9:
    j = 1
    while j<=i:
        print("%d * %d = %-2d  "%(j,i,i*j), end = "")
        j += 1
    i +=1
    print()
