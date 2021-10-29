i,b,c=0,0,0
a=0
while i<10:
    i+=1
    a=int(input("请输入数字"))
    if a>b:
        b=a
    c=c+a
print(b)
print(c)
print(c/10)