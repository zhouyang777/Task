import time
from threading import Thread

box = 0


class chef(Thread):
    chefname = ""
    num = 0

    def run(self) -> None:
        global box
        start = time.time()
        while True:
            end = time.time()
            if end - start < 60:
                if box < 500:
                    box += 1
                    self.num += 1
                else:
                    time.sleep(3)
            else:
                break
        return self.num



class user(Thread):
    username = ""
    count = 0
    money = 5000

    def run(self) -> None:
        global box
        start = time.time()
        while True:
            end = time.time()
            if end - start < 60:
                if box > 0:
                    if self.money >= 3:
                        self.money -= 3
                        self.count += 1
                        box -= 1
                    else:
                        break
                else:
                    time.sleep(2)
            else:
                break
        print("我是超级有钱的", self.name, "我今天买了", self.count, "个蛋挞，花了", self.count * 3, "元")


c1 = chef()
c1.name = "李大嘴"
c2 = chef()
c2.name = "小福贵"
c3 = chef()
c3.name = "小当家"
u1 = user()
u1.name = "王思聪"
u2 = user()
u2.name = "秦奋"
u3 = user()
u3.name = "马云"
u4 = user()
u4.name = "马化腾"
u5 = user()
u5.name = "王健林"
u6 = user()
u6.name = "董明珠"

c1.start()
c2.start()
c3.start()
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()

c1.join()
c2.join()
c3.join()
u1.join()
u2.join()
u3.join()
u4.join()
u5.join()
u6.join()
print("我是", c1.name, "大厨，我今天做了", c1.num, "个蛋挞，我今天挣了", c1.num * 1.5, "元")
print("我是", c2.name, "大厨，我今天做了", c2.num, "个蛋挞，我今天挣了", c2.num * 1.5, "元")
print("我是", c3.name, "大厨，我今天做了", c3.num, "个蛋挞，我今天挣了", c3.num * 1.5, "元")