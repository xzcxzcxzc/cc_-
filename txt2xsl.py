#file_affilication = open('Affiliations.txt','r')
import xlwt
import os
import sys

filename = './ttt.txt'
xlsname = './tt2ex.xls'

f = open(filename)
xls = xlwt.Workbook()
        #生成excel的方法，声明excel
sheet = xls.add_sheet('sheet',cell_overwrite_ok=True)
x = 0   #在excel开始写的位置（y）
line = f.readline()
while line:
    line = f.readline()
    line1=line.lstrip('   ttt=  ')  # 去除首尾字符 0   ttt=
    sheet.write(x,line1 )
    x += 1  #另起一行
    f.close()
    xls.save(xlsname)        #保存为xls文件

    # f = open("./ttt.txt")

    # line = f.readline()
    # while line:
    #     line = f.readline()
    #     print(line.lstrip('   ttt=  '))  # 去除首尾字符 0   ttt=
    #
    # f.close()

#
# if __name__ == '__main__':
#     filename = './ttt.txt'
#     xlsname = './tt2ex.xls'
#     txt_xls(filename,xlsname)