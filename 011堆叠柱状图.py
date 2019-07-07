import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('011Users.xlsx')

users['Total'] = users.Oct+users.Nov+users['Dec']
print(users)
users.sort_values(by='Total',inplace=True,ascending=True)
#垂直显示，改为水平显示，只需要把bar改为barh
# users.plot.bar(x='Name',y=['Oct','Nov','Dec'],stacked=True,title = 'User Behavior')
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title = 'User Behavior')

plt.tight_layout()
plt.show()