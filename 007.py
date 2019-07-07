import pandas as pd

products = pd.read_excel('007List.xlsx',index_col='ID')
#inplace是否用排序后的数据集替换原来的数据，默认为False，即不替换
#ascending默认为True，就是从小到大排序。
# products.sort_values(by='Price',inplace=True,ascending=False)
#两列排序
# products.sort_values(by=['Worthy','Price'],inplace=True)
'''           Name  Price Worthy
ID                           
12  Product_012   7.29     No
6   Product_006   7.34     No
9   Product_009   8.98     No
3   Product_003   9.62     No
15  Product_015  10.31     No
18  Product_018  11.22     No
5   Product_005   7.75    Yes
11  Product_011   8.31    Yes
13  Product_013   8.36    Yes
20  Product_020   8.82    Yes
14  Product_014   9.16    Yes
10  Product_010   9.18    Yes
1   Product_001   9.82    Yes
16  Product_016  10.26    Yes
19  Product_019  10.95    Yes
7   Product_007  10.97    Yes
4   Product_004  11.08    Yes
8   Product_008  11.14    Yes
17  Product_017  11.95    Yes
2   Product_002  11.99    Yes'''
#如果需要保持No,Yes顺序，再按价格降序排列。单独加ascending会将全部倒过来。可以用列表实现，就是worthy对应True，Price对应False降序。
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])
print(products)