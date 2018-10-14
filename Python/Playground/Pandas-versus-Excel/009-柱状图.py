import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_009_Students.xlsx')
students.sort_values(by='Number',inplace=True,ascending=False)
print(students)
'''pandas 绘图'''
#students.plot.bar(x='Field',y='Number',color='orange',title='International Students by Field')
'''matplotlib 绘图'''
plt.bar(students.Field,students.Number,color='orange') #绘制柱状图，颜色为橙色
plt.xticks(students.Field,rotation = '45') #备注名为Field列，角度为45
plt.xlabel('Field') #X 坐标Field
plt.ylabel('Number') #Y 坐标Number
plt.title('International Students by Field',fontsize=16) #标题 ‘International Students by Field’ 字体：16
plt.tight_layout() #标签显示完整
plt.show()