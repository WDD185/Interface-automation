import pytest

host = "https://yf1.jkwljy.com"
db_config = {
        'database': 'edu',
        "user": 'read_user',
        "password": 'c5JJUqmtTeaSaOTN2gs7',
        "host": '132.232.15.12',
        "port": 5432
}


def public_assert(res_json: dict):
    code = res_json.get("code", -100)
    msg = res_json.get("msg", "获取失败")
    pytest.assume(code == 0)
    pytest.assume(msg == "成功")
