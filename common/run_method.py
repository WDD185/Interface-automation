# coding:utf-8
import requests
import time
import traceback
from json.decoder import JSONDecodeError
from urllib3.connectionpool import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)


class RunMethod:

	@staticmethod
	def run_main(run_method, url, params=None, body_data=None, header=None, wait_time=None, time_out=60, **kwargs):
		try:
			print(run_method, url, params, body_data, header)
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
				res_j = {"res": res.text}
		except Exception as e:
			traceback.print_exc()
			res_j = {}
			res_headers = {}
		return res_j, res_headers

	@staticmethod
	def run_request(run_method, url, params=None, data=None, header=None, run_json=True, **kwargs):
		try:
			time_out = kwargs.get("time_out") if kwargs.get("time_out") else 60
			if run_method == 'POST':
				res = requests.post(url, json=data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'GET':
				res = requests.get(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PUT':
				res = requests.put(url, json=data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'DELETE':
				res = requests.delete(url, json=data, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'HEAD':
				res = requests.head(url, params=params, headers=header, timeout=time_out, verify=False)
			elif run_method == 'PATCH':
				res = requests.patch(url, json=data, params=params, headers=header, timeout=time_out, verify=False)
			else:
				res = requests.request(method=run_method, url=url, json=data, params=params, headers=header, timeout=time_out, verify=False)
			if run_json:
				try:
					res = res.json()
				except JSONDecodeError as e:
					res = {"err_msg": str(e), "res": res}
		except Exception as e:
			res = {"err_msg": str(e)}
		return res


if __name__ == "__main__":
	pass


