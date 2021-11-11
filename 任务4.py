dict1= {"k1":"v1","k2":"v2","k3":"v3"}
print ("字典值 : " ,dict1)
for key,values in dict1.items():
    print(key)
    print(values)

dict1['k4']=4
print("字典值",dict1)


info = {
    '苹果':32.8,
    '香蕉': 22,
    '葡萄': 15.5
}
print(info)

f=input("请输入水果")
if f in info.keys():
    print(f,info[f])
else:
    print("未查询到")

# list1 = list(info.keys())
# list2 = list(info.values())
# i = input("请输入水果名称")
# a = list1.index(i)
# print(list2[a])


Friuts = {
    "苹果": 12.3,  # 水果和单价
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info_name= {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money': 0
    }
}
d = 0
Friuts_money = list(Friuts.values())
for name_ in info_name.keys():
    c = 0
    for a in Friuts.keys():
        b = info_name[name_]['fruits'].get(a, -1)
        if b == -1:
            continue
        else:
            c = c + b * Friuts_money[d]
            d += 1
    info_name[name_]['money'] = c
print(info_name)

#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）

def fun(c):
    dict2={}
    for i in c:
        if str(i) not in dict2:
            dict2[str(i)]=1
        else:
            dict2[str(i)]+=1
    return dict2
five=[1,5,6,"hahha"]
print(fun(five))


# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
dict_names = {}
list_tab = ['年龄','性别','编号','任职公司','薪资','部门编号']
for tab in names:
    dict_names[tab[0]] = {list_tab[x]:tab[1:][x]
                          for x in range(0,len(list_tab))}
    print('*',tab[1:],'+')
print(dict_names)

list_tab