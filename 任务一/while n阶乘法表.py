num=int(input("请输入n阶数字"))
a=1
sum=0
while a<=num:
    i=1
    while i<=a:
        sum=i*a
        print(i,"x",a,"=",(i*a),"\t",end="")
        i=i+1
    print('')
    a=a+1