import csv
import numpy as np

f = open("201_250.txt")
line = f.readline()
i = 0
nset = 40


write_file1 = '161_3m.xlsx'
write_file2 = '162_3m.xlsx'
write_file3 = '163_3m.xlsx'
write_file4 = '164_3m.xlsx'
write_file5 = '165_3m.xlsx'
write_file6 = '166_3m.xlsx'
write_file7 = '167_3m.xlsx'
write_file8 = '168_3m.xlsx'
write_file9 = '169_3m.xlsx'
write_file10 = '170_3m.xlsx'

write_file11 = '171_3m.xlsx'
write_file12 = '172_3m.xlsx'
write_file13 = '173_3m.xlsx'
write_file14 = '174_3m.xlsx'
write_file15 = '175_3m.xlsx'
write_file16 = '176_3m.xlsx'
write_file17 = '177_3m.xlsx'
write_file18 = '178_3m.xlsx'
write_file19 = '179_3m.xlsx'
write_file20 = '180_3m.xlsx'

write_file21 = '181_3m.xlsx'
write_file22 = '182_3m.xlsx'
write_file23 = '183_3m.xlsx'
write_file24 = '184_3m.xlsx'
write_file25 = '185_3m.xlsx'
write_file26 = '186_3m.xlsx'
write_file27 = '187_3m.xlsx'
write_file28 = '188_3m.xlsx'
write_file29 = '189_3m.xlsx'
write_file30 = '190_3m.xlsx'

write_file31 = '191_3m.xlsx'
write_file32 = '192_3m.xlsx'
write_file33 = '193_3m.xlsx'
write_file34 = '194_3m.xlsx'
write_file35 = '195_3m.xlsx'
write_file36 = '196_3m.xlsx'
write_file37 = '197_3m.xlsx'
write_file38 = '198_3m.xlsx'
write_file39 = '199_3m.xlsx'
write_file40 = '200_3m.xlsx'

# write_file41 = '191_3m.xlsx'
# write_file42 = '192_3m.xlsx'
# write_file43 = '193_3m.xlsx'
# write_file44 = '194_3m.xlsx'
# write_file45 = '195_3m.xlsx'
# write_file46 = '196_3m.xlsx'
# write_file47 = '197_3m.xlsx'
# write_file48 = '198_3m.xlsx'
# write_file49 = '199_3m.xlsx'
# write_file50 = '200_3m.xlsx'



f_write1 = open(write_file1, 'w', newline='')
f_write2 = open(write_file2, 'w', newline='')
f_write3 = open(write_file3, 'w', newline='')
f_write4 = open(write_file4, 'w', newline='')
f_write5 = open(write_file5, 'w', newline='')
f_write6 = open(write_file6, 'w', newline='')
f_write7 = open(write_file7, 'w', newline='')
f_write8 = open(write_file8, 'w', newline='')
f_write9 = open(write_file9, 'w', newline='')
f_write10 = open(write_file10, 'w', newline='')



f_write11 = open(write_file11, 'w', newline='')
f_write12 = open(write_file12, 'w', newline='')
f_write13 = open(write_file13, 'w', newline='')
f_write14 = open(write_file14, 'w', newline='')
f_write15 = open(write_file15, 'w', newline='')
f_write16 = open(write_file16, 'w', newline='')
f_write17 = open(write_file17, 'w', newline='')
f_write18 = open(write_file18, 'w', newline='')
f_write19 = open(write_file19, 'w', newline='')
f_write20 = open(write_file20, 'w', newline='')



f_write21 = open(write_file21, 'w', newline='')
f_write22 = open(write_file22, 'w', newline='')
f_write23 = open(write_file23, 'w', newline='')
f_write24 = open(write_file24, 'w', newline='')
f_write25 = open(write_file25, 'w', newline='')
f_write26 = open(write_file26, 'w', newline='')
f_write27 = open(write_file27, 'w', newline='')
f_write28 = open(write_file28, 'w', newline='')
f_write29 = open(write_file29, 'w', newline='')
f_write30 = open(write_file30, 'w', newline='')



f_write31 = open(write_file31, 'w', newline='')
f_write32 = open(write_file32, 'w', newline='')
f_write33 = open(write_file33, 'w', newline='')
f_write34 = open(write_file34, 'w', newline='')
f_write35 = open(write_file35, 'w', newline='')
f_write36 = open(write_file36, 'w', newline='')
f_write37 = open(write_file37, 'w', newline='')
f_write38 = open(write_file38, 'w', newline='')
f_write39 = open(write_file39, 'w', newline='')
f_write40 = open(write_file40, 'w', newline='')

row = 37
col = 200*nset  #  现在一次采集十组数据  是之前的十倍列数 变成2000列
msg_mx = np.zeros([row, col], dtype=np.float32)
odict = {}

while line:
    msg = list(map(str, line.split()))
    try:
        if msg[0] == 'ttt=':
            # print(i, msg[1])
            if i > 36:
                odict[str((i%37))].append(msg[1])
            else:
                odict[str((i%37))] = []
            i += 1
    except:
        None
    line = f.readline()
f.close()


for i in range(row):
    for j in range(col):
        msg_mx[i, j] = np.float32(odict[str(i)][j])
    #print( msg_mx[])
    #print (msg_mx)
"""
可以对msg_mx进行处理，等到平均数 0 1那些
"""
# ***

