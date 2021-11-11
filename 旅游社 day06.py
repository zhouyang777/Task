city={
    "北京":{
        "昌平":{
            "八达岭":["八达岭长城"],
            "回龙观":["永旺超市","永辉超市","呷脯呷脯"]
        },
        "朝阳":{
            "景观":["玉渊潭公园"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "公园":["香山","植物园"],
            "博物馆":["军事博物馆","国家地质公园"]
        }
    },
    "上海":{}

}
shop=[
    ["联想电脑",6000],
    ["Iphone 16x plus",15000],
    ["ps5游戏机", 3500],
    ["老干妈", 7.5],
    ["老干妈", 5.5],
    ["卫龙辣条", 5],
    ["华为P50", 5500],
    ["MAC pc", 15000],
]

# def ShowCity(b):
#     while True:
#         for i in b:
#             print(i),
#         a=input("请输入")
#         if a =="Q" or a=="q":
#             print("欢迎下次光临")
#             break
#         elif a not in b:
#             print("输入错误，请重新输入")
#         else:
#             c=b[a]
#             print(b[a])
#             return c
#
#
#
# ShowCity(ShowCity(ShowCity(city)))







def showCity(data):
    for d in data:
        print(d)

mycart=[]


def shopping():
    salary = input("请输入您的余额：")
    salary = int(salary)
    while True:

        chose=input("请输入您要的商品编号:")
        if chose.isdigit(): #看chose能否看成数字
            chose = int(chose)
            #判断商品是否存在
            if chose < len(shop):
                #判断余额是否足够
                if salary >=shop[chose][1]:
                    #正常买东西
                    mycart.append(shop[chose])
                    #减去金额
                    salary=salary-shop[chose][1]
                    print("恭喜，添加成功，您的余额还剩：￥",salary)
                else:
                    print("穷鬼，选其他商品")

            else:
                print("对不起，您输入有误，请再次输入")
        elif chose=='Q'or chose=='q':
                print("欢迎下次光临，再见")
                break


while True:
    print("-------------------欢迎来到苏苏喂喂旅行社----------------------------")
    print("有以下城市可以去：")
    showCity(city)
    chose0=input("请输入你要去的城市：")
    if chose0=="q" or chose0=="Q":
        print("欢迎下次光临！")
        break
    else:
        showCity(city[chose0])
        chose1 = input("请输入您要去二级城市：")
        if chose1 == "q" or chose1 == "Q":
            print("欢迎下次光临！")
            break
        elif chose1 not in city[chose0]:
            print("输入错误，别瞎弄！")

        else:
            showCity(city[chose0][chose1])
            chose2 = input("请输入要去的具体景点：")
            if chose2 == "q" or chose2 == "Q":
                print("欢迎下次光临！")
                break
            elif chose2 not in city[chose0][chose1]:
                print("不好意思，没有这个景点！")
            else:
                showCity(city[chose0][chose1][chose2])
                print("每张票1000元/人！")
                chose3=input("是否买点纪念品？是或否，y或n")
                if chose3=="是" or chose3=="y":
                    for index, value in enumerate(shop):
                        print(index, value)
                    shopping()
                    print("-------购物车--------")
                    for index, value in enumerate(mycart):
                        print(index, value)

                else:
                    print("祝你旅游愉快")

