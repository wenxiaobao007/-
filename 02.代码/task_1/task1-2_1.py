'''
把“会员信息表.csv”和“会员购物情况表.csv”合并成“task1.csv”，合并方式为外连接
'''

import pandas as pd

table_1 = pd.read_csv('../../data/会员信息表.csv')
table_2 = pd.read_csv('../../data/会员购物情况表.csv')

table = pd.merge(table_1,table_2,how='outer',on='会员卡号')
table.to_csv('..\\..\\data\\task1.csv',index=False)