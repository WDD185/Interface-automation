# coding:utf-8
import requests
import json
from json.decoder import JSONDecodeError
from common.common_config import common_config
from urllib3.connectionpool import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)


class RunMethod:

	@staticmethod
	def run_request(run_method, url, params=None, body=None, header=None, return_json=True, **kwargs):
		try:
			host = kwargs.get("host")
			config_host = common_config.get("host")
			host = host or config_host
			api_name = kwargs.get("name")
			if not url.startswith("http"):
				url = host + url
			time_out = kwargs.get("time_out") if kwargs.get("time_out") else 60
			if isinstance(body, dict) or isinstance(body, list):
				body = json.dumps(body, ensure_ascii=False).encode()
			if run_method == 'POST':
				res = requests.post(url, data=body, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'GET':
				res = requests.get(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PUT':
				res = requests.put(url, data=body, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'DELETE':
				res = requests.delete(url, data=body, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'HEAD':
				res = requests.head(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PATCH':
				res = requests.patch(url, data=body, params=params, headers=header, timeout=time_out, verify=False)
			else:
				res = requests.request(method=run_method, url=url, data=body, params=params, headers=header, timeout=time_out, verify=False)
			if return_json:
				try:
					res = res.json()
				except JSONDecodeError as e:
					res = {"err_msg": str(e), "res": res}
		except Exception as e:
			res = {"err_msg": str(e)}
		# print(res)
		import allure
		if return_json:
			allure.attach(body=json.dumps(res, ensure_ascii=False), name='响应信息', attachment_type=allure.attachment_type.JSON)
		else:
			allure.attach(body=res.text, name='响应信息', attachment_type=allure.attachment_type.TEXT)
		return res


if __name__ == "__main__":
	pass
