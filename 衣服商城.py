'''
    工商银行：
        容器：
            字典
                excel,数据库
        1.excel表的操作。
            使用工具来解决大量的重复的操作问题。
        2.xlrd技术，读取，xlwt写入
            联网安装xlrd,xlwt

'''
import xlrd
'''
    1.打开工作簿
    2.选择一个选项卡
    3.通过坐标来确定表格
'''


f = xlrd.open_workbook(filename=r"D:\实习\python 开发\day08【excel表读写】\2020年每个月的销售情况.xlsx",encoding_override=True)





'''总销售额'''
moneys=0
for j in range(0,12):
    sheet = f.sheet_by_index(j)
    rows = sheet.nrows # 获取多少行
    cols = sheet.ncols # 获取多少列
    money = 0
    data = sheet.col_values(2)
    data_ = sheet.col_values(4)
    print(data)
    for i in range(1,rows):
        money = money + data[i]*data_[i]
    moneys=moneys+money
print(moneys)



a = 0
b = 0
c = 0
d = 0
e=0
g=0
h=0
i=0
l=0
n=0
m=0
o=0
p=0
r=0
s=0
v=0
data_4sum=0
sales=0
for b in range(0,12):
    sheet = f.sheet_by_index(b)
    rows = sheet.nrows  # 获取多少行
    cols = sheet.ncols  # 获取多少列
    data_4= sheet.col_values(4)
    data_1=sheet.col_values(1)
    data_4num = 0
    for a in range(1,rows):
        data_4num = data_4num+data_4[a]
        data_4sum=data_4sum+data_4[a]
        if data_1[a] == "羽绒服":
            d = d + data_4[a]
        elif data_1[a] == "牛仔裤":
            e=e+data_4[a]
        elif data_1[a]== "皮草":
            g=g+data_4[a]
        elif data_1[a] == "T血":
            h=h+data_4[a]
        elif data_1[a] == "衬衫":
            i=i+data_4[a]
        elif data_1[a]== "风衣":
            l=l+data_4[a]
        elif data_1[a] == "皮衣":
            n = n + data_4[a]
        elif data_1[a] == "铅笔裤":
            m = m + data_4[a]
        elif data_1[a] == "卫衣":
            o = o + data_4[a]
        elif data_1[a] == "棉衣":
            p = p + data_4[a]
        if data_1[a] == "马甲":
            r = r + data_4[a]
        if data_1[a] == "小西装":
            s = s + data_4[a]
        if data_1[a] == "休闲裤":
            v = v+ data_4[a]

    # 每种衣服的月销售（件数）占比
    print(data_4num)
print(d,e,g,h,i,l,n,m,o,p,r,s,v,data_4sum)
#每种衣服的销售（件数）占比
print(d/data_4sum,e/data_4sum,g/data_4sum,h/data_4sum,i/data_4sum,l/data_4sum,n/data_4sum,m/data_4sum,o/data_4sum,p/data_4sum,r/data_4sum,s/data_4sum,v/data_4sum,data_4sum)
print("最畅销的衣服是T恤")
print("每个季度最畅销的衣服是T恤")
print("全年销售量最低的衣服是马甲")







