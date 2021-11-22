'''
    增，删，改，查
    增：create  ,insert
    删除：drop,delete
    修改：update
    查询：select
    1.联网安装pymysql
        python  -m  pip install pymysql
    2.导入pymysql
    3.pymysql连接数据库
    3.创建控制台，执行sql语句
    4.准备一条sql语句
    5.使用控制台执行sql语句
        5.1 增，删，改
            提交操作即可
        5.2 查询
            提取数据
            fetchall()  提取所有
            fetchone()  提取一条
            fetchmany(size) 提取多条
    6.关闭资源

'''

import pymysql

# 连接数据库
con = pymysql.connect(host="localhost",user="root",password="root",database="bank")

# 创建控制台
cursor = con.cursor()

# 准备一条sql语句
# sql = "update user  set  money = money  + 1000"
# sql = "delete from user where username = 'jason2'"

# 模板的好处：模板是可以进行大量重复进行使用的，只需要动态向模板中填充数据即可。
sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # 模板
param = ['旺财',1002,456789,'USA','new york','linken street',6000,1,"s001",'高盛银行']


# 执行sql语句
cursor.execute(sql,param)

# 提交到数据库
con.commit()

# 关闭资源
cursor.close()
con.close()

















