import re


def get_current_method():
    from script import base_api
    current_methods = dir(base_api)
    methods = ["get", "post", "patch", "head", "delete", "put"]
    current_methods = [x for x in current_methods if x.split("_")[-1] in methods]
    return current_methods


def get_method_name(url: str):
    if re.match(r".*\d+", url):
        method_re = re.sub(r"_\d+", "_.+?", url)
        method_names = [x for x in get_current_method() if re.match(method_re, x)]
        if method_names:
            return method_names[0]
        else:
            return url
    else:
        return url


def get_method(url, method):
    server_name, method_name = url[1:].replace("-", "_").split("/", 1)
    file_name = method_name.split("/")[0]
    server_name = server_name
    method_name = get_method_name(method_name.replace("/", "_") + "_" + method.lower())
    print(f"from script.base_api.{server_name}.{file_name} import {method_name}")


if __name__ == '__main__':
    get_method("/api-operation-app/employee/login", "POST")
