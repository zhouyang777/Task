import datetime
import random
import time

from DBUtils import select
from DBUtils import update

the_limit = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
bank_name = '中国农业银行沙河分行'



def welcome():  # 欢迎界面
    print('\t当前时间为:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('''
    ****************************************************
    *               中国农业银行账户管理系统                *
    ****************************************************
    *                       选项                        *
    *                      1.开户                       *  
    *                      2.存款                       *
    *                      3.取款                       *
    *                      4.转账                       *
    *                      5.查询                       *
    *                      6.退出                       *
    ****************************************************
    ''')
    a = input('\t请输入序号选择要办理的业务>>>')
    return a


def database_open_an_account(account, names, password, country, province, street, door, remaining_sum,
                             account_type, bank_name):  # 银行的数据库开户
    sql = "select count(*) from user"
    data = select(sql, [], mode="all")  # ((56),)

    if data[0][0] > 100:
        return 3
    sql1 = "select * from user where names  = %s"
    param1 = [names]
    data1 = select(sql1, param1, mode="all")
    if len(data1) > 0:
        return 2
    else:
        sql2 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [names, account, password, country, province, street, remaining_sum, account_type, door, bank_name,
                  the_limit, 0]
        update(sql2, param2)
        return 1


def savemoney_account():  # 银行的数据库存款
    names = input("请输入您的姓名")
    sql3 = 'select * from user where names=%s'
    param3 = [names]
    data3 = select(sql3, param3, mode="all")
    if len(data3) <= 0:
        return 2, 0
    elif len(data3) > 0:
        password = int(input("请输入密码"))

        if password == data3[0][2]:
            m = int(input("请输入要存的金额"))
            sql5 = 'update user set money=money+%s'
            param5 = [m]
            update(sql5, param5)

            sql4 = 'select * from user where names=%s'
            param4 = [names]
            data4 = select(sql4, param4, mode="all")

            return 1, data4[0][6]
        else:
            return 3, 0


def bank_drawmoney():  # 银行的数据库取钱方法
    names = input("请输入您的姓名:")
    sql3 = 'select * from user where names=%s'
    param3 = [names]
    data3 = select(sql3, param3, mode="all")
    if len(data3) <= 0:
        return (1, 0)
    elif len(data3) > 0:
        password_1 = int(input("请输入您的密码:"))
        if password_1 != data3[0][2]:
            return (2, 0)
        else:
            money = int(input('请输入您要取的金额'))
            if money > data3[0][6]:
                return (3, 0)
            else:
                sql5 = 'update user set money=money-%s'
                param5 = [money]
                update(sql5, param5)
                sql4 = 'select * from user where names=%s'
                param4 = [names]
                data4 = select(sql4, param4, mode="all")
                return (4, data4[0][6])


def bank_about():
    about_name = input('请输入您的姓名')
    sql3 = 'select * from user where names=%s'
    param3 = [about_name]
    data3 = select(sql3, param3, mode="all")
    if len(about_name) <= 0:
        return 1, None
    else:
        about_password = int(input('请输入密码'))
        if about_password != data3[0][2]:
            return 2, None
        else:
            return 3, data3


def open_an_account():  # 开户
    while 1:
        names = input("\t请输入您的姓名>>>")  # 获取用户姓名
        try:
            password = input("\t请输入您的密码>>>")  # 获取用户密码
            if len(password) != 6:
                raise ValueError()
        except ValueError:
            print('\t输入错误，密码只支持六位！')
            break
        country = input("\t请输入您的国籍>>>")  # 获取用户国籍
        province = input("\t请输入您的省份>>>")  # 获取用户省份
        street = input("\t请输入您的街道>>>")  # 获取用户街道
        door = input("\t请输入您的门牌号>>>")  # 获取用户门牌号
        try:
            remaining_sum = int(input("\t请输入您的初始账户金额>>>"))  # 获取用户账户金额
        except ValueError:
            print('\t输入错误，账户余额只支持数字！')
            break
        try:
            print('\t请输入序号选择账户类型，1.金卡  2.普通卡')
            account_type = int(input('\t>>>'))  # 获取用户类型
            if account_type != 1 and account_type != 2:
                raise ValueError()
        except ValueError:
            print('\t输入错误，请重新输入！')
            break

        account = random.randint(10000000, 99999999)  # 获取用户账号
        # 调用银行的数据库
        status = database_open_an_account(account, names, password, country, province, street, door, remaining_sum,
                                          account_type, bank_name)

        if status == 3:
            print("\t银行库已经满了！请携带证件到其他银行办理！")
        elif status == 2:
            print("\t不允许重复开户！")
        elif status == 1:
            print("\t恭喜，开户成功！")
            info = '''
    ************************个人信息**********************
    *\t姓   名:%s                                       
    *\t账   号:%s
    *\t密   码:%s
    *\t国   籍:%s
    *\t省   份:%s
    *\t街   道:%s
    *\t余   额:%s
    *\t账户类型:%s
    *\t门 牌 号 :%s
    *\t开户行名称:%s
    ****************************************************
            '''
            print(info % (
                names, account, password, country, province, street, remaining_sum, account_type, door, bank_name))
        break


def SaveMoney():  # 存款
    (a, b) = savemoney_account()
    if a == 1:
        print("存款成功")
        print("您的余额为", b)
    elif a == 2:
        print("请先开户")
    elif a == 3:
        print("密码错误")


def drawmoney_1():  # 取钱
    (c, d) = bank_drawmoney()
    if c == 1:
        print('请您先开户:')
    elif c == 2:
        print("密码错误!")
    elif c == 3:
        print("余额不足!")
    elif c == 4:
        print("取款成功!")
        print("您的余额为", d)


# 转账
def transfer_accounts():
    while True:
        go_names = input("\t请输入转出账号的姓名>>>")  # 获取转出账号用户姓名
        try:
            go_password = input("\t请输入转出账号的密码>>>")  # 获取转出账号用户密码
            if len(go_password) != 6:
                raise ValueError()
            go_password = int(go_password)
        except ValueError:
            print('\t输入错误，密码只支持六位数字！')
            break
        come_names = input("\t请输入转入账号的姓名>>>")  # 获取转入账号用户姓名
        try:
            go_money = int(input("\t请输入转账金额>>>"))  # 获取转账金额
        except ValueError:
            print('\t输入错误，账户余额只支持数字！')
            break
        try:
            sql = 'SELECT operation_time FROM user WHERE names = %s'
            time_data = select(sql, go_names, 'one')  # 获取数据库内信息
            if time_data[0] + datetime.timedelta(1) <= datetime.datetime.now():
                sql = 'UPDATE user SET  cumulative_amount=0 WHERE names=%s'
                update(sql, go_names)

            #          姓名    密码      账户余额        账户类型       累计转账金额        操作时间
            sql = 'SELECT names,password,money,account_type,cumulative_amount,operation_time' \
                  ' FROM user WHERE names = %s'
            data = select(sql, go_names, 'one')  # 获取数据库内信息
            sql = 'SELECT names,account_type FROM user WHERE names = %s'
            data2 = select(sql, come_names, 'one')  # 获取数据库内信息

            if data[1] != go_password:
                print('\t密码错误!')
                break
            elif data[2] - go_money < 0:
                print('\t账户余额不足!')
                break
            elif data[0] == data2[0]:
                print('\t账户相同!')
                break
            elif (int(data[3]) == 1 and int(data[4]) >= 50000) or (
                    int(data[3]) == 1 and int(data[4]) + go_money > 50000):
                print('\t今日已限额!')
                break
            elif (int(data[3]) == 2 and int(data[4]) >= 20000) or (
                    int(data[3]) == 2 and int(data[4]) + go_money > 20000):
                print('\t今日已限额!')
                break
            else:
                sql = 'UPDATE user SET money = money - %s WHERE names=%s '
                sql0 = 'UPDATE user SET money = money + %s WHERE names=%s '
                sql1 = 'UPDATE user SET cumulative_amount = cumulative_amount + %s WHERE names=%s '
                sql2 = 'UPDATE user SET operation_time=%s WHERE names=%s '
                param = [go_money, go_names]
                param0 = [go_money, come_names]
                param2 = [the_limit, go_names]
                update(sql, param)
                update(sql0, param0)
                update(sql1, param)
                update(sql2, param2)

                sql2 = 'SELECT names,money,account_type,operation_time FROM user WHERE names = %s'
                data = select(sql2, go_names, 'one')  # 获取数据库内信息
                info = '''
    ************************转账信息**********************
    *\t转帐姓名:%s
    *\t收款姓名:%s
    *\t转账金额:%s
    *\t账户余额:%s
    *\t账户类型:%s类卡
    *\t操作时间:%s
    *\t银行名称:%s
    ****************************************************'''
                print(info % (data[0], come_names, go_money, data[1], data[2], data[3], bank_name))
            break

        except TypeError:
            print('\t未查询到账户信息，请您开户后重试！')
            break


def about():
    (about_i, about_name) = bank_about()
    if about_i == 1:
        print('账户信息不存在')
    elif about_i == 2:
        print("密码错误")
    elif about_i == 3:
        print('信息如下')
        info = '''
                    ------------个人信息------------
                    用户名 : %s
                    账号：%s
                    取款密码 : %s
                    账户类型:%s
                    地址信息：
                        国籍：%s
                        省份：%s
                        街道：%s
                        门牌号：%s
                    余额:%s
                    开户行名称：%s
'''
        # for i in about_name[0]:
        #     print(info % (i))

        print(info % (
            about_name[0][0], about_name[0][1], about_name[0][2], about_name[0][7], about_name[0][3], about_name[0][4],
            about_name[0][5],about_name[0][8]
            , about_name[0][6], about_name[0][9]))


while True:
    option_number = welcome()
    if option_number == '1':
        open_an_account()
    elif option_number == '2':
        SaveMoney()
    elif option_number == '3':
        drawmoney_1()
    elif option_number == '4':
        transfer_accounts()
    elif option_number == '5':
        about()
    elif option_number == '6':
        print('\t欢迎您下次光临！')
        break
    else:
        print('\t输入错误！请重新输入！')
