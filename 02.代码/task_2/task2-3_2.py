'''
把一年分为春夏秋冬四个季节，分别统计会员在各年的各个季节中的消费总额，
并根据季节和年份绘制了柱状图
'''

import pandas as pd
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('../../data/会员购物情况表.csv')
data['消费时间'] = pd.to_datetime(data['消费时间'])

#定义绘图函数
plt.rcParams['font.sans-serif'] = ['FangSong']
def plot_figure(x,year,xticks):
    plt.figure()
    plt.bar(range(len(x)),
            x,
            color='r')
    plt.title(str(year)+'年各季度会员消费人数')
    plt.ylabel('单位：人')
    plt.xlabel('季度')
    plt.xticks(range(len(x)),xticks)
    for i in range(len(x)):
        plt.text(i,x[i],round(x[i]))
    filename = '../../figures/' + str(year)+'年各季度会员消费人数.png'
    plt.savefig(filename)
    plt.show()

years = [2015,2016,2017]
season_dict = {}
for year in years:
    df = data[data['消费时间'].dt.year==year]
    x = []
    x.append(df[(df['消费时间'].dt.month==3) | \
                (df['消费时间'].dt.month==4) | \
                (df['消费时间'].dt.month==5)].shape[0])
    x.append(df[(df['消费时间'].dt.month == 6) | \
                (df['消费时间'].dt.month == 7) | \
                (df['消费时间'].dt.month == 8)].shape[0])
    x.append(df[(df['消费时间'].dt.month == 9) | \
                (df['消费时间'].dt.month == 10) | \
                (df['消费时间'].dt.month == 11)].shape[0])
    x.append(df[(df['消费时间'].dt.month == 12) | \
                (df['消费时间'].dt.month == 1) | \
                (df['消费时间'].dt.month == 2)].shape[0])
    season_dict[year] = x

#绘图并保存
for year in years:
    plot_figure(x=season_dict[year],
                year=year,
                xticks=['春季','夏季','秋季','冬季'])