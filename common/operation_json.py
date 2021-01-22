# coding:utf-8
import json
import jsonpath


class OperetionJson:

	# 读取json文件
	def read_data(self, file_path):
		with open(file_path, "r", encoding="utf-8") as fp:
			data = json.load(fp)
			return data

	# 根据关键字获取数据
	def get_data(self, id, data):
		print(type(data))
		return data[id]

	# 写json
	def write_data(self, file_path, data):
		with open(file_path, 'w', encoding="utf-8") as fp:
			fp.write(json.dumps(data))


if __name__ == '__main__':
	opj = OperetionJson()
	json_string = opj.read_data("test_json.json")
	print(jsonpath.jsonpath(json_string, "$.data.content[0,1,2].courseIds"))
