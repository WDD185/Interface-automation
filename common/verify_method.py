# coding:utf-8
import json
import operator
import re


def is_contain(str_one, str_two):
    """
    判断一个字符串是否再另外一个字符串中
    str_one:查找的字符串
    str_two：被查找的字符串
    """
    if isinstance(str_one, str):
        str_one = str(str_one)
    return operator.le(str_one, str_two)


def is_equal_dict(dict_one, dict_two):
    """判断两个字典是否相等"""
    if isinstance(dict_one, str):
        dict_one = json.loads(dict_one)
    if isinstance(dict_two, str):
        dict_two = json.loads(dict_two)
    return operator.eq(dict_one, dict_two)


def test_result_verify(except_value, real_value, assert_type=None):
    print("校验期望结果的参数：except_value：%s, real_value:%s, assert_type: %s" % (except_value, real_value, assert_type))
    flag = False
    try:
        if assert_type == "equal" or assert_type is None:
            flag = operator.eq(str(real_value), except_value)
        elif assert_type.strip() == "contain":
            flag = True if str(except_value) in str(real_value) else False
        elif assert_type.strip() == "be_contain":
            flag = True if str(real_value) in str(except_value) else False
        elif assert_type.strip() == "not_contain":
            flag = False if str(except_value) in str(real_value) else True
        elif assert_type.strip() == "not_null":
            flag = True if real_value else False
        elif assert_type.strip() == "is_null":
            flag = False if real_value else True
        elif assert_type.strip() == "start_with":
            flag = str(real_value).startswith(str(except_value))
        elif assert_type.strip() == "end_with":
            flag = str(real_value).endswith(str(except_value))
        elif assert_type.strip() == "regular":
            pattern = re.compile(str(except_value), re.M)
            flag = True if pattern.findall(str(real_value)) else False
        else:
            flag = operator.eq(str(real_value), str(except_value))
    except Exception as e:
        print("断言异常：%s" % repr(e))
    return flag











