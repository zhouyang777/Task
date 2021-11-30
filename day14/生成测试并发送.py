import unittest
from unittestreport import TestRunner

tests = unittest.defaultTestLoader.discover(r"D:\实习\python 开发\task\day14",pattern="Test*.py")

runner = TestRunner(tests,
                    filename="report.html",
                    report_dir="11",
                    title="计算器加法测试报告",
                    tester="周洋",
                    desc="计算器加法项目测试生成的报告",
                    templates=3)
runner.run()
runner.send_email(host="smtp.qq.com",
                  password='kwnhowoxqqklgdge',
                  port=465,
                  to_addrs="1501930527@qq.com",
                  user="1501930527@qq.com")