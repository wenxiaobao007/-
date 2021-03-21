'''
根据业务特征构建的特征标签有：
消费水平：[低消费，中等消费，高消费]
新老会员：[新会员，老会员]
总消费次数：int
购买过的商品：

添加的特征保存在“task3_2.csv”
'''

import pandas as pd
import numpy as np

task1 = pd.read_csv('../../data/task1.csv',low_memory=False)
data = pd.read_csv('../../data/task3_1.csv')

#消费水平
data['消费水平'] = pd.cut(data['消费金额'],
                      bins=[-0.001,300,1500,10000000000],
                      labels=['低消费','中等消费','高消费'])

#新老会员
data['新老会员'] = pd.cut(data['入会时长'],
                      bins=[-0.1,5,17],
                      labels=['新会员','老会员'])

#总消费次数
count = task1[['会员卡号','消费金额']].groupby(by='会员卡号').count()
data = pd.merge(data,count,how='inner',on='会员卡号')
data.rename({'消费金额_y':'消费次数'},axis=1,inplace=True)

#购买过的商品
df = task1[['会员卡号','商品名称']].groupby(by='会员卡号').\
    agg(购买过的商品=pd.NamedAgg(column='商品名称', aggfunc=np.array))
data = pd.merge(data,df,on='会员卡号',how='inner')

#删除无关特征
data.drop(['出生日期','入会时间'],axis=1,inplace=True)

#保存处理结果
data.to_csv('../../data/task3_2.csv',index=False)
