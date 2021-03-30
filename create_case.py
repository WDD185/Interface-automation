import json
import os
from urllib import parse
from common.common_util import replace_string


def get_cases(path):
    with open(path, 'r', encoding='utf-8') as file:
        case_content_json = json.loads(file.read())
        entries = case_content_json.get("log").get("entries")
        step_lists = []
        for entry in entries:
            request_data = entry.get("request")
            # print(request_data)
            try:
                response_data = json.loads(entry.get("response", {}).get("content", {}).get("text", "{}"))
            except Exception:
                response_data = {}
            url_obj = parse.urlsplit(request_data.get("url"))
            request_method = request_data.get("method")
            post_data = request_data.get("postData")
            uri = url_obj.path
            server_name, method_name = uri[1:].replace("-", "_").split("/", 1)
            step_dict = {
                "method": request_method,
                "uri": uri,
                "params": url_obj.query,
                "body": post_data.get("text") if post_data else None,
                "server_name": server_name,
                "method_name": method_name.replace("/", "_") + "_" + request_method.lower(),
                "assert_data": parse_res(response_data, "$")
            }
            step_lists.append(step_dict)
        return step_lists


def parse_res(res, path):
    assert_list = []
    if isinstance(res, dict):
        for k, v in res.items():
            if not isinstance(v, dict) and not isinstance(v, list):
                assert_list.append({
                    "variable_name": k,
                    "variable_value": v,
                    "variable_path": path + "." + str(k)
                })
            if isinstance(v, dict):
                assert_list.extend(parse_res(v, path + "." + str(k)))
            if isinstance(v, list):
                assert_list.extend(parse_res(v[0], path + "." + str(k) + "[0]"))
    return assert_list


def create_file(step_list, is_assert=False):
    current_path = os.path.join(os.getcwd(), "temp.py")
    server_names = list(set([x.get("server_name") for x in step_list]))
    import_datas = []
    for server_name in server_names:
        import_datas.append(f"from script.base_api.{server_name} import *")
    import_datas = replace_string(import_template, {"import_datas": "\r\n".join(import_datas)})
    step_str_list = []
    for step in step_list:
        assert_str_list = []
        if is_assert:
            assert_datas = step.get("assert_data")
            for assert_data in assert_datas:
                assert_str_list.append(replace_string(assert_template, assert_data))
        step["assert_data"] = "".join(assert_str_list)
        step_str_list.append(replace_string(step_template, step))
    case_data = replace_string(case_template, {"steps": "".join(step_str_list)})
    with open(current_path, "w", encoding="utf-8") as file:
        file.write(import_datas)
        file.write(case_data)


case_template = """
@allure.feature("待修改")
@allure.testcase("待修改")
class AutoCreate:

    @allure.story("待修改")
    def test_auto_create(self):
        ${steps}        
"""

step_template = """
        params = "${params}"
        body = ${body}
        res = ${method_name}(params, body=body)
        ${assert_data}
"""

assert_template = """
        ${variable_name} = jsonpath.jsonpath(res, "${variable_path}")[0] if jsonpath.jsonpath(res, "${variable_path}") else None
        pytest.assume(${variable_name} == "${variable_value}")
"""

import_template = """
import pytest
import allure
import jsonpath
${import_datas}

"""

if __name__ == '__main__':
    file_path = "/Users/huangqiang/Downloads/yf1.jkwljy.com.har"
    create_file(get_cases(file_path))
