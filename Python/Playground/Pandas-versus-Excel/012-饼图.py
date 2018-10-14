import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_012_Students.xlsx',index_col='From')

#顺时针排序 【1、数据排序 小 大】 .sort_values(ascending=True)
print(students)
students['2017'].sort_values(ascending=True).plot.pie(fontsize=8,startangle=-270) # 从上方开始 startangle=-270
plt.title('Source of International Students',fontsize=16,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold')
plt.axis('equal')#画正圆
plt.show()