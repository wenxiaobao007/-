'''
随机选取一名会员进行画像，以词云图展示
'''

import pandas as pd
from wordcloud import WordCloud
from scipy.misc import imread
import matplotlib.pyplot as plt

data = pd.read_csv('../../data/task3_3.csv')

#选取一名会员并将其信息存到列表customer中
customer = list(data.iloc[19,:].values)
merchandise = customer.pop(-3)
merchandise = merchandise[2:-2].split()
customer.extend(merchandise)
print(customer)

#绘制词云图
##文本处理
customer[3] = '入会时长' + str(customer[3]) + '年'
customer[4] = '总消费金额' + str(customer[4]) + '元'
customer[7] = '消费次数' + str(customer[7]) + '次'
text = ' '.join(customer)

##创建词云对象
back_figure = imread('../../figures/词云底图2.jpg')
wordcloud = WordCloud(background_color='white',
                      width=2000,
                      height=1000,
                      margin=2,
                      max_words=100,
                      mask=back_figure,
                      font_path='simhei.ttf',
                      random_state=10)
w = wordcloud.generate(text)  # 传入需画词云图的文本
plt.imshow(w)
plt.axis('off')
plt.savefig('../../figures/词云图2.png')
plt.show()