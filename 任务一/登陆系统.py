a = 0
while a < 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "root" and password == "admin":
        print("登陆成功")
        break;
    elif username != "root" or password != "admin":
        print("用户名或密码错误")
        a += 1
if a == 3:
    print("连续三次错误锁定")
