import pandas as pd
from datetime import  date,timedelta

print('=====================================')
#月份逻辑算法计算
def add_month(d,md):
    yd = md // 12 #月份整除12，得出年份
    m = d.month + md % 12 #当前月份加上月份取余12
    if m != 12:
        yd += m //12
        m = m % 12
    return date(d.year+yd,m,d.day)

books = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_005_Books.xlsx',skiprows=3,usecols='C:F',index_col=None,dtype={'ID':str,'InStore':str,'Date':str})

start = date(2018,10,1)
for i in books.index:
    '''方法一：Series 使用列改行的值【行列确定单元格】
    books['ID'].at[i] = i+1
    books['InStore'].at[i] = 'Yes' if i%2 ==0 else 'No'
    # 日期上加1 timedelta(days=i)
    #books['Date'].at[i] = start+timedelta(days=i)
    #年份上加1 date(start.year+i,start.month,start.day)
    #books['Date'].at[i] = date(start.year+i,start.month,start.day)
    #月份上加1  def add_month 调用自定义函数
    books['Date'].at[i] = add_month(start,i)'''

    '''方法二：DataFrame 找出单元格，修改单元格的值【直接找出单元格】'''
    books.at[i,'ID'] = i+1
    books.at[i,'InStore'] ='Yes' if i%2 ==0 else 'No'
    books.at[i,'Date'] = add_month(start,i)
print(books)

#保存文件
#不生成index的列
books.set_index('ID',inplace=True)
books.to_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_005_完成版_Books.xlsx')
print('Done!')


