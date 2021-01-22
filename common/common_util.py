# coding:utf-8
import string
import traceback


def replace_string(template_str: str, variable_dict: dict):
	template = string.Template(template_str)
	return template.safe_substitute(**variable_dict)


def result_calculate(pass_num, fail_num):
	pass_num = float(pass_num)
	fail_num = float(fail_num)
	count_num = pass_num + fail_num
	# 90%
	if count_num:
		pass_rate = "%.2f%%" % (pass_num / count_num * 100)
		fail_rate = "%.2f%%" % (fail_num / count_num * 100)
	else:
		pass_rate = "-"
		fail_rate = "-"
	return pass_rate, fail_rate


def get_time_diff(start, end):
	diff = str((end-start).seconds) + "s"
	return diff


def get_page_num(page_number, page_size):
	try:
		page_number = int(page_number) if int(page_number) >= 1 else 1
		page_size = int(page_size) if int(page_size) >= 1 else 10
		start_num = int((page_number - 1) * page_size)
		end_num = int(start_num + page_size)
	except ValueError as e:
		print("page_num: %s,page_size:%s,格式错误" % (page_number, page_size))
		traceback.print_exc()
		start_num = 0
		end_num = 10
	return start_num, end_num


