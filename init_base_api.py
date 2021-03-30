from common.connect_db import OperationDb
from common.common_util import replace_string
import os


def get_base_apis():
    config = {
        'database': 'edu',
        "user": 'read_user',
        "password": 'c5JJUqmtTeaSaOTN2gs7',
        "host": '132.232.15.12',
        "port": 5432
    }
    sql = """SELECT name, server_name, url, http_method FROM service_user.permission WHERE type = 'URL'"""
    query_result = OperationDb(config).query_sql(sql)
    base_apis = [{
        "name": x[0],
        "server_name": x[1].replace("-", "_"),
        "url": x[2],
        "http_method": x[3],
        "method_name": x[2].replace("{", "").replace("}", "").replace("-", "_").replace("/", "_")[1:] + "_" + x[3].lower(),
        "file_name": x[2].replace("-", "_")[1:].split("/")[0] + "_temp.py"
    } for x in query_result]
    return base_apis


def create_all(base_apis: list):
    server_names = list(set([x.get("server_name") for x in base_apis]))
    current_path = os.getcwd()
    import_data_out = []
    for server_name in server_names:
        folder_path = os.path.join(current_path, "script/base_api/" + server_name)
        folder_apis = [x for x in base_apis if x.get("server_name") == server_name]
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        file_names = list(set([x.get("file_name") for x in folder_apis]))
        init_file_path = os.path.join(folder_path, "__init__.py")
        import_datas = []
        for file_name in file_names:
            file_apis = [x for x in base_apis if x.get("file_name") == file_name]
            file_path = os.path.join(folder_path, file_name)
            create_file(file_path, file_apis)
            import_datas.append(f"from script.base_api.{server_name}.{file_name.replace('.py', '')} import *")
        create_init_file(init_file_path, import_datas)
        import_data_out.append(f"from script.base_api.{server_name} import *")
    create_init_file("script/base_api/__init__.py", import_data_out)


def get_current_method(**kwargs):
    from script import base_api
    current_methods = dir(base_api)
    print(dir(base_api))
    print(len(dir(base_api)))


def create_file(path, base_apis):
    with open(path, "w", encoding="utf-8") as file:
        file.write(file_template)
        for base_api in base_apis:
            http_method = base_api["http_method"]
            if http_method.upper() == "GET":
                data = replace_string(get_template, base_api)
            elif http_method.upper() == "POST":
                data = replace_string(post_template, base_api)
            elif http_method.upper() == "HEAD":
                data = replace_string(head_template, base_api)
            elif http_method.upper() == "PUT":
                data = replace_string(put_template, base_api)
            elif http_method.upper() == "PATCH":
                data = replace_string(patch_template, base_api)
            elif http_method.upper() == "DELETE":
                data = replace_string(delete_template, base_api)
            else:
                data = replace_string(post_template, base_api)
            file.write(data)


def create_init_file(path, import_datas):
    with open(path, "w", encoding="utf-8") as file:
        for import_data in import_datas:
            file.write(import_data)
            file.write("\r\n")


get_template = """
@allure.step("${name}")
def ${method_name}(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

post_template = """
@allure.step("${name}")
def ${method_name}(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

put_template = """
@allure.step("${name}")
def ${method_name}(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):    
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

delete_template = """
@allure.step("${name}")
def ${method_name}(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

patch_template = """
@allure.step("${name}")
def ${method_name}(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

head_template = """
@allure.step("${name}")
def ${method_name}(params=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/${server_name}${url}"
    res = RunMethod.run_request("HEAD", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

"""

file_template = """
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure

"""

if __name__ == '__main__':
    # create_all(get_base_apis())
    get_current_method()
