import pytest


def public_assert(res_json: dict):
    code = res_json.get("code", -100)
    msg = res_json.get("msg", "获取失败")
    pytest.assume(code == 0)
    pytest.assume(msg == "成功")