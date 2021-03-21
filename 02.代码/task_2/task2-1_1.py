'''
将会员按年龄分为青年人、中年人、老年人，并绘制饼状图并保存
44岁以下为青年人，44岁至59岁为中年人，60岁以上为老年人
'''

import pandas as pd
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('..\\..\\data\\有出生日期的会员信息表.csv')
data['出生日期'] = pd.to_datetime(data['出生日期'])

#年龄构成饼图, 44岁以下为青年人，44岁至59岁为中年人，60岁以上为老年人
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure()
plt.pie([data[2018-data['出生日期'].dt.year <= 44].shape[0],
         data[(2018-data['出生日期'].dt.year > 44) & \
              (2018-data['出生日期'].dt.year < 60)].shape[0],
         data[2018-data['出生日期'].dt.year >= 44].shape[0]],
        labels=['青年人','中年人','老年人'],
        explode=[0.01,0.01,0.01],
        autopct='%.1f%%',
        pctdistance=0.7,)
plt.title('会员年龄占比图')
plt.savefig('..\\..\\figures\\会员年龄占比图.png')
plt.show()

