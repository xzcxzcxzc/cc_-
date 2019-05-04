#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据

import xlrd

xlsx_name = '251_300_test.xlsx'
res_name = xlsx_name[:-5] + '.txt'

res_file = open(res_name, 'w')
data = xlrd.open_workbook(xlsx_name) # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows      # 获取表的行数
for i in range(nrows):   # 循环逐行打印
    # print(table.row_values(i)[:13]) # 取前十三列
    msg_write = '.alter\n.param vthn= %.5f       $ %d\n.param vthp= %.5f\n\n'%(table.row_values(i)[0], i+1, table.row_values(i)[1])
    #print(msg_write)
    res_file.write(msg_write)
