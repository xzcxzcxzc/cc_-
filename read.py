import csv
import numpy as np

f = open("31_40.txt")
line = f.readline()
i = 0

write_file = '31_40_3m.csv'
f_write = open(write_file, 'w', newline='')

row = 91
col = 200*10   #  现在一次采集十组数据  是之前的十倍列数 变成2000列
msg_mx = np.zeros([row, col], dtype=np.float32)
odict = {}

while line:
    msg = list(map(str, line.split()))
    try:
        if msg[0] == 'ttt=':
            # print(i, msg[1])
            if i > 90:
                odict[str((i%91))].append(msg[1])
            else:
                odict[str((i%91))] = []
            i += 1
    except:
        None
    line = f.readline()
f.close()


for i in range(row):
    for j in range(col):
        msg_mx[i, j] = np.float32(odict[str(i)][j])

"""
可以对msg_mx进行处理，等到平均数 0 1那些
"""
# ***


csv_write = csv.writer(f_write, dialect='excel')
for i in range(row):
    csv_write.writerow(msg_mx[i])
print('Finish writing...')
