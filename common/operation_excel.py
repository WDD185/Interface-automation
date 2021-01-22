# coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
import os


class OperationExcel:
    def __init__(self, file_name, sheet_name):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name
        else:
            print("excel的路径和sheetname不能为空", file_name, sheet_name)

    # 获取sheets的内容
    def get_sheet(self):
        data = xlrd.open_workbook(self.file_name, encoding_override="utf-8")
        tables = data.sheet_by_name(self.sheet_name)
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.get_sheet()
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.get_sheet().cell_value(row, col)

    # 根据data,列号，找到找到对应行的内容
    def get_row_datas(self, data, col_id):
        row_nums = self.get_row_num(data, col_id)
        rows_datas = self.get_row_values(row_nums)
        return rows_datas

    # 根据对应的1个内容找到对应的行号
    def get_row_num(self, data, col_id):
        nums = []
        num = 0
        cols_data = self.get_cols_data(col_id)
        for col_data in cols_data:
            if data == col_data:
                nums.append(num)
            num = num + 1
        return nums

    # 根据行号，找到该行的内容
    def get_row_values(self, row_nums):
        tables = self.get_sheet()
        row_datas = []
        for num in row_nums:
            row_data = tables.row_values(num)
            row_datas.append(row_data)
        return row_datas

    # 获取某一列的内容
    def get_cols_data(self, col_id):
        if col_id:
            cols = self.get_sheet().col_values(col_id)
        else:
            cols = self.get_sheet().col_values(0)
        return cols


if __name__ == '__main__':
    pass
# opers = OperationExcel()
# print(opers.get_cell_value(1, 2))
