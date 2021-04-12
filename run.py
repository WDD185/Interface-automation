import pytest
import os


if __name__ == '__main__':
    run_config = [
        "-s", "./script/ji_yun_ying_pc/test_login.py", "--alluredir", "./report/xml", "--host", "http://192.168.32.36",
        "--account", "b"
    ]
    pytest.main(run_config)
    # os模块运行allure命令，来生成html格式的报告（根据刚刚生成的配置信息）
    os.system("/Users/huangqiang/WorkPlace/allure-2.13.8/bin/allure generate ./report/xml -o ./report/html --clean")
