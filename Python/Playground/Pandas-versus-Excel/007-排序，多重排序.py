import pandas as pd

products = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_007_List.xlsx',index_col='ID')
#排序 最贵的产品
#products.sort_values(by='Price',inplace=True,ascending=False) #ascending=False 降序

#排序 不值得的产品里那个最贵【值不值，贵不贵】
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])

print(products)