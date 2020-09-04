# coding:utf-8
import sys
from hq_framework.main.run_api import Run
from hq_framework.common.operation_log import Log
from config import run_setting
log = Log(__name__).get_logger()


def get_host(args: list):
    log.info("输入的命令行参数args: %s" % repr(args))
    return args[1] if len(args) == 2 else "192.168.32.43:3000"


if __name__ == "__main__":
    host = get_host(sys.argv)
    log.info("获取的host:" + host)
    run_setting["host"] = host
    Run(run_setting).run()

