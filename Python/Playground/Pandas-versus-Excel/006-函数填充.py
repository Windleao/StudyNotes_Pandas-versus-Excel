import pandas as pd

books = pd.read_excel('D:\OneDrive\OneDrive - LingFeng\H-CodingWorld\Python\Playground\Pandas-versus-Excel\Temp\Demo_006_Books.xlsx',index_col='ID')

#函数
def add_2(x):
    return x + 2

'''方式一：思维上转换，excel操作的是单元格；pandas操作的是行或列'''
#计算出最终的价格
#books['Price'] = books['ListPrice']*books['Discount']
'''操作符的重载    *'''

'''方式二：用循环来完成计算，【不想从头到尾运算时，推荐！！！】
#从头到尾运算
for i in books.index:
        books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i] 
#从5到20运算
for i in range(5,20):
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]'''

'''书籍涨价2元'''
#方式一：本身+2
#books['ListPrice'] = books['ListPrice']+2
#方式二： Series的函数apply
#books['ListPrice'] = books['ListPrice'].apply(add_2)
#方式三：lambda表达式
books['ListPrice'] = books['ListPrice'].apply(lambda x:x+5)
print(books)