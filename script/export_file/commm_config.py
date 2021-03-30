import pytest

header = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
login_data = {"type": "employee",
              "identityType": 1,
              "ip": "0.0.0.0",
              "account": "15360956010",
              "password": "88888888",
              "assistant": False
            }


def public_assert(res_json: dict):
    code = res_json.get("code", -100)
    msg = res_json.get("msg", "获取失败")
    pytest.assume(code == 0)
    pytest.assume(msg == "成功")