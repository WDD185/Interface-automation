
from common.run_method import RunMethod


def coupon_distributeAutoCouponByNewStudent_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "通用/前台业务/学生信息/发放新生优惠券"
    url = f"/service-profile/coupon/distributeAutoCouponByNewStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res
