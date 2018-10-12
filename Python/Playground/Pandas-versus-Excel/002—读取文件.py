import  pandas as pd

# 读取excel文件【people】
people = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_People.xlsx')

print(people.shape) #shape 查看出多少行多少列
print(people.columns) #colums 列名是什么
print(people.head(100)) #head(x) 前x条数据，默认为x=5
print('=========================================')
print(people.tail(20)) #tail(n) 前x条数据，默认为n=5
print('Done!')

print('==========================================================')
#读取excel文件【people】 文件内有杂乱数据，进行梳理
people2 = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_People2.xlsx',header=2) #header=x 忽略前x列，x默认为0
print(people2.columns)

print('==========================================================')
#读取excel文件【people】 文件内没有列名
people3 = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_People3.xlsx',header=None)#header=None 读取excel时不要设置header


print('==========================================================')
#人为的设置列名
people3.columns = ['ID','Type','Title','FirstName','MiddleName','LastName']
people4 = people3.set_index('ID') #将ID列设置为索引
#people4 = people3.set_index('ID',inplace=True) #直接改，不生成新的索引
print(people4.columns)
people4.to_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_002_People4.xlsx')
print('Done!')


print('==========================================================')
#在读取文件时，知道某列为索引的话，可提前指明
df = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_001_output2.xlsx',index_col='ID')
df.to_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_001_output3.xlsx')
print(df.head())



