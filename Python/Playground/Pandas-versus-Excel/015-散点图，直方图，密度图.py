import pandas as pd
import matplotlib.pyplot as plt

#显示所有列的数据
pd.options.display.max_columns = 777
homes = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_014_home_data.xlsx')

print(homes.head())

'''print('===================================')
#画直方图
homes.price.plot.hist(bins=100)
plt.xticks(range(0,max(homes.price),100000),fontsize = 8,rotation = 90)
plt.show()

print('==============================   =====')
#密度图
homes.sqft_living.plot.kde()
plt.xticks(range(0,max(homes.sqft_living),500),fontsize = 8,rotation = 90)
plt.show()'''

print(homes.corr())