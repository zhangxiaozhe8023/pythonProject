# -*- coding: utf-8 -*-
# __author__:zhangxiaozhe
# 2020/10/31 9:19
import sys
from sys import argv,path
print("命令行参数为                                     ：")
for i in  sys.argv:
    print(i)
print(sys.argv)

print('\n python 路径为',path)
#必须缩进对齐
if True:
    print("true")

else:
    print("false")
#实现+ \实现多行切换
a = 5 + 3 + \
    2 + 3
ab= "dsfsd" + \
    "dsdfsd"
print(ab)
str="rubnnvb"
print(r""+str)
expression =1
if expression:
    print("333",end="")
elif expression:
    print("3333")
else:
    print("33333")
print("66666")
counter=100
minles =1000.0
name= "zxz"
print(counter)
print(minles)
print(name)
#多个变量赋值,三个变量都赋予相同的数值
a=b=c=1
a,b,c=1,2,3

#标准数据类型 number。String，List，Tuble，Set，Dictiomcary
#不可变变量：number，String，Tuble
#可变数据：List 、Dictionary,Set
str ='RUnoob'
print(str[0:-1])
print(str[2:5])
print(str[2:])
list1= ['google','runoob',1997,2000,1,2,3,4,5,6]
print(list1[-2])
print(list1[0:2])
print(len(list1))
#更新列表、
print('第三个元素是:',list1[2])
list1[2]='张晓哲'
list1.append('zxz')
print('更新后的第三个元素是'+list1[2])
print('原始更新后的元素是',list1)
del list1[2]
print('删除后的list集合',list1)
#长度
print(len(list1))
#组合
print(list1 + [7, 8, 9])
#重复

print("重复后的",list1*2)
#元素是否存在
print("zxz" in list1)

#迭代
for x in list1:
    print(x,end='')
print("\n")
print(list1[1:])
print("aaaaa",list1)
list1, list2 = ['Google', 'Runoob', 'Taobao','Taobao'], [456, 700, 200]
print('zuida',max(list1))

min(list1)
for i in range(len(list1)):
    print(list1[i])
for item in list1:
    print(item)
print("dd",list1.count("Taobao"))
#元组









