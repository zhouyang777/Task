'''
随机生成1000个整数;
数字范围[20,100];
输出所有不同的数字及其每个数字重复的次数,
有能力的话升序排序打印所有数字{“数字”:”次数”}
'''
'''
import random
list_0=[]
i=0
while i<1000:
    num = random.randint(20, 100)
    list_0.append(num)
    i+=1
print(list_0)
print(len(list_0))
list_1=list(set(list_0))
print(list_1)
dict_0=dict.fromkeys(list_1,0)
for j in dict_0:
 dict_0[j] = list_0.count(j)
print(dict_0)
'''



# def fun (listnum):
#     dict={}
#     for a in listnum:
#         if str(a) not in dict:
#             dict[str(a)]=1
#         else:
#             dict[str(a)]+=1
#
#
#     return dict
#
# print(fun(list))



import random
list_0=[random.randint(20,100) for i in range(1000)]
list_set=list(set(list_0))
dict_0={}
for s in list_set:
    dict_0[s]=list_0.count(s)
print(dict_0)
'''

输出商品列表，用户输入序号，显示用户选中的商品

商品列表：
       
要求:

1：页面显示 序号 + 商品名称 + 商品价格，如

​ 1 电脑 1999

​ 2 鼠标 10

2：用户输入选择的商品序号，然后打印商品名称及商品价格

3：如果用户输入的商品序号有误，则提示输入有误，并重新输入

4：用户输入Q或者q，退出程序
'''


goods = [{"name": "电脑", "price": 1999},

         {"name": "鼠标", "price": 10},

         {"name": "显示器", "price": 120},

         {"name": "内存", "price": 230}, ]

'''
for key,values in dict1.items():
    print(key)
    print(values)
'''
print(len(goods))
a=0
while a < len(goods):
    print(a+1,goods[a]["name"],goods[a]["price"])
    a+=1
while True:
    try:
        b=input("请输入商品序号")
        if b=='q' or b=='Q':
            print("退出系统")
            break
        elif int(b)<=0:
            raise IndexError
        else:
            print(b,'',goods[int(b)-1]["name"],goods[int(b)-1]["price"])
    except:
        print("请输入正确的序号")
        continue



