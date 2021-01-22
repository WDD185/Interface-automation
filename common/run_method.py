# coding:utf-8
import requests
import time
import traceback
from json.decoder import JSONDecodeError
from urllib3.connectionpool import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)
from common.operation_log import Log
log = Log.get_logger(__name__)


class RunMethod:

	@staticmethod
	def run_main(run_method, url, params=None, body_data=None, header=None, wait_time=None, time_out=60, **kwargs):
		try:
			if wait_time:
				print(f"开启等待时间{wait_time}")
				time.sleep(int(wait_time))
			if run_method == 'POST':
				res = requests.post(url, json=body_data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'GET':
				res = requests.get(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PUT':
				res = requests.put(url, json=body_data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'DELETE':
				res = requests.delete(url, json=body_data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'HEAD':
				res = requests.head(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PATCH':
				res = requests.patch(url, json=body_data, params=params, headers=header, timeout=time_out, verify=False)
			else:
				res = requests.request(method=run_method, url=url, json=body_data, params=params, headers=header, timeout=time_out, verify=False)
			res_headers = res.headers
			try:
				res_j = res.json()
			except JSONDecodeError as e:
				log.info("请求返回的接口格式错误：%s" % repr(e))
				res_j = {"res": res.text}
		except Exception as e:
			log.info("其他未知异常：%s" % repr(e))
			traceback.print_exc()
			res_j = {}
			res_headers = {}
		return res_j, res_headers


if __name__ == "__main__":
	pass


