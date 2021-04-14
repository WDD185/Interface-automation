import datetime
import time
from datetime import timedelta


class GetTime:
    @staticmethod
    def get_current_time():
        current_now = datetime.datetime.now()
        current_time = current_now.strftime("%Y-%m-%d %H:%M:%S")
        current_time_num = int(time.time() * 1000)
        return {"current_time": current_time, "current_time_num": current_time_num}

    @staticmethod
    def get_today():
        current_time = datetime.datetime.now()
        today_start = current_time.strftime("%Y-%m-%d 00:00:00")
        today_end = current_time.strftime("%Y-%m-%d 23:59:59")
        today_date = current_time.strftime("%Y-%m-%d")
        return {"today_start": today_start, "today_end": today_end, "today_date": today_date}

    @staticmethod
    def get_this_week():
        current_time = datetime.datetime.now()
        this_week_start = current_time - timedelta(days=current_time.weekday())
        this_week_end = current_time + timedelta(days=(6-current_time.weekday()))
        this_week_start_date = this_week_start.strftime("%Y-%m-%d")
        this_week_start_time = this_week_start.strftime("%Y-%m-%d 00:00:00")
        this_week_end_date = this_week_end.strftime("%Y-%m-%d")
        this_week_end_time = this_week_end.strftime("%Y-%m-%d 23:59:59")
        return {
                "this_week_start_date": this_week_start_date,
                "this_week_end_date": this_week_end_date,
                "this_week_start_time": this_week_start_time,
                "this_week_end_time": this_week_end_time,
                }

    @staticmethod
    def get_this_month():
        current_time = datetime.datetime.now()
        this_month_start = datetime.datetime(current_time.year, current_time.month, 1)
        this_month = current_time.month
        print(this_month)
        if this_month == 12:
            this_month_start_date = f"{current_time.year}-12-01"
            this_month_start_time = f"{current_time.year}-12-01 00:00:00"
            this_month_end_date = f"{current_time.year}-12-31"
            this_month_end_time = f"{current_time.year}-12-31 23:59:59"
        else:
            this_month_end = datetime.datetime(current_time.year, current_time.month + 1, 1) - timedelta(days=1)
            this_month_start_date = this_month_start.strftime("%Y-%m-%d")
            this_month_start_time = this_month_start.strftime("%Y-%m-%d 00:00:00")
            this_month_end_date = this_month_end.strftime("%Y-%m-%d")
            this_month_end_time = this_month_end.strftime("%Y-%m-%d 23:59:59")
        return {
                "this_month_start_date": this_month_start_date,
                "this_month_end_date": this_month_end_date,
                "this_month_start_time": this_month_start_time,
                "this_month_end_time": this_month_end_time,
                }

    @staticmethod
    def get_today_before(num):
        current_time = datetime.datetime.now()
        n_tian_qian = current_time - timedelta(days=num)
        before_time = n_tian_qian.strftime("%Y-%m-%d 00:00:00")
        before_date = n_tian_qian.strftime("%Y-%m-%d")
        return {
            f"before_date_{num}": before_date,
            f"before_time_{num}": before_time
        }

    @staticmethod
    def get_today_after(num):
        current_time = datetime.datetime.now()
        n_tian_hou = current_time + timedelta(days=num)
        after_time = n_tian_hou.strftime("%Y-%m-%d 23:59:59")
        after_date = n_tian_hou.strftime("%Y-%m-%d")
        return {
            f"after_date_{num}": after_date,
            f"after_time_{num}": after_time
        }

    @staticmethod
    def get_all():
        return {**GetTime.get_today(),
                **GetTime.get_current_time(),
                **GetTime.get_this_month(),
                **GetTime.get_this_week(),
                **GetTime.get_today_after(7),
                **GetTime.get_today_before(1),
                **GetTime.get_today_before(7),
                **GetTime.get_today_before(30)
                }

    # 获取当前时间毫秒数
    @staticmethod
    def get_current_time_millis():
        current_time = time.time()
        return int(round(current_time * 1000))


# now = datetime.datetime.now()
# # 今天
# today = now.strftime("%Y-%m-%d %H:%M:%S")
# print("今天")
# print(today)
# # 昨天
# yesterday = now - timedelta(days=1)
# print("昨天")
# print(yesterday)
# # 明天
# tomorrow = now + timedelta(days=1)
# print("明天")
# print(tomorrow)
# 当前季度
# now_quarter = now.month/3 if now.month % 3 == 0 else now.month / 3 + 1
# print("当前季度")
# print(now_quarter)
#
# # 上周第一天和最后一天
# last_week_start = now - timedelta(days=now.weekday() + 7)
# last_week_end = now - timedelta(days=now.weekday() + 1)
# print("上周第一天和最后一天")
# print(last_week_start, last_week_end)
#
#
# # 上月第一天和最后一天
# last_month_end = this_month_start - timedelta(days=1)
# last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
# print("上月第一天和最后一天")
# print(last_month_start, last_month_end)
#
# # 本季第一天和最后一天
# month = (now.month - 1) - (now.month - 1) % 3 + 1
# this_quarter_start = datetime.datetime(now.year, month, 1)
# this_quarter_end = datetime.datetime(now.year, month + 3, 1) - timedelta(days=1)
# print("本季第一天和最后一天")
# print(this_quarter_start, this_quarter_end)
#
# # 上季第一天和最后一天
# last_quarter_end = this_quarter_start - timedelta(days=1)
# last_quarter_start = datetime.datetime(last_quarter_end.year, last_quarter_end.month - 2, 1)
# print("上季第一天和最后一天")
# print(last_quarter_start, last_quarter_start)
#
# # 本年第一天和最后一天
# this_year_start = datetime.datetime(now.year, 1, 1)
# this_year_end = datetime.datetime(now.year + 1, 1, 1) - timedelta(days=1)
# print("本年第一天和最后一天")
# print(this_year_start, this_year_end)
#
# # 去年第一天和最后一天
# last_year_end = this_year_start - timedelta(days=1)
# last_year_start = datetime.datetime(last_year_end.year, 1, 1)
# print("去年第一天和最后一天")
# print(last_year_start, last_year_end)


if __name__ == "__main__":
    # print(GetTime.get_today_start_end())
    # print(GetTime.get_this_month())
    # print(GetTime.get_today_before(5))
    # print(GetTime.get_today_after(5))
    print(GetTime.get_all())