csv_write1 = csv.writer(f_write1, dialect='excel')
csv_write2 = csv.writer(f_write2, dialect='excel')
csv_write3 = csv.writer(f_write3, dialect='excel')
csv_write4 = csv.writer(f_write4, dialect='excel')
csv_write5 = csv.writer(f_write5, dialect='excel')
csv_write6 = csv.writer(f_write6, dialect='excel')
csv_write7 = csv.writer(f_write7, dialect='excel')
csv_write8 = csv.writer(f_write8, dialect='excel')
csv_write9 = csv.writer(f_write9, dialect='excel')
csv_write10 = csv.writer(f_write10, dialect='excel')

csv_write11 = csv.writer(f_write11, dialect='excel')
csv_write12 = csv.writer(f_write12, dialect='excel')
csv_write13 = csv.writer(f_write13, dialect='excel')
csv_write14 = csv.writer(f_write14, dialect='excel')
csv_write15 = csv.writer(f_write15, dialect='excel')
csv_write16 = csv.writer(f_write16, dialect='excel')
csv_write17 = csv.writer(f_write17, dialect='excel')
csv_write18 = csv.writer(f_write18, dialect='excel')
csv_write19 = csv.writer(f_write19, dialect='excel')
csv_write20 = csv.writer(f_write20, dialect='excel')

csv_write21 = csv.writer(f_write21, dialect='excel')
csv_write22 = csv.writer(f_write22, dialect='excel')
csv_write23 = csv.writer(f_write23, dialect='excel')
csv_write24 = csv.writer(f_write24, dialect='excel')
csv_write25 = csv.writer(f_write25, dialect='excel')
csv_write26 = csv.writer(f_write26, dialect='excel')
csv_write27 = csv.writer(f_write27, dialect='excel')
csv_write28 = csv.writer(f_write28, dialect='excel')
csv_write29 = csv.writer(f_write29, dialect='excel')
csv_write30 = csv.writer(f_write30, dialect='excel')

csv_write31 = csv.writer(f_write31, dialect='excel')
csv_write32 = csv.writer(f_write32, dialect='excel')
csv_write33 = csv.writer(f_write33, dialect='excel')
csv_write34 = csv.writer(f_write34, dialect='excel')
csv_write35 = csv.writer(f_write35, dialect='excel')
csv_write36 = csv.writer(f_write36, dialect='excel')
csv_write37 = csv.writer(f_write37, dialect='excel')
csv_write38 = csv.writer(f_write38, dialect='excel')
csv_write39 = csv.writer(f_write39, dialect='excel')
csv_write40 = csv.writer(f_write40, dialect='excel')
for i in range(row):
    csv_write1.writerow(msg_mx[i,0:200])
    csv_write2.writerow(msg_mx[i,200:400])
    csv_write3.writerow(msg_mx[i,400:600])
    csv_write4.writerow(msg_mx[i,600:800])
    csv_write5.writerow(msg_mx[i,800:1000])
    csv_write6.writerow(msg_mx[i,1000:1200])
    csv_write7.writerow(msg_mx[i,1200:1400])
    csv_write8.writerow(msg_mx[i,1400:1600])
    csv_write9.writerow(msg_mx[i,1600:1800])
    csv_write10.writerow(msg_mx[i,1800:2000])

    csv_write11.writerow(msg_mx[i, 2000:2200])
    csv_write12.writerow(msg_mx[i, 2200:2400])
    csv_write13.writerow(msg_mx[i, 2400:2600])
    csv_write14.writerow(msg_mx[i, 2600:2800])
    csv_write15.writerow(msg_mx[i, 2800:3000])
    csv_write16.writerow(msg_mx[i, 3000:3200])
    csv_write17.writerow(msg_mx[i, 3200:3400])
    csv_write18.writerow(msg_mx[i, 3400:3600])
    csv_write19.writerow(msg_mx[i, 3600:3800])
    csv_write20.writerow(msg_mx[i, 3800:4000])

    csv_write21.writerow(msg_mx[i, 4000:4200])
    csv_write22.writerow(msg_mx[i, 4200:4400])
    csv_write23.writerow(msg_mx[i, 4400:4600])
    csv_write24.writerow(msg_mx[i, 4600:4800])
    csv_write25.writerow(msg_mx[i, 4800:5000])
    csv_write26.writerow(msg_mx[i, 5000:5200])
    csv_write27.writerow(msg_mx[i, 5200:5400])
    csv_write28.writerow(msg_mx[i, 5400:5600])
    csv_write29.writerow(msg_mx[i, 5600:5800])
    csv_write30.writerow(msg_mx[i, 5800:6000])

    csv_write31.writerow(msg_mx[i, 6000:6200])
    csv_write32.writerow(msg_mx[i, 6200:6400])
    csv_write33.writerow(msg_mx[i, 6400:6600])
    csv_write34.writerow(msg_mx[i, 6600:6800])
    csv_write35.writerow(msg_mx[i, 6800:7000])
    csv_write36.writerow(msg_mx[i, 7000:7200])
    csv_write37.writerow(msg_mx[i, 7200:7400])
    csv_write38.writerow(msg_mx[i, 7400:7600])
    csv_write39.writerow(msg_mx[i, 7600:7800])
    csv_write40.writerow(msg_mx[i, 7800:8000])

print('Finish writing...')
