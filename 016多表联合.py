import pandas as pd
import matplotlib.pyplot as plt

#多个sheet表的用sheet_name找对应的数据表，读成独立的dataframe
# students = pd.read_excel('016Student_Score.xlsx',sheet_name='Students')
# scores = pd.read_excel('016Student_Score.xlsx',sheet_name='Scores')

#方法一：merge,默认innderjoin，这表没有数据的直接去掉了。可以修改merge模式通过how来改。students在左边，按left就是说学生表为基准，没有的也要保留学生。fillna把没有的值改为0.
#默认on不写merge会自动查找两张表一样的，按它来合并。但是制定了index_col的时候需要显式的写出on不然会出错。
#指定index的情况也可以写left_on=Students.index,right_on=Scores.index

# table = students.merge(scores,how = 'left',on='ID').fillna(0) #此时数据改为了float，可以通过astype改为int

#如果左边表和右边表的ID不一样。则on要用left_on,和right_on分开写
# table.Score = table.Score.astype(int)

#方法二：join
students = pd.read_excel('016Student_Score.xlsx',sheet_name='Students',index_col='ID')
scores = pd.read_excel('016Student_Score.xlsx',sheet_name='Scores',index_col='ID')
table = students.join(scores,how='left',on = 'ID').fillna(0) #join没有left_on和right_on
table.Score = table.Score.astype(int)
print(table)
