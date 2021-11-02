#有下列人员数据库，请按要求实现
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]
i = 0
a = 0
b = 0
while i < len(names):
    a = a + names[i][5]
    b = b + int(names[i][6])
    i += 1

print("平均薪资", a / 4)
print("平均年龄", b / 4)
names.insert(2, ["刘备", "45", "男", "220", "alibaba", 500, "30"])
print(names)
# 男女人数
c = 0
num = 0
num1 = 0
list2 = []
peo = input("请输入部门编号")
while c < len(names):
    list2.append(names[c][6])
    dd = list2.count(peo)
    if names[c][2] == "女":
        num = num + 1
    else:
        num1 = num1 + 1
    c += 1
# 部门人数
print("该部门人数", dd)
print("女生人数", num)
print("男生人数", num1)



###魔法学院
# 求每个人的总成绩
print("-----------魔法学院求每个人的总成绩------------")
magic = [
    ["罗恩", 23, 35, 44],
    ["哈利", 60, 77, 68, 88, 90],
    ["赫敏", 97, 99, 89, 91, 95, 90],
    ["马尔福", 100, 85, 90]
]

mm = 0

while mm < len(magic):
    gg = 0
    cc = 0
    while gg < len(magic[mm]):
        if gg == 0:
            print(magic[mm][gg], end=":")
        else:
            cc = cc + magic[mm][gg]
        gg += 1
    print(cc)
    mm += 1

number = int(input("请输入一个数字"))
while number != 0:
    print(number % 10)
    number = number // 10





#冒泡
print("---------冒泡------------")

arr= [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
f1=0
for f1 in range(len(arr)):
    for f2 in range(0,len(arr)-f1-1):
        if arr[f2]>arr[f2+1]:
            arr[f2],arr[f2+1]=arr[f2+1],arr[f2]
print(arr)






