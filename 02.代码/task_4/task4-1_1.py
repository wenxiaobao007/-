'''
构建的价值分析特征指标主要有：
①Recency  最后一次消费时间与截止日期的间隔
②Frequency 每年消费频率
③Monetary  总消费额
'''

import pandas as pd

data = pd.read_csv('../../data/task3_3.csv')
task1 = pd.read_csv('../../data/task1.csv',low_memory=False)
task1['消费时间'] = pd.to_datetime(task1['消费时间'])

# Recency
task1['Recency'] = pd.to_datetime('2018/01/31') - task1['消费时间']
task1['Recency'] = task1['Recency'].dt.days
df = task1[['会员卡号','Recency']].groupby(by='会员卡号').min()
df = df.dropna()
data = pd.merge(data,df,on='会员卡号')

#Monetary
data.rename({'消费金额_x':'Monetary'},axis=1,inplace=True)

#Frequency
data['Frequency'] = round(data['消费次数'] /3,4)

data[['会员卡号','Recency','Monetary','Frequency']].to_csv('../../data/task4_1.csv',index=False)



# data['消费频率'] = round(data['消费次数']/3,2)
# data['平均每次消费金额'] = data['消费金额_x'] / data['消费次数']
# data['平均每次消费金额'].fillna(0,inplace=True)
# data['平均每次消费金额'] = round(data['平均每次消费金额'],2)
#
# data[['会员卡号','入会时长','消费频率','平均每次消费金额']].to_csv('../../data/task4_1.csv',index=False)






