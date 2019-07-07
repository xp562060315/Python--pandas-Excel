import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('010Students.xlsx')
print(students)
students.sort_values(by='2017',inplace=True,ascending=False)
students.plot.bar(x='Field',y=['2016','2017'],color=['orange','red'],)
plt.title('Internations students by field',fontsize=16,fontweight='bold')
plt.xlabel('Field',fontweight='bold')
plt.ylabel('Number',fontweight='bold')

# plt.xticks(rotation=45,ha='right')
ax = plt.gca()
#旋转是以中心旋转的，故不会对齐
# ax.set_xticklabels(students['Field'],rotation=45)
ax.set_xticklabels(students['Field'],rotation=45,ha='right') #ha水平对齐
#边缘空白比较多
f = plt.gcf()
f.subplots_adjust(left=0.2,bottom=0.42)
# plt.tight_layout()
plt.show()

