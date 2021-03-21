'''
绘制了不同年份的会员消费总额的柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

#读取文件
data = pd.read_csv('../../data/会员购物情况表.csv')
data['消费时间'] = pd.to_datetime(data['消费时间'])

year = data['消费时间'].dt.year.unique()
x = []
for i in range(len(year)):
    x.append(data.loc[data['消费时间'].dt.year==year[i],'消费金额'].sum())

#绘制条形图
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.bar(range(4),x,color=list('rgbk'))
plt.xticks(range(4),year)
for i in range(4):
    plt.text(i-0.25,x[i],round(x[i]))
plt.ylabel('单位：元')
plt.title('会员每年消费总额图')
plt.savefig('../../figures/会员每年消费总额图.png')
plt.show()