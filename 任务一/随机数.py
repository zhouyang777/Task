'''
random:随机数
1 导入随机数：import ramdom
2 使用这个工具里的方法randint()

'''

'''
import random
num=random.randint(0,50)
print(num)
'''

'''
猜数字
需求:
    1猜的数字是系统产生，不是自己定义
    2键盘输入
    3循环
      while条件循环
      开始，结束，自增，任务
    4判断
      if 判断条件 elif 判断条件。。。。else
    范围：0-150
    如果输入大了：温馨提示：大了
    如果输入小了，温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxx
    

'''
import random
#1.让一个系统产生一个随机数
num = random.randint(0,150)
print(num)
#2.开始输入您要猜的数
i=0
while i<10:
    i=i+1
    print("这是您猜的第",i,"次,您现在有",1000-(i*20),"元")
    number=input("请输入您猜的数：")

#判断
    if num=='q'or num =='Q':
        print("退出")
        break

    elif int(number)<num:
        print("小了")
    elif int(number)>num:
        print("大了！")
    else:
        print("恭喜猜中！本次数字为：",num,"您还剩",1000-(i*20),"元")
        break

#起始5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定，猜中加3000