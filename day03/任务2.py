citylist1 = ['北京', '上海', '广东', '石家庄', '海口', ]
citylist1.insert(4,"兰州")
citylist2=["哈尔滨","长春","沈阳"]
city=citylist1+citylist2
#切片  [)
city[1:3]=["广东","上海"]
print(city)

GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
i=0
a=0
while i<len(GDP):
    a=a+GDP[i]
    i+=1
print("GDP之和",a)
print("GDP平均数",a/8)

#有以下一个列表，求其中是5的倍数的和
five=[1,5,21,30,15,9,30,24]
b=0
c=0
while b<len(five):
    if five[b]%5==0:
        c=c+five[b]
    b+=1
print("5的倍数的和",c)

#有下列列表，请编程实现列表的数据翻转
List = [1,2,3,4,5,6,7,8,9]
# d=list(reversed(List))
# print(d)
List.reverse()
print(List)

#请编程统计列表中的每个数字出现的次数
six = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
print(six)
f=int(input("请输入数字："))
num=six.count(f)
print(num)
