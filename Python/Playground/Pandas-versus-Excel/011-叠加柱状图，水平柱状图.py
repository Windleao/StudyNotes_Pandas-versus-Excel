import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_011_Users.xlsx')
users['Total']=users['Oct']+users['Nov']+users['Dec']
users.sort_values(by='Total',inplace=True,ascending=True)
print(users)

users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Behavier') #竖状图叠加 图转90度【.bar改成.barh】
plt.tight_layout()
plt.show()


