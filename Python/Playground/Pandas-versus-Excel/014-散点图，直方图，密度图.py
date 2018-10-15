import pandas as pd
import matplotlib.pyplot as plt

#显示所有列的数据
pd.options.display.max_columns = 777
homes = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_014_home_data.xlsx')

print(homes.head())

print('===================================')
#画散点图
homes.plot.scatter(y='sqft_living',x='price')
plt.show()

print('===================================')
#画直方图