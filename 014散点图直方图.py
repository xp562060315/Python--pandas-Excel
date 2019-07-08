#散点图，直方图（比如价格，或者面积的集中区间，按区间分出来），密度图（一个西雅图地区的房子有多大概率为70多万？）
import pandas as pd
import matplotlib.pyplot as plt

#有些列无法显示，可以通过以下修改处理。
pd.options.display.max_columns = 777
homes = pd.read_excel('014home_data.xlsx')
#散点图
# homes.plot.scatter(x='price',y = 'sqft_living')

#面积的直方图，默认的分布区间比较少可以改变你bins
# homes.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation = 90)

#价格的直方图
# homes.price.plot.hist(bins=100)
# plt.xticks(range(0,max(homes.price),100000),fontsize=8,rotation = 90)

#密度图
# homes.sqft_living.plot.kde()
# plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation = 90)
#
# plt.show()

#查看两两之间的相关性
print(homes.corr())
'''                     id     price  bedrooms  bathrooms  sqft_living  \
id             1.000000 -0.016762  0.001286   0.005160    -0.012258   
price         -0.016762  1.000000  0.308350   0.525138     0.702035   
bedrooms       0.001286  0.308350  1.000000   0.515884     0.576671   
bathrooms      0.005160  0.525138  0.515884   1.000000     0.754665   
sqft_living   -0.012258  0.702035  0.576671   0.754665     1.000000   
sqft_basement -0.005151  0.323816  0.303093   0.283770     0.435043   
sqft_lot      -0.132109  0.089661  0.031703   0.087740     0.172826   
floors         0.018525  0.256794  0.175429   0.500653     0.353949   
yr_built       0.021380  0.054012  0.154178   0.506019     0.318049'''