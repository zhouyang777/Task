j =int(input("请输入您要打印的星星："))
while j >0:
    for i in range(1,j):
        print(" "*(j),"* "*(i))
        j-=1