#使用pandas进行数据筛选

import pandas as pd

#条件一：年龄大于18小于30岁的
# def age_18_to_30(a):
#     return 18<=a<30
#条件二：分数大于85小于100
# def level_a(s):
#     return 85<=s<=100

students = pd.read_excel('008Students.xlsx',index_col='ID')
#loc后面必须跟方括号
# students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
# students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]

#lambda函数优化
students = students.loc[students.Age.apply(lambda x:18<=x<30)].loc[students.Score.apply(lambda x:85<=x<=100)]


print(students)