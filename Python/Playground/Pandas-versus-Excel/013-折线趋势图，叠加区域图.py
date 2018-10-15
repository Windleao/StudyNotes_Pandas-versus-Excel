import pandas as pd
import matplotlib.pyplot as plt

week = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_013_Orders.xlsx',index_col='Week')

print(week)
print(week.columns)

#week.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components']) #多条折线图
week.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components']) #叠加区域图
week.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Components'],stacked=True) #叠加柱状图
plt.title('Sales Weekly Trend',fontsize=16,fontweight='bold') #标题
plt.ylabel('Total',fontsize=12,fontweight='bold') #y轴标题
plt.xticks(week.index,fontsize=8)
plt.show()