import pytest
import jsonpath
from script import default_header
from common.common_config import common_config
from script.db_config import db_configs
from script.base_api.service_user.auth import auth_employee_post
from script.defalut_account import accounts
from script.base_api.service_user.departments import departments_schools_get
from script.base_api.service_user.wxMini import wxMini_auth_post
from script.base_api.api_operation_app.employee import employee_login_post


def pytest_addoption(parser):
    # 注册一个命令行选项host
    parser.addoption("--host", default="https://yf1.jkwljy.com", dest="env", help="set test run env")
    # 注册一个命令行选项db
    parser.addoption("--db", default="yf1", dest="db", help="set test database")
    # 注册一个命令行选项account
    parser.addoption("--account", default="A", dest="account", help="set run default account group")


@pytest.fixture(scope='session', autouse=True)
def get_host(pytestconfig):
    # 初始化测试环境变量
    common_config["host"] = pytestconfig.getoption('--host')

    # 初始化测试数据库配置
    common_config["db_config"] = db_configs.get(pytestconfig.getoption('--db'))


@pytest.fixture(scope="session", autouse=True)
def ji_yun_ying_login(pytestconfig):
    account = accounts.get(pytestconfig.getoption('--account').upper())
    jyy_account = account.get("jyy_account")
    body_data = {
        "type": "employee",
        "identityType": 1,
        "ip": "0.0.0.0",
        "account": jyy_account.get("account"),
        "password": jyy_account.get("password"),
        "assistant": False
    }
    res_json = auth_employee_post(body=body_data, header=default_header.jyy_header, default_assert=False)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    if tokens:
        default_header.jyy_header.setdefault("Authorization", f"Bearer {tokens[0]}")
    else:
        default_header.jyy_header.setdefault("Authorization", "token  not found")


@pytest.fixture(scope="session", autouse=True)
def gos_login(pytestconfig):
    account = accounts.get(pytestconfig.getoption('--account').upper())
    gos_account = account.get("gos_account")
    body_data = {"identifier": gos_account.get("account"), "credential": gos_account.get("password")}
    res_json = wxMini_auth_post(body=body_data, header=default_header.gos_header)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    if tokens:
        default_header.gos_header.setdefault("Authorization", f"Bearer {tokens[0]}")
    else:
        default_header.gos_header.setdefault("Authorization", "token  not found")


@pytest.fixture(scope="session", autouse=True)
def jyy_app_login(pytestconfig):
    account = accounts.get(pytestconfig.getoption('--account').upper())
    jyy_app_account = account.get("jyy_app_account")
    body_data = {"account": jyy_app_account.get("account"),
                 "password": jyy_app_account.get("password"),
                 "type": "employee",
                 "identityType": 1,
                 "ip": "0.0.0.0"
                 }
    res_json = employee_login_post(body=body_data, header=default_header.jyy_app_header)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    print("tokens", tokens)
    if tokens:
        default_header.jyy_app_header.setdefault("authorization", f"Bearer {tokens[0]}")
    else:
        default_header.jyy_app_header.setdefault("authorization", "token  not found")


@pytest.fixture(scope="session")
def get_big_area_schools():
    res = departments_schools_get(headers=default_header.jyy_header)
    schools = res.get("data")
    if schools:
        big_area_list = []
        for big_area in schools:
            school_area_id_list = []
            big_area_name = big_area.get("name", None)
            big_area_id = big_area.get("id", None)
            areas = big_area.get("children", None)
            if areas:
                for area in areas:
                    school_areas = area.get("children", None)
                    if school_areas:
                        for school_area in school_areas:
                            school_area_id = school_area.get("id", None)
                            school_area_type = school_area.get("type", 10)
                            if school_area_id and school_area_type == 30:
                                school_area_id_list.append(school_area_id)
            if big_area_name and big_area_id and school_area_id_list:
                big_area_new = {
                    "big_area_name": big_area_name,
                    "big_area_id": big_area_id,
                    "school_area_id_list": school_area_id_list
                }
                big_area_list.append(big_area_new)
            return big_area_list
        else:
            return []


@pytest.fixture(scope="session")
def get_area_schools():
    res = departments_schools_get(headers=default_header.jyy_header)
    schools = res.get("data")
    if schools:
        area_list = []
        for big_area in schools:
            areas = big_area.get("children", None)
            if areas:
                for area in areas:
                    school_area_id_list = []
                    area_name = area.get("name", None)
                    area_id = area.get("id", None)
                    school_areas = area.get("children", None)
                    if school_areas:
                        for school_area in school_areas:
                            school_area_id = school_area.get("id", None)
                            school_area_type = school_area.get("type", 10)
                            if school_area_id and school_area_type == 30:
                                school_area_id_list.append(school_area_id)
                    if area_name and area_id and school_area_id_list:
                        area_new = {
                            "area_name": area_name,
                            "big_area_id": area_id,
                            "school_area_id_list": school_area_id_list
                        }
                        area_list.append(area_new)
        return area_list
    else:
        return []

# def pytest_collection_modifyitems(session, config, items):
#     print(dir(config))
#     print(dir(items[0]))


# 1.conftest中fixture的scope参数为session，那么所有的测试文件执行前执行一次
# 2.conftest中fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
# 3.conftest中fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
# 4.conftest中fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture
