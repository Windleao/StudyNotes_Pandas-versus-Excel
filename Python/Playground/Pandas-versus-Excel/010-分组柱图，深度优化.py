import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_010_Students.xlsx')

students.sort_values(by='2017',inplace=True,ascending=False)
print(students)
students.plot.bar(x='Field',y=['2016','2017'],color=['red','orange'])
plt.title('International Students by Field',fontsize=16,fontweight='bold')
plt.xlabel('Field',fontweight='bold') #X 坐标Field
plt.ylabel('Number',fontweight='bold') #Y 坐标Number
ax = plt.gca()
ax.set_xticklabels(students['Field'],rotation=45,ha='right')
f = plt.gcf()
f.subplots_adjust(left=0.2,bottom=0.42) #子图形调整
#plt.tight_layout() #标签显示完整
plt.show()