# coding:utf-8
import sys
from hq_framework.main.run_api import Run
from hq_framework.main import init_conf
from hq_framework.common.operation_log import Log
log = Log(__name__).get_logger()


class GetSysArgs:
    def __init__(self, args: list):
        if len(args) == 2:
            self.ip = args[1]
            print(self.ip)
            log.info("输入的命令行参数args: %s" % args)
        else:
            print(args)
            self.ip = "132.232.15.12"
            log.info("输入的命令行参数args: %s没有ip或参数过多使用: ip: 132.232.15.12" % args)

    def get_ip(self):
        if self.ip == "geek.jkwljy.com" or self.validate_ip():
            return self.ip
        else:
            log.info("输入的ip:%s有误，使用默认Ip: ip: 132.232.15.12" % self.ip)
            return "132.232.15.12"

    def validate_ip(self) -> bool:
        sep = self.ip.split(':')[0].split(".")
        if len(sep) != 4:
            return False
        for i, x in enumerate(sep):
            try:
                int_x = int(x)
                if int_x < 0 or int_x > 255:
                    return False
            except ValueError:
                return False
        return True


if __name__ == "__main__":
    ip = GetSysArgs(sys.argv).get_ip()
    print("获取的ip:" + ip)
    log.info("用于初始化config的ip:" + ip)
    config_path = "data/config/config.conf"
    path_config_path = "data/config/data_path.conf"
    init_conf.InitConfig(ip, config_path)
    Run(config_path, path_config_path).run()

