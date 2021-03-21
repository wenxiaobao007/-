'''
统计不同性别的消费金额比例和人数比例，并绘制饼状图、柱状图
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('D:\\python_files\\百货商场数据分析\\项目任务\data\\task1.csv',low_memory=False)
data1 = pd.read_csv('../../data/会员信息表.csv')

#会员性别比例图
rito = [data1[data1['性别']==1].shape[0],
        data1[data1['性别']==0].shape[0]]
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure()
plt.bar([1,2],rito,color=['r','g'],width=0.5)
plt.xticks([1,2],['男','女'])
plt.text(1,rito[0],str(rito[0]))
plt.text(2,rito[1],str(rito[1]))
plt.text(1,0.5*rito[0],str(round(rito[0]/sum(rito),2)))
plt.text(2,0.5*rito[1],str(round(rito[1]/sum(rito),2)))
plt.title('男女人数对比图')
plt.savefig('../../figures/男女人数对比图.png')
plt.show()

plt.figure()
plt.pie(rito[::-1],
        labels=['女人','男人'],
        explode=[0.01,0.01],
        autopct='%.1f%%',
        pctdistance=0.7,)
plt.title('男女人数占比')
plt.savefig('../../figures/男女人数占比.png')
plt.show()

#男女消费总金额对比
data2 = data[['性别','消费金额']].groupby(by='性别').sum()
plt.figure()
plt.pie(data2.values,
        labels=['女人','男人'],
        explode=[0.01,0.01],
        autopct='%.1f%%',
        pctdistance=0.7,)
plt.title('男女消费总金额占比')
plt.savefig('../../figures/男女消费总金额占比.png')
plt.show()
