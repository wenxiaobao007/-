'''
对“cumcm2018c1.xlsx”进行预处理，预处理包括：
①去除卡号重复的记录
②将出生日期异常的通通标为1800年1月1日，以备用
③入会时间缺失的用众数填补
④将数据生成“会员信息表.csv”
⑤把出生日期正常的记录单独生成“有出生日期的会员信息表.csv”，以备用
'''


import pandas as pd

# 1.读取数据
data2 = pd.read_excel('..\\..\\data\\cumcm2018c1.xlsx')
print('预处理之前的记录数量：',data2.shape[0])

# 2.去除重复的会员卡号
before_shape = data2.shape
print('去重复值之前的数据：',before_shape)
data2.drop_duplicates('会员卡号',inplace=True)
after_shape = data2.shape
print('去缺失值后的数据：',after_shape)
print('共去除了{}条数据'.format(before_shape[0]-after_shape[0]))
del before_shape,after_shape

# 3.检查并去除异常值
## 3.1出生日期用特殊值1800/01/01填补缺失值
data3 = data2[~data2['出生日期'].isnull().values==True].copy()  #出生日期为非空值的会员数据
print('有出生日期记录的会员数量有：{}条'.format(data3.shape[0]))
print('没有出生日期记录的会员数量有：{}条'.format(data2.shape[0]-data3.shape[0]))
data2['出生日期'] = data2['出生日期'].fillna('1800/01/01')
data2['出生日期'] = pd.to_datetime(data2['出生日期'])
## 3.2用特殊出生日期1800/01/01替代异常的出生日期
print('1900年之前出生的定义为异常值，异常值有{}条'\
      .format(data2[data2['出生日期'].dt.year<1900].shape[0]))
data2.loc[(data2['出生日期'].dt.year>1800) & \
          (data2['出生日期'].dt.year<1900),'出生日期'] = pd.to_datetime('1800/01/01')
## 3.3 用众数填补入会时间缺失值
mode_year = int(data2['入会时间'].dt.year.mode())
data2['入会时间'] = data2['入会时间'].fillna('{}/01/01'.format(mode_year))
data2['入会时间'] = pd.to_datetime(data2['入会时间'])
## 3.4手动删除入会时间为1900年和2080年的3条数据
## 3.5删除性别不详的会员记录
print('性别不详的会员数量：',data2[data2['性别'].isnull().values==True].shape[0])
data2 = data2[~data2['性别'].isnull().values==True]

# 4.保存预处理结果
print('预处理完之后剩下的记录数量：',data2.shape[0])
data2.to_csv('..\\..\\data\\会员信息表.csv',index=False)
print('有出生日期记录的会员数量：',data3.shape[0])
data3.to_csv('..\\..\\data\\有出生日期的会员信息表.csv',index=False)