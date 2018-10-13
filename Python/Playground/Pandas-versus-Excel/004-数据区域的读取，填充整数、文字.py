import pandas as pd
from  datetime import date , timedelta
print('=============================================')
#读取excel文件【books】
#忽略空行【skiprows=x】
#使用列数据【usecols='C:F'】
books = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_003_Books.xlsx',
                      index_col=None,usecols='C:F',dtype={'ID':str,'InStore':str,'Date':str}) #

# books['ID'].at[0]=1  #Series at函数
# print(books['ID'])

#循环生成序号
start = date[2018,1,1]
for i in books.index:
    books['ID'].at[i]=i+1 #填充序号
    books['InStore'].at[i]='Yes' if i%2 ==0 else 'No' #添加条件进行循环
    books['Date'].at[i] = start
print(books)