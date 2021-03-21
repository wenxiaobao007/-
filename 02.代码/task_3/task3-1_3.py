'''
根据会员用户的兴趣特征，构建如下字段：
购物季节：春天、夏天、秋天、冬天
购物时间段：凌晨、上午、中午、下午、晚上

构建的特征保存在“task3_3.csv”文件中
'''

import pandas as pd

data = pd.read_csv('../../data/task3_2.csv')
task1 = pd.read_csv('../../data/会员购物情况表.csv',low_memory=False)
print(data.shape)  #(142701, 9)
print(task1.shape)  #(1013660, 12)

#购物季节
task1['消费时间'] = pd.to_datetime(task1['消费时间'])
task1['季节'] = pd.cut(task1['消费时间'].dt.month,
                     bins=[0,2,5,8,11,13],
                     labels=['冬天','春天','夏天','秋天','冬'])
task1.loc[task1['季节']=='冬','季节'] = '冬天'
df = task1[['会员卡号','季节']].groupby(by='会员卡号').max()
data = pd.merge(data,df,on='会员卡号',how='left')

#购物时间段
task1['购物时间段'] = pd.cut(task1['消费时间'].dt.hour,
                        bins=[0,6,11,14,18,24],
                        labels=['凌晨','上午','中午','下午','晚上'])
task1.drop(task1[task1['购物时间段'].isnull().values==True].index,inplace=True)
df1 = task1[['会员卡号','购物时间段']].groupby(by='会员卡号').max()
data = pd.merge(data,df1,on='会员卡号',how='left')

#保存
data.to_csv('../../data/task3_3.csv',index=False)