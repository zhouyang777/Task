a=int(input("请输入第一条边"))
b=int(input("请输入第二条边"))
c=int(input("请输入第三条边"))
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print("不能构成三角形")
else:
    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("生成直角三角形")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("生成等腰三角形")
    elif a==b==c:
        print("生成等边三角形")
    else:
        print("普通三角形")

