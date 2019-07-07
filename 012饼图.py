import pandas as pd
import matplotlib.pyplot as plt

#2016,2017年，在excel里面直接前面加了'，防止数字和其他数据混起来。导致出错。
students = pd.read_excel('012Students.xlsx',index_col='From')
print(students)
#只需要拿2017年的列数据即可。因此用serials就可以。
#以上饼图为逆时针，要改为顺时针，先需要把小数据排前面。.sort_values(ascending=True)
# students['2017'].sort_values(ascending=True).plot.pie(fontsize=8,startangle=-270) #默认为index的时候直接出来的标签是index，要出现国家，则要指定index_col为From
# plt.title('Source of International Students',fontsize=26,fontweight='bold')
# plt.ylabel('2017',fontsize=12,fontweight='bold')
# plt.show()

#改为顺时针也可以不用先排序，再改角度。通过counterclock改为False可以实现。
students['2017'].plot.pie(fontsize=8,counterclock=False)
plt.title('Source of International Students',fontsize=26,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold')
plt.show()