'''
根据单据号字符，分别统计会员与非会员的订单数，并对结果进行可视化，
绘制了会员与非会员的订单数量饼状图、柱状图

'''

import pandas as pd
import matplotlib.pyplot as plt

#数据读取
data1 = pd.read_csv('../../data/会员购物情况表.csv')
data2 = pd.read_csv('../../data/非会员购物情况表.csv')

#绘饼状图
x = [data1.shape[0],data2.shape[0]]
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure()
plt.pie(x,
        labels=['会员','非会员'],
        explode=[0.02,0.02],
        shadow=True,
        autopct='%.1f%%',
        pctdistance=0.7)
plt.title('会员与非会员订单数')
plt.savefig('../../figures/会员与非会员订单数量.png')
plt.show()

#画柱状图
plt.figure()
plt.bar(range(2),x,color=['r','b'])
plt.xticks(range(2),['会员','非会员'])
for i in range(2):
        plt.text(i,x[i],str(x[i]))
plt.title('会员与非会员订单数量柱状图')
plt.savefig('../../figures/会员与非会员订单数量柱状图.png')
plt.show()