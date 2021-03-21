'''
绘制了会员与非会员的消费总额饼状图、柱状图
绘制了会员与非会员平均每单消费额柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

#数据读取
data1 = pd.read_csv('../../data/会员购物情况表.csv')
data2 = pd.read_csv('../../data/非会员购物情况表.csv')

#画消费总额饼状图
x = [data1['消费金额'].sum(),data2['消费金额'].sum()]
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure()
plt.pie(x,
        labels=['会员','非会员'],
        explode=[0.02,0.02],
        shadow=True,
        autopct='%.1f%%',
        pctdistance=0.7)
plt.title('会员与非会员消费总额')
plt.savefig('../../figures/会员与非会员消费总额.png')
plt.show()

#画消费总额柱状图
plt.figure()
plt.bar(range(2),x,color=['r','b'])
plt.xticks(range(2),['会员','非会员'])
for i in range(2):
        plt.text(i,x[i],str(x[i]))
plt.title('会员与非会员消费总额柱状图')
plt.savefig('../../figures/会员与非会员消费总额柱状图.png')
plt.show()

#画平均每单消费额饼状图
x = [data1['消费金额'].mean(),data2['消费金额'].mean()]
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure()
plt.pie(x,
        labels=['会员','非会员'],
        explode=[0.02,0.02],
        shadow=True,
        autopct='%.1f%%',
        pctdistance=0.7)
plt.title('会员与非会员平均每单消费额')
plt.savefig('../../figures/会员与非会员平局每单消费额.png')
plt.show()

#画平均每单消费额柱状图
plt.figure()
plt.bar(range(2),x,color=['r','b'])
plt.xticks(range(2),['会员','非会员'])
for i in range(2):
        plt.text(i,x[i],str(x[i]))
plt.title('会员与非会员平均每单消费额柱状图')
plt.savefig('../../figures/会员与非会员平均每单消费额柱状图.png')
plt.show()
