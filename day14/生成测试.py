import unittest
import time
from HTMLTestRunner import HTMLTestRunner
#1,加载所有用例
tests=unittest.defaultTestLoader.discover(r"D:\实习\python 开发\task\day14",pattern="Test*.py")
#2用运行期运行这些用例
run=HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是计算器的测试报告",
#测试报告的详细程度
    verbosity=1,
    stream=open("计算器报告.html",mode="w+",encoding="utf-8")

)
#运行
run.run(tests)

time.sleep(10)

import zmail
# 你的邮件内容
mail_content = {
    'subject': 'Success!',  # 随便填写
    'content_text': '！',  # 随便填写
    'attachments': 'D:\实习\python 开发\\task\day14\计算器报告.html'
}

# 使用你的邮件账户名和密码登录服务器
server = zmail.server('1501930527@qq.com', 'kwnhowoxqqklgdge')
# 发送邮件
server.send_mail('3121114552@qq.com',mail_content )


