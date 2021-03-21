'''
使用Kmeans聚类算法，对“task4_1.csv"文件的数据进行聚类，
并进行雷达图可视化
'''

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data0 = pd.read_csv('../../data/task4_1.csv')
data = data0[['Recency', 'Monetary', 'Frequency']].copy()

# 数据标准化预处理
sc = StandardScaler()
standard_data = sc.fit_transform(data)

# 选取K值
SSE = []
for k in range(1, 9):
    estimator = KMeans(n_clusters=k)
    estimator.fit(standard_data)
    SSE.append(estimator.inertia_)
X = range(1, 9)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, 'o-')
plt.show()

# 模型构建与训练
model = KMeans(n_clusters=3, random_state=0, max_iter=500)
fit_model = model.fit(standard_data)
data0['类别'] = fit_model.predict(standard_data)
data0.to_csv('../../data/task4_2.csv', index=False)

# 模型可视化
print('聚类中心：\n', fit_model.cluster_centers_)  # 聚类中心
plt.rcParams['font.family'] = 'FangSong'
plt.rcParams['font.sans-serif'] = ['FangSong']
label = np.array(['Recency', 'Monetary', 'Frequency'])

angles = np.linspace(0, 2 * np.pi, 3, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))
centers = fit_model.cluster_centers_
plt_data = np.concatenate((centers, centers[:, [0]]), axis=1)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)
for i in range(len(plt_data)):
    ax.plot(angles, plt_data[i], 'o-', label=label[i])
ax.set_thetagrids(angles * 180 / np.pi, label)
# plt.legend(bbox_to_anchor=(0.8,1.15),ncol=3)
plt.legend(['第0类', '第1类', '第2类'])
plt.savefig('../../figures/雷达图.png')
plt.show()

x = [data0.loc[data0['类别'] == 0, 'Monetary'].count(),
     data0.loc[data0['类别'] == 1, 'Monetary'].count(),
     data0.loc[data0['类别'] == 2, 'Monetary'].count()]
plt.pie(x, explode=[0.01,0.01,0.01],
        labels=['第0类', '第1类', '第2类'],
        shadow=True,
        autopct='%.1f%%',
        pctdistance=0.7
        )
plt.title('各类会员数量')
plt.savefig('../../figures/各类会员人数之比.png')
plt.show()

y = [data0.loc[data0['类别'] == 0, 'Monetary'].sum(),
     data0.loc[data0['类别'] == 1, 'Monetary'].sum(),
     data0.loc[data0['类别'] == 2, 'Monetary'].sum()]
plt.pie(y, explode=[0.01,0.01,0.01],
        labels=['第0类', '第1类', '第2类'],
        shadow=True,
        autopct='%.1f%%',
        pctdistance=0.7
        )
plt.title('各类会员对总销售额的贡献')
plt.savefig('../../figures/各类会员消费额贡献之比.png')
plt.show()