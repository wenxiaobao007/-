'''
把一天划分为以下几个时间段
凌晨：00：00-06：00
上午：06：00-11：00
中午：11：00-14：00
下午：14：00-18：00
晚上：18：00-24：00
并对会员再每个时间段的消费总额进行了统计，
根据统计结果绘制了柱状图、饼状图
'''

import pandas as pd
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('../../data/会员购物情况表.csv')
data['消费时间'] = pd.to_datetime(data['消费时间'])


#各时间段消费金额提取
x = []
x.append(data.loc[data['消费时间'].dt.hour < 6,'消费金额'].sum())
x.append(data.loc[(data['消费时间'].dt.hour>=6) & (data['消费时间'].dt.hour<11),'消费金额'].sum())
x.append(data.loc[(data['消费时间'].dt.hour>=11) & (data['消费时间'].dt.hour<14),'消费金额'].sum())
x.append(data.loc[(data['消费时间'].dt.hour>=14) & (data['消费时间'].dt.hour<18),'消费金额'].sum())
x.append(data.loc[(data['消费时间'].dt.hour>=18) & (data['消费时间'].dt.hour<=23),'消费金额'].sum())

#绘制柱状图
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.bar(x=range(5),height=x,color=list('rgbkr'))
for i in range(5):
    plt.text(i-0.25,x[i],round(x[i]))
plt.xticks(range(5),['凌晨','上午','中午','下午','晚上'])
plt.title('会员在各个时间段的消费总额')
plt.ylabel('单位：元')
plt.savefig('../../figures/会员在各个时间段的消费金额柱状图.png')
plt.show()

#绘制饼状图
plt.figure()
plt.pie(x=x,
        labels=['凌晨','上午','中午','下午','晚上'],
        shadow=True,
        autopct='%.4f%%',
        pctdistance=0.7)
plt.title('会员在各个时间段消费金额饼图')
plt.savefig('../../figures/会员在各个时间段消费金额饼图.png')
plt.show()