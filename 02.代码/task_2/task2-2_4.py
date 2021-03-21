'''
按不同年份绘制了每个月的消费总额柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/会员购物情况表.csv')
data['消费时间'] = pd.to_datetime(data['消费时间'])

plt.rcParams['font.sans-serif'] = ['FangSong']
def plot_figure(x,year,xticks):
    plt.figure()
    plt.bar(range(len(x)),
            x,
            color='g')
    plt.title(str(year)+'年会员每月消费总金额')
    plt.ylabel('单位：元')
    plt.xlabel('月份')
    plt.xticks(range(len(x)),xticks)
    for i in range(len(x)):
        plt.text(i-0.5,x[i],round(x[i]))
    filename = '../../figures/' + str(year)+'年会员每月消费总金额.png'
    plt.savefig(filename)
    plt.show()

year = data['消费时间'].dt.year.unique()
month_data = {}
for i in range(len(year)):
    df = data[data['消费时间'].dt.year==year[i]]
    months = df['消费时间'].dt.month.unique()
    month_list = []
    for j in range(len(months)):
        month_list.append(df.loc[df['消费时间'].dt.month==months[j],'消费金额'].sum())
    month_data[year[i]] = [month_list,months]

for y in year:
    plot_figure(x=month_data[y][0],year=y,xticks=month_data[y][1])

