#三位数位数分离；
"""
x=int(input("请输入要分离的三位数："))
y=x//100#百位
z=x//10%10#十位
b=x%10#个位
print(x,y,z,b)"""

"""#输出一个8位数，每位数字是1-6之间
import random
for i in range(8):
    print(random.randint(1,6),end="")"""


#99乘法表
"""
i=1
while i<=9:
    j=0
    while j<=i-1:
        j=j+1
        print(j,"*",i,"=",j*i,end="  ")
    print("\n")
    i = i + 1"""


#求100-200之间的素数，并按照每五个进行打印换行
"""
k=0
for m in range(100,200):
    flag=1
    for i in range(2,m):
        if m%i == 0:
            flag=0
    if flag==1:
        print(m,end=" ")
        k+=1
        if k%5==0:
            print("\n")"""



str=input("请输入一串字符串：")
flage=0
count=0
for i in str:
    if i == " ":
        flage=0
    else :
        if flage==0:
            flage=1
            count+=1
print(str,"字符串","共有",count,"单词")


#输入五个单词，输出以元音开头的单词
"""str="AEIOUaeiou"
a_list=[]
for i in range(0,5):
    x=input("请输入一个英文单词")
    a_list.append(x)
for i in range(0,5):
    for ch in str:
        if a_list[i][0]==ch:
            print(a_list[i])
            break
        """
# 列表操作
""" 
x=[23,44,5,54,78,90,8]
print("最大值：",max(x))
print("最小值：",min(x))
print("列表长度：",len(x))
print("列表和：",sum(x))
print("升序排列：",sorted(x))
print("降序排列：",sorted(x,reverse=True))"""

#判断列表中两数之和为9的元素对
"""
nums=[2,7,11,15,1,8,7]
length=len(nums)
print("[",end="")
for i in range(length):
    for j in range(i+1,length):
        if nums[i]+nums[j]==9:
            print("(",nums[i],",",nums[j],")",end="")
print("]")"""

