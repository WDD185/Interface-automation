import pytest


def public_assert(res_json: dict):
    code = res_json.get("code", -100)
    msg = res_json.get("msg", "获取失败")
    pytest.assume(code == 0)
    pytest.assume(msg == "成功")


def assert_res_field_contain_value(data_list: list, value: str):
    if data_list:
        err_values = [x for x in data_list if value not in x]
        if err_values:
            flag = False
        else:
            flag = True
    else:
        flag = False
    return flag


def assert_res_field_equal_value(data_list: list, value: str):
    if data_list:
        err_values = [x for x in data_list if str(value) != str(x)]
        if err_values:
            flag = False
        else:
            flag = True
    else:
        flag = False
    return flag


def assert_res_field_order(data_list: list, order_type="desc"):
    if data_list:
        if order_type == "desc":
            err_datas = []
            num = len(data_list)
            for x in range(1, num):
                if data_list[x] > data_list[x-1]:
                    err_datas.append(data_list[x])
            if err_datas:
                flag = False
            else:
                flag = True
        else:
            err_datas = []
            num = len(data_list)
            for x in range(1, num):
                if data_list[x] < data_list[x-1]:
                    err_datas.append(data_list[x])
            if err_datas:
                flag = False
            else:
                flag = True
    else:
        flag = False
    return flag

