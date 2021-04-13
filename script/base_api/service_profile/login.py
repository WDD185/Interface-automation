
from common.run_method import RunMethod


def login_verificationCode_receiveVerificationCode_studentPhoneNum_phoneNumber_get(verificationCode, studentPhoneNum, params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/使用手机验证码登录"
    url = f"/service-profile/login/{verificationCode}/receiveVerificationCode/{studentPhoneNum}/phoneNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

