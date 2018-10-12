import pandas as pd

df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Tom','David'],'Age':[22,25,29]})  #DataFrame:数据帧【对于excel的worksheet】
df.to_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_001_output.xlsx')
print(df)
print('Done!')

print('===============================================================')
#ID列 设置为索引
df2 = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Tom','David'],'Age':[22,25,29]})  #DataFrame:数据帧【对于excel的worksheet】
df2.to_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_output.xlsx')
df2 = df2.set_index('ID') #ID列 设置为索引
print(df2)
print('Done2!')


