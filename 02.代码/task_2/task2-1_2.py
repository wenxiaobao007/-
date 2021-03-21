'''
统计不同年龄段的消费总额，并绘制饼状图、折线图
'''

import pandas as pd
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('D:\\python_files\\百货商场数据分析\\项目任务\data\\task1.csv',low_memory=False)

#导出年龄数据
data['出生日期'] = pd.to_datetime(data['出生日期'])
data['消费时间'] = pd.to_datetime(data['消费时间'])
data = data[data['出生日期'].dt.year >= 1900]
data['年龄'] = 2018 - data['出生日期'].dt.year

#导出不同年龄的消费总额
data1 = data[['年龄','消费金额']].groupby(by='年龄').sum()

#作不同年龄的消费金额图
plt.rcParams['font.sans-serif'] = ['FangSong']
x = [data1.iloc[:45,0].sum(),
     data1.iloc[45:60,0].sum(),
     data1.iloc[60:,0].sum()]
plt.figure()
plt.pie(x,
        labels=['青年人','中年人','老年人'],
        explode=[0.01,0.01,0.01],
        autopct='%.1f%%',
        pctdistance=0.7,)
plt.title('各年龄群消费金额图')
plt.savefig('../../figures/各年龄消费金额占比图.png')
plt.show()

#各个具体年龄消费金额图
plt.figure()
data1.plot()
plt.xlabel('年龄')
plt.ylabel('消费总金额')
plt.title('各具体年龄消费总额图')
plt.savefig('../../figures//各具体年龄消费总额图.png')
plt.show()
