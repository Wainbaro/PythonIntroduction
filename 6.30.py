num=18
print(num)
print(type(num))# type函数
arr=[1,2,3]# 数组/列表list
tup=(1,2,3)# 元组tuple
dic={"sss",1}# 字典dictionary
print(dic)
#变量命名，sN小驼峰，SN大驼峰，s_n下划线
import math
print(math.pi)
print("1",end="")#print默认换行，此为取消，逗号输出有空格
name=input("Input name:")
print(name)
print(type(name))
x=1
y=3
a="JINI"
b="TAIMEI"
print(x+y)
print(a+b)# -*/不适用
print("NIGANMA"*10)
if x>y:
    print("x>y")
else:
    print("x<y")
print(2**3)#幂
print(x//y)#下取整

flag=1
while flag<3:
    print("flag=",flag)
    flag+=1
else:
    print("End.")
#break跳出整个while
#continue重复这一次的循环

