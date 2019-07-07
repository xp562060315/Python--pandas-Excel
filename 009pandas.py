#pandas只能做一些中规中矩的图
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('009Students.xlsx')

students.sort_values(by= ['Number'],inplace=True,ascending=False)
#用pandas绘图
# students.plot.bar(x='Field',y='Number',color='orange',title='International Students by Field')
# plt.tight_layout()#可以看到整个底部
# plt.show()

#用matplotlib绘图
plt.bar(students.Field,students.Number,color = 'orange')#此时底部字叠在一起
#把字旋转一下就好。
plt.xticks(students.Field,rotation='90')
#加x，y轴的标签
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Field',fontsize=16)
plt.tight_layout()
plt.show()