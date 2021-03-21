'''
对cumcm2018c2.csv文件进行预处理，预处理包括：
①更改中文列名
②去除重复值
③去除异常值
④筛选特征
⑤将会员数据和非会员暑假区分
⑥会员暑假生成“会员购物情况表.csv”，非会员数据生成“非会员购物情况表.csv”
'''

import pandas as pd

#读取数据
data = pd.read_csv('../../data/cumcm2018c2.csv', low_memory=False)

#更改列名
columns = ['会员卡号','消费时间','商品编码','销售数量','商品售价',
           '消费金额','商品名称','积分','收银机号',
           '单据号','柜组编码','柜组名称']
data.columns = columns

#去除重复值
before_shape = data.shape
print('去重复值之前的数据：',before_shape)
data.drop_duplicates(inplace=True)
after_shape = data.shape
print('去缺失值后的数据：',after_shape)
print('共去除了{}条数据'.format(before_shape[0]-after_shape[0]))
del before_shape,after_shape

#去除异常值
data['消费时间'] = pd.to_datetime(data['消费时间'])
#print(data.loc[data['消费时间'].dt.year==2019].shape)
#经查，数据皆是2015、2016、2017、2018年的，并无2019年数据

#筛选特征
data.drop(['柜组名称','柜组编码','收银机号'],axis=1,inplace=True)

#缺失值处理
print(data.isnull().sum())
print('去除缺失值前的数据：',data.shape)
non_vip_data = data[data.isnull().values==True].copy()
data.dropna(axis=0,how='any',inplace=True)
print('去缺失值后的数据：',data.shape)

#保存预处理结果
data.to_csv('..\\..\\data\\会员购物情况表.csv',index=False)
non_vip_data.to_csv('..\\..\\data\\非会员购物情况表.csv',index=False)






