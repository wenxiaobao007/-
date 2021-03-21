'''
构建会员基本特征，主要有如下
年龄段：[青年人，中年人，老年人]；
性别：[男，女]
入会时长：0，1，2，...
消费金额：

添加的特征保存在“task3_1.csv”
'''

import pandas as pd
import numpy as np

task1 = pd.read_csv('../../data/task1.csv',low_memory=False)
data = pd.read_csv('../../data/会员信息表.csv')

#性别特征
data['性别'] = data['性别'].map({1.0:'男',0.0:'女'})

#年龄段
data['出生日期'] = pd.to_datetime(data['出生日期'])
data['年龄段'] = '未知'
data.loc[(2018-data['出生日期'].dt.year<=44)&(2018-data['出生日期'].dt.year>=0),'年龄段'] = '青年人'
data.loc[(2018-data['出生日期'].dt.year<=59)&(2018-data['出生日期'].dt.year>=45),'年龄段'] = '中年人'
data.loc[(2018-data['出生日期'].dt.year<=100)&(2018-data['出生日期'].dt.year>=60),'年龄段'] = '老年人'
data.drop(data[data['年龄段']=='未知'].index, inplace=True)

#入会时长
data['入会时间'] = pd.to_datetime(data['入会时间'])
data['入会时长'] = 2018 - data['入会时间'].dt.year

#消费金额
cumsume = task1[['会员卡号','消费金额']].groupby(by='会员卡号').sum()
data = pd.merge(data,cumsume,on='会员卡号',how='inner')

data.to_csv('../../data/task3_1.csv',index=False)